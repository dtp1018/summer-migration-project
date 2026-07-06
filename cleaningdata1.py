import pandas as pd
from uploadingcsvfile import new_dataset


min_value = new_dataset['EXPCATCHNUM'].min()
max_value = new_dataset['EXPCATCHNUM'].max()
max_location = new_dataset['EXPCATCHNUM'].idxmax()
print(min_value, max_value, max_location)