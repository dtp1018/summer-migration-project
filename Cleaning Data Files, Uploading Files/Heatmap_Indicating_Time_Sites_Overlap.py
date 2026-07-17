import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from site_overlap import fall_overlapping_sites_count

fall_overlap_data = fall_overlapping_sites_count.copy()
fall_overlap_data["YEAR"] = fall_overlap_data["CRUISE6"].astype(str).str[:4]
species_list = sorted(fall_overlap_data["SCIENTIFIC_NAME"].unique())
for species in species_list:
    species_data = fall_overlap_data[fall_overlap_data["SCIENTIFIC_NAME"] == species]
    pivot = (species_data.assign(Present=1).pivot_table(index="STATION", columns="YEAR", values="Present", aggfunc="max", fill_value=0))
    plt.figure(figsize=(14, 8))
    sns.heatmap(pivot, cmap="Greens", cbar=False, linewidths=0.5)
    plt.title(species)
    plt.xlabel("Year")
    plt.ylabel("Station")
    plt.tight_layout()
    plt.show()
