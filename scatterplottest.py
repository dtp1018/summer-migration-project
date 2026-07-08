import matplotlib.pyplot as plt
from uploadingcsvfile import new_dataset
from cleaningdata1 import excluded_dataset
import pandas as pd

excluded_dataset.plot(kind = 'scatter', x = 'CRUISE6', y = 'EXPCATCHNUM', c = 'SCIENTIFIC_NAME')
plt.savefig("ScatterplotExcludedAttempt")
#plt.show()

#minidata = pd.DataFrame(excluded_dataset)
#for name, group in minidata.groupby("SCIENTIFIC_NAME"):
#    ax.plot(group["CRUISE6"], group["EXPCATCHNUM"], label=name)

plt.show()
