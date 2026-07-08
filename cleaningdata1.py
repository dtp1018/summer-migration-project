import pandas as pd
from uploadingcsvfile import new_dataset


min_value = new_dataset['EXPCATCHNUM'].min()
max_value = new_dataset['EXPCATCHNUM'].max()
max_location = new_dataset['EXPCATCHNUM'].idxmax()
print(min_value, max_value, max_location)

excluded_dataset = new_dataset[new_dataset['EXPCATCHNUM'] != 168036.0]
excluded_dataset = excluded_dataset[excluded_dataset['EXPCATCHNUM'] != 153128.0]
excluded_dataset = excluded_dataset[excluded_dataset['EXPCATCHNUM'] != 99693.0]
excluded_dataset = excluded_dataset[excluded_dataset['EXPCATCHNUM'] != 77473.0]
excluded_dataset = excluded_dataset[excluded_dataset['EXPCATCHNUM'] != 64968.0]
excluded_dataset.to_csv('outlier_sampleset.csv')

excluded_min_value = excluded_dataset['EXPCATCHNUM'].min()
excluded_max_value = excluded_dataset['EXPCATCHNUM'].max()
excluded_max_location = excluded_dataset['EXPCATCHNUM'].idxmax()
print(excluded_min_value, excluded_max_value, excluded_max_location)