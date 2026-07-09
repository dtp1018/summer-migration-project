import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from uploadingcsvfile import new_dataset
from cleaningdata2 import new_excluded_dataset


station_data = new_excluded_dataset[new_excluded_dataset['STATION'] == 329]

species_list = station_data['SCIENTIFIC_NAME'].unique()
fig, axes = plt.subplots(2, 4, figsize=(18, 10), sharex=True, sharey=True)
axes = axes.flatten()

for ax, species in zip(axes, species_list):
    species_data = (station_data[station_data['SCIENTIFIC_NAME'] == species].sort_values('CRUISE6'))
    x = species_data['CRUISE6']
    y = species_data['EXPCATCHNUM']
    ax.scatter(x, y)
    if len(species_data) >= 2:
        slope, intercept = np.polyfit(x, y, 1)
        trend = slope * x + intercept
        ax.plot(x, trend, color='red', linewidth=2)

    if len(species_data) >= 2:
        ax.set_title(f"{species}\nSlope = {slope:.2f}", fontsize=10)
    else:
        ax.set_title(species, fontsize=10)
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")

for ax in axes[len(species_list):]:
    fig.delaxes(ax)

fig.suptitle("Population Trends by Species", fontsize=16)

plt.tight_layout()
plt.savefig("Site329PlotPlaiceAbundance.png", dpi=300)
plt.show()