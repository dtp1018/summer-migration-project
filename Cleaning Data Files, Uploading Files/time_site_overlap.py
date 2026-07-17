from site_overlap import fall_overlapping_sites_count

fall_overlap_data = fall_overlapping_sites_count.copy()
fall_overlap_data["YEAR"] = (fall_overlap_data["CRUISE6"].astype(str).str[:4])
station_year_complete = (fall_overlap_data.groupby(["STATION", "YEAR"]).filter(lambda x: x["SCIENTIFIC_NAME"].nunique() == 8))
print(station_year_complete)
years_per_station = (station_year_complete.groupby("STATION")["YEAR"].unique())
for station, years in years_per_station.items():
    print(f"Station {station}: {sorted(years)}")
