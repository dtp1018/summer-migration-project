from uploadingcsvfile import new_dataset, new_dataset2, new_dataset3, new_dataset4


min_value_fall = new_dataset['EXPCATCHNUM'].min()
max_value_fall = new_dataset['EXPCATCHNUM'].max()
max_location_fall = new_dataset['EXPCATCHNUM'].idxmax()
print(f"Min Fall: {min_value_fall} | Max Fall: {max_value_fall} | Max Fall Location: {max_location_fall}")

fall_excluded_dataset = new_dataset[new_dataset['EXPCATCHNUM'] != 168036.0]
fall_excluded_dataset = fall_excluded_dataset[fall_excluded_dataset['EXPCATCHNUM'] != 153128.0]
fall_excluded_dataset = fall_excluded_dataset[fall_excluded_dataset['EXPCATCHNUM'] != 99693.0]
fall_excluded_dataset = fall_excluded_dataset[fall_excluded_dataset['EXPCATCHNUM'] != 77473.0]
fall_excluded_dataset = fall_excluded_dataset[fall_excluded_dataset['EXPCATCHNUM'] != 64968.0]
fall_excluded_dataset.to_csv('fall_excluded_sampleset.csv')

excluded_min_value_fall = fall_excluded_dataset['EXPCATCHNUM'].min()
excluded_max_value_fall = fall_excluded_dataset['EXPCATCHNUM'].max()
excluded_max_location_fall = fall_excluded_dataset['EXPCATCHNUM'].idxmax()
print(f"New Min Fall: {excluded_min_value_fall} | New Max Fall: {excluded_max_value_fall} | New Max Fall Location: {excluded_max_location_fall}")

min_value_winter = new_dataset2[' "EXPCATCHNUM"'].min()
max_value_winter = new_dataset2[' "EXPCATCHNUM"'].max()
max_location_winter = new_dataset2[' "EXPCATCHNUM"'].idxmax()
print(f"Min Winter: {min_value_winter} | Max Winter: {max_value_winter} | Max Winter Location: {max_location_winter}")

min_value_summer = new_dataset3[' "EXPCATCHNUM"'].min()
max_value_summer = new_dataset3[' "EXPCATCHNUM"'].max()
max_location_summer = new_dataset3[' "EXPCATCHNUM"'].idxmax()
print(f"Min Summer: {min_value_summer} | Max Summer: {max_value_summer} | Max Summer Location: {max_location_summer}")

min_value_spring = new_dataset4['EXPCATCHNUM'].min()
max_value_spring = new_dataset4['EXPCATCHNUM'].max()
max_location_spring = new_dataset4['EXPCATCHNUM'].idxmax()
print(f"Min Spring: {min_value_spring} | Max Spring: {max_value_spring} | Max Spring Location: {max_location_spring}")