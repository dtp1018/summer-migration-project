import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from uploadingcsvfile import new_dataset
from cleaningdata2 import new_excluded_dataset

fig, ax = plt.subplots(figsize=(10, 6))
species_list = new_excluded_dataset['SCIENTIFIC_NAME'].unique()

for species in species_list:
    species_data = new_excluded_dataset[new_excluded_dataset['SCIENTIFIC_NAME'] == species]
    ax.scatter(species_data['CRUISE6'],species_data['EXPCATCHNUM'],label=species)
    if len(species_data) > 1:
        x = np.sort(species_data['CRUISE6'])
        log_x = np.log(x)
        slope, intercept = np.polyfit(log_x, species_data.sort_values('CRUISE6')['EXPCATCHNUM'], 1)
        y = slope * np.log(x) + intercept
        ax.plot(x, y, linewidth=2)

ax.set_xlabel("Year")
ax.set_ylabel("Population")
ax.set_title("Populations over Time")
ax.legend(title="Species", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.savefig("ScatterplotLog")
plt.show()