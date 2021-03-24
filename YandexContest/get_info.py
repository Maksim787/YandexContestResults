import pandas as pd


def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    df = pd.read_csv("all.csv")
    df["DZ_total"] = 0.05 * sum([df["DZ_" + str(i)] for i in range(1, 9)]) / 10
    df["KR_total"] = 0.1 * sum([df["KR_" + str(i)] for i in range(1, 5)]) / 5

    df["DZ_total"] = df["DZ_total"].round(5)
    df["KR_total"] = df["KR_total"].round(5)

    df["Mark"] = df["DZ_total"] + df["KR_total"]
    df = df.sort_values(by="Mark", ascending=False)
    df.index = pd.Series(range(1, df.shape[0] + 1))
    df["Percentile"] = (df.index - 1) * 100 / df.shape[0]
    df["Percentile"] = df["Percentile"].round(1)
    df["Percent of done works"] = df["Mark"] / (0.05 * 8 + 0.1 * 4) * 10
    df["Percent of done works"] = df["Percent of done works"].round(5)
    for col in df.columns:
        if max(df[col]) == 0:
            del df[col]
    df.to_csv("results.csv")
    return df


if __name__ == "__main__":
    main()
