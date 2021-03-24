import parse_files
import merge_files
import get_info

parse_files.main()
merge_files.main()
df = get_info.main()
print(df)

# print("-" * 150)
# df_sorted = df.copy()
# df_sorted["Sort_factor"] = -df["DZ_total"] + df["KR_total"]
# df_sorted = df_sorted.sort_values(by="Sort_factor")
# print(df_sorted)
