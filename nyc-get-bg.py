import json

bg_data = {}

gj = json.load(open('./City_of_New_York_Blocks.geojson', 'r'))

fieldnames = [
    'TOTPOP',
	'LF_20_AfAm',
	'LF_20_Asian',
	'LF_20_Hispanic_or_Latino',
	# 'Others',
	'CVAP_15-19_Total',
	'CVAP_15-19_Black or African American Alone',
	'CVAP_15-19_Asian Alone',
	'CVAP_15-19_Hispanic or Latino',
	# 'CVAP_Others',
]

for feature in gj['features']:
    # bg id 360419505001
    block = feature['properties']['GEOID20']
    bg_id = block[:12]

    if bg_id not in bg_data:
        bg_data[bg_id] = {
            'TOTPOP': 0,
        	'LF_20_AfAm': 0,
        	'LF_20_Asian': 0,
        	'LF_20_Hispanic_or_Latino': 0,
        	'Others': 0,
        	'CVAP_15-19_Total': 0,
        	'CVAP_15-19_Black or African American Alone': 0,
        	'CVAP_15-19_Asian Alone': 0,
        	'CVAP_15-19_Hispanic or Latino': 0,
        	'CVAP_Others': 0,
        }
    for field in fieldnames:
        bg_data[bg_id][field] += feature['properties'][field.replace("TOTPOP", "LF_20_Total")]
    bg_data[bg_id]['Others'] = feature['properties']['LF_20_AiAn'] + feature['properties']['LF_20_HoPI'] + feature['properties']['LF_20_White']
    bg_data[bg_id]['CVAP_Others'] = feature['properties']['CVAP_15-19_American Indian or Alaska Native Alone'] + feature['properties']['CVAP_15-19_White Alone'] + feature['properties']['CVAP_15-19_Native Hawaiian or Other Pacific Islander Alone']

ny = json.load(open('./nyc-bg-src.geojson', 'r'))
op_features = []
fieldnames += ['Others', 'CVAP_Others']
for bg in ny["features"]:
    if bg["properties"]["GEOID"] in bg_data:
        for field in fieldnames:
            bg["properties"][field] = bg_data[bg["properties"]["GEOID"]][field]
        op_features.append(bg)

open('./nyc-bg-final.geojson', 'w').write(json.dumps({
    "type": "FeatureCollection",
    "crs": ny["crs"],
    "features": op_features,
}))
