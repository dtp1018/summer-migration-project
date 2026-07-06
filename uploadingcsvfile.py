import pandas as pd


def csv_upload():
    dataset1 = pd.read_csv(r"C:\Users\Dasha\OneDrive - USNH\Desktop\samplesetdata.csv")
    print(dataset1.to_string())

csv_upload()