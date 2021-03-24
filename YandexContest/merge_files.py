from os import path


def add_file(name):
    is_kr = int(name[0:2] == "KR")
    name_type = name[0:2]
    number_start = name.index("_out_") + 5
    number_end = name.index("/", number_start)
    number = int(name[number_start:number_end])
    index = number + is_kr * 8 - 1
    with open(name + ".txt", encoding="utf-8") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        for i in range(len(lines)):
            name, score = lines[i].split(",")
            if name not in name_to_score:
                name_to_score[name] = [0] * len_info
            name_to_score[name][index] = score


def write_info(file_name):
    with open(file_name + ".csv", "w", encoding="utf-8") as file:
        print("name",
              ",".join(["DZ_" + str(i) for i in range(1, 9)]),
              ",".join(["KR_" + str(i) for i in range(1, 5)]),
              sep=",", file=file)
        for name, data in name_to_score.items():
            print(name, *data, sep=",", file=file)


len_info = 8 + 4
name_to_score = {}
for i in range(1, 9):
    for page in range(1, 30):
        name = "DZ_out/DZ_out_" + str(i) + "/" + str(page)
        if path.exists(name + ".txt"):
            add_file(name)

for i in range(1, 5):
    for page in range(1, 30):
        name = "KR_out/KR_out_" + str(i) + "/" + str(page)
        if path.exists(name + ".txt"):
            add_file(name)

write_info("all")
