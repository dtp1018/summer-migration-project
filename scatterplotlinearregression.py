import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from uploadingcsvfile import new_dataset
from cleaningdata2 import new_excluded_dataset

fig, ax = plt.subplots(figsize=(10, 6))
species_list = new_excluded_dataset['SCIENTIFIC_NAME'].unique()

for species in species_list:
    species_data = new_excluded_dataset[new_excluded_dataset['SCIENTIFIC_NAME'] == species].sort_values('CRUISE6')
    ax.scatter(species_data['CRUISE6'],species_data['EXPCATCHNUM'],label=species)
    if len(species_data) >= 2:
        x = species_data['CRUISE6']
        y = species_data['EXPCATCHNUM']
        slope, intercept = np.polyfit(x, y, 1)
        trend = slope * x + intercept
        ax.plot(x, trend, linewidth=2)

ax.set_xlabel("Year")
ax.set_ylabel("Population")
ax.set_title("Populations over Time")
ax.legend(title="Species", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.savefig("ScatterplotLinearRegression")
plt.show()