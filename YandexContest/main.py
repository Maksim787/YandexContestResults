import parse_files
import merge_files
import get_info

parse_files.main()
merge_files.main()
df = get_info.main(save=True)
print(df)
