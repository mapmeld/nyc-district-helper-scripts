import json

op = open('nyc_popdemo_blocks20.csv', 'w')

gj = json.load(open('./nyc-centers.geojson', 'r'))
op.write('GEOID,LAT,LNG\n')
for ctr in gj['features']:
    op.write(str(ctr['properties']['GEOINDEX']) + ','
    + str(ctr['geometry']['coordinates'][1]) + ','
    + str(ctr['geometry']['coordinates'][0]) + '\n')
