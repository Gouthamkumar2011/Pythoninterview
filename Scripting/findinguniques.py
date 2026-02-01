# import pandas as pd

# df = pd.read_csv(r"D:\G\p1.csv", encoding="cp1252")

# set_a = set(df["columnA"].dropna())
# set_b = set(df["columnB"].dropna())

# # Unique to either column (not common)
# unique_only = set_a.symmetric_difference(set_b)

# result_df = pd.DataFrame(unique_only, columns=["unique_only"])

# result_df.to_csv("unique_only.csv", index=False)

# print("Total unique (non-common) values:", len(unique_only))

import pandas as pd

df = pd.read_excel(r"D:\G\p1.xlsx")

set_a = set(df["columnA"].dropna())
set_b = set(df["columnB"].dropna())

unique_only = set_a.symmetric_difference(set_b)

result_df = pd.DataFrame(unique_only, columns=["unique_only"])
result_df.to_csv(r"D:\G\unique_only_1.csv", index=False)
print("Total unique (non-common) values:", len(unique_only), unique_only)

