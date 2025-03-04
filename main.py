import pandas as pd

# Read the CSV file
df = pd.read_csv('sample_data.csv', sep=';', header=None, skiprows=1)

# Set column names
df.columns = ["Category", "2024", "4_kvartal_2024"]

#invert the way the dataset is siplayed
df_pivot = df.set_index("Category").T

df_pivot.loc["2024", "Døde"] = "99999"

# Print out the Døde column
print(df_pivot["Døde"])
