from statsmodels.nonparametric.smoothers_lowess import lowess
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from uploadingcsvfile import new_dataset
from cleaningdata2 import new_excluded_dataset

species_list = new_excluded_dataset['SCIENTIFIC_NAME'].unique()
fig, axes = plt.subplots(2, 4, figsize=(18, 10), sharex=True, sharey=True)
axes = axes.flatten()

for ax, species in zip(axes, species_list):
    species_data = (new_excluded_dataset[new_excluded_dataset['SCIENTIFIC_NAME'] == species].sort_values('CRUISE6'))
    x = species_data['CRUISE6']
    y = species_data['EXPCATCHNUM']
    ax.scatter(x, y)
    if len(species_data) >= 3:
        smooth = lowess(y, x, frac=0.4)
        ax.plot(smooth[:, 0], smooth[:, 1], color='red', linewidth=2)

        ax.set_title(species, fontsize=10)
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")

for ax in axes[len(species_list):]:
    fig.delaxes(ax)

fig.suptitle("Population Trends by Species", fontsize=16)

plt.tight_layout()
plt.savefig("SpeciesScatterplotsLOWESS.png", dpi=300)
plt.show()