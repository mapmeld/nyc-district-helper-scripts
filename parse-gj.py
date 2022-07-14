# Load GeoJSON file
# Replace GEOID20 with a GEOINDEX with 0 being the lowest Census GEOID20
# Move all columns except for GEOINDEX and TOTPOP into a CSV for server reference
# Output the new GeoJSON with GEOINDEX and TOTPOP

import json
import csv

gj = json.load(open('./City_of_New_York_Blocks.geojson', 'r'))

# print(len(gj['features']))

features = list(sorted(gj['features'], key=lambda f: f['properties']['GEOID20']))
op_features = []

csv_file = open('nyc-data.csv', 'w')

fieldnames = [
	'LF_20_AfAm',
	'LF_20_Asian',
	'LF_20_Hispanic_or_Latino',
	'Others',
	'CVAP_15-19_Total',
	'CVAP_15-19_Black or African American Alone',
	'CVAP_15-19_Asian Alone',
	'CVAP_15-19_Hispanic or Latino',
	'CVAP_Others',
]


def run_stuff():
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	total_others = 0
	max_others = 0
	total_ocvap = 0
	max_ocvap = 0

	for idx, f in enumerate(features):
		op_features.append({
			"type": "Feature",
			"geometry": f['geometry'],
			"properties": {
				"GEOINDEX": idx,
				"TOTPOP": f['properties']['LF_20_Total']
			},
		})
		props = f['properties']
		outprops = {}
		for field in fieldnames:
			if field in props:
				outprops[field] = props[field]
		# add other and cvap_other
		outprops['Others'] = props['LF_20_AiAn'] + props['LF_20_HoPI'] + props['LF_20_White']
		total_others += outprops['Others']
		max_others = max(max_others, outprops['Others'])
		outprops['CVAP_Others'] = props['CVAP_15-19_American Indian or Alaska Native Alone'] + props['CVAP_15-19_White Alone'] + props['CVAP_15-19_Native Hawaiian or Other Pacific Islander Alone']
		total_ocvap += outprops['CVAP_Others']
		max_ocvap = max(max_ocvap, outprops['CVAP_Others'])
		writer.writerow(outprops)

		print([
			total_others,
			max_others,
			total_ocvap,
			max_ocvap,
		])

run_stuff()

open('output.geojson', 'w').write(json.dumps({
	"type": "FeatureCollection",
	"crs": gj['crs'],
	"features": op_features,
}))

#print(features[:5])
