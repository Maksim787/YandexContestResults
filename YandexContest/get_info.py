import pandas as pd


def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    df = pd.read_csv("all.csv")
    df["DZ_total"] = 0.05 * sum([df["DZ_" + str(i)] for i in range(1, 9)]) / 10
    df["KR_total"] = 0.1 * sum([df["KR_" + str(i)] for i in range(1, 5)]) / 5
    df["Total"] = df["DZ_total"] + df["KR_total"]
    df["Mark"] = df["Total"] / (0.05 * 8 + 0.1 * 4)

    df = df.sort_values(by="Total", ascending=False)
    df.index = pd.Series(range(1, df.shape[0] + 1))
    for col in df.columns:
        if max(df[col]) == 0:
            del df[col]
    df.to_csv("results.csv")
    return df


if __name__ == "__main__":
    main()
