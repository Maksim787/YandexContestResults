import matplotlib.pyplot as plt
import pandas as pd
import set_pd_options

set_pd_options.main()


def find_kr_dz(name):
    row = df[df["name"] == name]
    return row.iloc[0]["DZ_total"], row.iloc[0]["KR_total"]


def find_kr_dz_literal(name, surname):
    for i in range(df.shape[0]):
        values = df.iloc[i]["name"].split()
        if name in values and surname in values:
            return df.iloc[i]["DZ_total"], df.iloc[i]["KR_total"]


def read_names(file_name):
    with open(file_name + ".txt", encoding='utf-8') as file:
        lines = [ln.strip() for ln in file.readlines()]
        return list(map(lambda x: x.split(), lines))


df = pd.read_csv("Data/results.csv", index_col=0)
print(df)
m_204 = read_names("Data/204")
m_202 = read_names("Data/202")

m_204_res = [find_kr_dz_literal(name, surname) for (name, surname) in m_204]
m_202_res = [find_kr_dz_literal(name, surname) for (name, surname) in m_202]

dz_total = list(df["DZ_total"])
kr_total = list(df["KR_total"])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
plt.scatter(dz_total, kr_total, alpha=0.5, label="All")
plt.scatter([x[0] for x in m_202_res], [x[1] for x in m_202_res], alpha=0.7, color="yellow", label="202",
            s=[50] * len(m_202_res))
plt.scatter([x[0] for x in m_204_res], [x[1] for x in m_204_res], alpha=0.7, color="black", label="204",
            s=[50] * len(m_202_res))
plt.xlabel("DZ_total")
plt.ylabel("KR_total")
plt.legend()
plt.show()
