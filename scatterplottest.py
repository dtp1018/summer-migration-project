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
        slope, intercept = np.polyfit(species_data['CRUISE6'],species_data['EXPCATCHNUM'],1)
        x = np.sort(species_data['CRUISE6'])
        y = slope * x + intercept
        ax.plot(x, y, linewidth=2)

ax.set_xlabel("Year")
ax.set_ylabel("Population")
ax.set_title("Populations over Time")
ax.legend(title="Species", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.savefig("ScatterplotTrendLines")
plt.show()

#ax = new_excluded_dataset.plot(kind = 'scatter', x = 'CRUISE6', y = 'EXPCATCHNUM', c = 'SCIENTIFIC_NAME')
#slope, intercept = np.polyfit(new_excluded_dataset['CRUISE6'], new_excluded_dataset['EXPCATCHNUM'], 1)
#trend_y = slope * new_excluded_dataset['CRUISE6'] + intercept
#ax.plot(new_excluded_dataset['CRUISE6'], trend_y, color='red', linestyle='--', label='Trend Line')

#plt.savefig("ScatterplotNewExcludedAttempt")
#plt.show()

#minidata = pd.DataFrame(excluded_dataset)
#for name, group in minidata.groupby("SCIENTIFIC_NAME"):
#    ax.plot(group["CRUISE6"], group["EXPCATCHNUM"], label=name)

#plt.show()
