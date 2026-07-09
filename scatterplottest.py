import matplotlib.pyplot as plt
from uploadingcsvfile import new_dataset
from cleaningdata2 import new_excluded_dataset
import pandas as pd
import numpy as np

ax = new_excluded_dataset.plot(kind = 'scatter', x = 'CRUISE6', y = 'EXPCATCHNUM', c = 'SCIENTIFIC_NAME')
slope, intercept = np.polyfit(new_excluded_dataset['CRUISE6'], new_excluded_dataset['EXPCATCHNUM'], 1)
trend_y = slope * new_excluded_dataset['CRUISE6'] + intercept
ax.plot(new_excluded_dataset['CRUISE6'], trend_y, color='red', linestyle='--', label='Trend Line')

plt.savefig("ScatterplotNewExcludedAttempt")
#plt.show()

#minidata = pd.DataFrame(excluded_dataset)
#for name, group in minidata.groupby("SCIENTIFIC_NAME"):
#    ax.plot(group["CRUISE6"], group["EXPCATCHNUM"], label=name)

plt.show()
