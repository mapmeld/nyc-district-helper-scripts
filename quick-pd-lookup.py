import pandas as pd

nyc_fieldnames = [
	'LF_20_AfAm',
	'LF_20_Asian',
	'LF_20_Hispanic_or_Latino',
	'CVAP_15-19_Total',
	'CVAP_15-19_Black or African American Alone',
	'CVAP_15-19_Asian Alone',
	'CVAP_15-19_Hispanic or Latino',
]

nyc_df = pd.read_csv("./nyc-data.csv", names=nyc_fieldnames)

geoindexes = [3, 5]

# print(df.loc[geoindexes])
# print(df.loc[geoindexes, fieldnames])
print(nyc_df.loc[geoindexes, nyc_fieldnames].sum(axis=0))
print(nyc_df.loc[geoindexes, nyc_fieldnames].sum(axis=0).to_json())
