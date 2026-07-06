import pandas as pd
import matplotlib.pyplot as plt


dataset1 = pd.read_csv(r"C:\Users\Dasha\OneDrive - USNH\Desktop\samplesetdata.csv")
new_dataset = dataset1.dropna()
new_dataset.to_csv('sampleset.csv')