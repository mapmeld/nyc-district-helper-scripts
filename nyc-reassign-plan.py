# Load GeoJSON file
# Replace GEOID20 with a GEOINDEX with 0 being the lowest Census GEOID20
# Move all columns except for GEOINDEX and TOTPOP into a CSV for server reference
# Output the new GeoJSON with GEOINDEX and TOTPOP

import json
import csv

assigned = {}
first = True
for row in open('./DraftA.csv', 'r').read().split('\n'):
	if first:
		first = False
		continue
	vals = row.strip().split(',')
	if len(vals) > 1:
		assigned[vals[0]] = int(vals[1]) - 1

gj = json.load(open('./City_of_New_York_Blocks.geojson', 'r'))

# print(len(gj['features']))

features = list(sorted(gj['features'], key=lambda f: f['properties']['GEOID20']))

op_assign = {}
op_json = json.load(open('./nyc2022.json', 'r'))
for idx, f in enumerate(features):
	# print(f['properties']['GEOID20'])
	# print(idx)
	op_assign[str(idx)] = assigned[f['properties']['GEOID20']]
op_json["plans"][0]["plan"]["assignment"] = op_assign
open('./nyc2022-output.json', 'w').write(json.dumps(op_json)) # indent = 2
