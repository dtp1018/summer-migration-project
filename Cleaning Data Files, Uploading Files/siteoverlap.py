from cleaningdata1 import fall_excluded_dataset, new_dataset2, new_dataset3, new_dataset4
print(new_dataset3.columns.tolist())
fall_site_counts = (fall_excluded_dataset.groupby(["SCIENTIFIC_NAME", "STATION"]).size().reset_index(name='count').sort_values(by=["SCIENTIFIC_NAME", "STATION"], ascending=[True, False]))

fall_site_counts.to_csv('fall_site_counts')

fall_total_species = 8
fall_overlapping_sites_count = (fall_excluded_dataset.groupby('STATION').filter(lambda x: x['SCIENTIFIC_NAME'].nunique() == fall_total_species))
fall_overlapping_sites_list = fall_overlapping_sites_count['STATION'].unique().tolist()
print(f"Fall Overlapping Sites: {fall_overlapping_sites_list}")

fall_overlapping_sites_count.to_csv('fall_overlapping_sites_detail')


winter_site_counts = (new_dataset2.groupby([' "SCIENTIFIC_NAME"', ' "STATION"']).size().reset_index(name='count').sort_values(by=[' "SCIENTIFIC_NAME"', ' "STATION"'], ascending=[True, False]))

winter_site_counts.to_csv('winter_site_counts')

winter_total_species = 8
winter_overlapping_sites_count = (new_dataset2.groupby(' "STATION"').filter(lambda x: x[' "SCIENTIFIC_NAME"'].nunique() == winter_total_species))
winter_overlapping_sites_list = winter_overlapping_sites_count[' "STATION"'].unique().tolist()
print(f"Winter Overlapping Sites: {winter_overlapping_sites_list}")

winter_overlapping_sites_count.to_csv('winter_overlapping_sites_detail')


summer_site_counts = (new_dataset3.groupby([' "SCIENTIFIC_NAME"', ' "STATION"']).size().reset_index(name='count').sort_values(by=[' "SCIENTIFIC_NAME"', ' "STATION"'], ascending=[True, False]))

summer_site_counts.to_csv('summer_site_counts')

summer_total_species = 7
summer_overlapping_sites_count = (new_dataset3.groupby(' "STATION"').filter(lambda x: x[' "SCIENTIFIC_NAME"'].nunique() == summer_total_species))
summer_overlapping_sites_list = summer_overlapping_sites_count[' "STATION"'].unique().tolist()
print(f"Summer Overlapping Sites: {summer_overlapping_sites_list}")

summer_overlapping_sites_count.to_csv('summer_overlapping_sites_detail')


spring_site_counts = (new_dataset4.groupby(["SCIENTIFIC_NAME", "STATION"]).size().reset_index(name='count').sort_values(by=["SCIENTIFIC_NAME", "STATION"], ascending=[True, False]))

spring_site_counts.to_csv('spring_site_counts')

spring_total_species = 8
spring_overlapping_sites_count = (new_dataset4.groupby('STATION').filter(lambda x: x['SCIENTIFIC_NAME'].nunique() == spring_total_species))
spring_overlapping_sites_list = spring_overlapping_sites_count['STATION'].unique().tolist()
print(f"Spring Overlapping Sites: {spring_overlapping_sites_list}")

spring_overlapping_sites_count.to_csv('spring_overlapping_sites_detail')
