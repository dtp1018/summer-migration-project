import pandas as pd
from cleaningdata1 import excluded_dataset, new_dataset

site_counts = (new_dataset.groupby(["SCIENTIFIC_NAME", "STATION"]).size().reset_index(name='count').sort_values(by=["SCIENTIFIC_NAME", "STATION"], ascending=[True, False]))
#site_counts = new_dataset["STATION"].value_counts()

#print(site_counts)
site_counts.to_csv('sitecounts')

total_species = 8
overlapping_sites_count = (new_dataset.groupby('STATION').filter(lambda x: x['SCIENTIFIC_NAME'].nunique() == total_species))
overlapping_sites_list = overlapping_sites_count['STATION'].unique().tolist()
#print(overlapping_sites_list)
#print(overlapping_sites_count)
#overlapping_sites_list.to_csv('overlappingsiteslist')
overlapping_sites_count.to_csv('overlappingsitesmoredetail')
