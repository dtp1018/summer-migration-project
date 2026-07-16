import pandas as pd
import matplotlib.pyplot as plt


dataset1 = pd.read_csv(r"C:\Users\Dasha\OneDrive - USNH\Desktop\samplesetdata.csv")
new_dataset = dataset1.dropna()
new_dataset.to_csv('fallsampleset.csv')

dataset2 = pd.read_csv(r"C:\Users\Dasha\OneDrive - USNH\Desktop\wintersampledataset.csv")
new_dataset2 = dataset2.dropna()
new_dataset2.to_csv('wintersampleset.csv')

dataset3 = pd.read_csv(r"C:\Users\Dasha\OneDrive - USNH\Desktop\summersampledataset.csv")
new_dataset3 = dataset3.dropna()
new_dataset3.to_csv('summersampleset.csv')

dataset4 = pd.read_csv(r"C:\Users\Dasha\OneDrive - USNH\Desktop\springsampledataset.csv")
new_dataset4 = dataset4.dropna()
new_dataset4.to_csv('springsampleset.csv')
