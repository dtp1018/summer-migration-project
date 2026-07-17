import pandas as pd

fall = pd.read_csv("fall_excluded_sampleset.csv")
fall["Season"] = "Fall"
winter = pd.read_csv("wintersampleset_fixed.csv")
winter["Season"] = "Winter"
spring = pd.read_csv("springsampleset.csv")
spring["Season"] = "Spring"
summer = pd.read_csv("summersampleset_fixed.csv")
summer["Season"] = "Summer"
combined = pd.concat([fall, winter, spring, summer], ignore_index=True)
combined.to_csv("combined_data.csv", index=False)