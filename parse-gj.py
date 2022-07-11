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

csv_file = open('output.csv', 'w')
# LF_20_AiAn', 'CVAP_15-19_American Indian or Alaska Native Alone',
# 'CVAP_15-19_White Alone', 'CVAP_15-19_Native Hawaiian or Other Pacific Islander Alone',
# 'LF_20_HoPI', 'LF_20_White'
fieldnames = [
	'LF_20_AfAm',
	'LF_20_Asian',
	'LF_20_Hispanic_or_Latino',
	'CVAP_15-19_Total',
	'CVAP_15-19_Black or African American Alone',
	'CVAP_15-19_Asian Alone',
	'CVAP_15-19_Hispanic or Latino',
]
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
def to_fields(props):
	outprops = {}
	for field in fieldnames:
		outprops[field] = props[field]
	return outprops

for idx, f in enumerate(features):
	op_features.append({
		"type": "Feature",
		"geometry": f['geometry'],
		"properties": {
			"GEOINDEX": idx,
			"TOTPOP": f['properties']['LF_20_Total']
		},
	})
	writer.writerow(to_fields(f['properties']))

open('output.geojson', 'w').write(json.dumps({
	"type": "FeatureCollection",
	"crs": gj['crs'],
	"features": op_features,
}))

#print(features[:5])
