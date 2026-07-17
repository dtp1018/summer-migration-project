import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

combined = pd.read_csv("combined_data.csv")
combined["YEAR"] = combined["CRUISE6"].astype(str).str[:4]
season_colors = {"Spring": "green", "Summer": "orange", "Fall": "red", "Winter": "blue"}
species_list = sorted(combined["SCIENTIFIC_NAME"].unique())
for species in species_list:
    species_data = combined[combined["SCIENTIFIC_NAME"] == species]
    plt.figure(figsize=(16,8))
    sns.scatterplot(data=species_data, x="YEAR", y="STATION", hue="Season", palette=season_colors, s=120)
    plt.title(species)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()