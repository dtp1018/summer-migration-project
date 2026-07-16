from site_overlap import overlapping_sites_list
from cleaning_data_outliers import fall_excluded_dataset
from uploading_csv_files import new_dataset2, new_dataset3, new_dataset4

fall_sites_excluded_dataset = fall_excluded_dataset[fall_excluded_dataset['STATION'].isin(overlapping_sites_list)]
fall_sites_excluded_dataset.to_csv('fall_sites_excluded_dataset')

winter_sites_excluded_dataset = new_dataset2[new_dataset2[' "STATION"'].isin(overlapping_sites_list)]
winter_sites_excluded_dataset.to_csv('winter_sites_excluded_dataset')

summer_sites_excluded_dataset = new_dataset3[new_dataset3['STATION'].isin(overlapping_sites_list)]
summer_sites_excluded_dataset.to_csv('summer_sites_excluded_dataset')

spring_sites_excluded_dataset = new_dataset4[new_dataset4['STATION'].isin(overlapping_sites_list)]
spring_sites_excluded_dataset.to_csv('spring_sites_excluded_dataset')
