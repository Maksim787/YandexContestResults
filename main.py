import parse_files
import merge_files
import get_info

parse_files.main()
merge_files.main()
df = get_info.main()
for col in df.columns:
    if max(df[col]) == 0:
        del df[col]
print(df)
print("-" * 150)

df_sorted = df.copy()
df_sorted["Sort_factor"] = (df["KR_total"] + 0.3) / df["DZ_total"]
df_sorted = df_sorted.sort_values(by=["Sort_factor", "DZ_total"], ascending=[True, False])
print(df_sorted)
