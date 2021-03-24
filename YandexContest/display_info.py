import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("all.csv")
df["Total"] = 0.05 * sum([df["DZ_" + str(i)] for i in range(1, 9)]) / 10 + 0.1 * sum([df["KR_" + str(i)] for i in range(1, 5)]) / 5
df["Percent"] = df["Total"] / (0.05 * 10 * 8 + 0.1 * 10 * 4)

df = df.sort_values(by=["Total"], ascending=False)
df["Place"] = list(range(1, df.shape[0] + 1))
print(df)
