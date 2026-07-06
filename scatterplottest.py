import matplotlib.pyplot as plt
from uploadingcsvfile import new_dataset

new_dataset.plot(kind = 'scatter', x = 'CRUISE6', y = 'EXPCATCHNUM', c = 'SCIENTIFIC_NAME')
plt.savefig("ScatterplotFirstAttempt")
plt.show()
