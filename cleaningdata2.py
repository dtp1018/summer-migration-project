from siteoverlap import overlapping_sites_list
import pandas as pd
from cleaningdata1 import excluded_dataset

new_excluded_dataset = excluded_dataset[excluded_dataset['STATION'].isin(overlapping_sites_list)]
new_excluded_dataset.to_csv('newexcludedset')
