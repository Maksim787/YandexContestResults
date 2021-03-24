import os


def parse(input_file_name, output_file_name):
    with open(input_file_name + ".txt", encoding="utf-8") as file:
        data = file.readlines()
        if not data:
            print("Need:", input_file_name)
            return
        data = list(map(lambda x: x.strip(), data))

    start = data.index("Очки") + 1
    end = data.index("СправкаОбратная связьПользовательское соглашение© 2013–2021  ООО «Яндекс»")
    data = data[start:end]

    name_index = []
    score_index = []

    for i in range(len(data)):
        if all(map(lambda x: x.isalpha() or x.isspace(), data[i])):
            name_index.append(i)
    n_names = len(name_index)
    for i in range(1, n_names):
        score_index.append(name_index[i] - 2)
    score_index.append(len(data) - 1)

    name_to_score = {}
    for i in range(n_names):
        name_to_score[data[name_index[i]]] = int(data[score_index[i]])
    with open(output_file_name + ".txt", encoding="utf-8", mode="w") as file:
        for name, score in name_to_score.items():
            print(name, score, file=file, sep=',')


for i in range(1, 9):
    for page in range(1, 30):
        name_input = "DZ/DZ_" + str(i) + "/" + str(page)
        name_output = "DZ_out/DZ_out_" + str(i)
        if os.path.exists(name_input + ".txt"):
            if not os.path.exists(name_output):
                os.makedirs(name_output)
            parse(name_input, name_output + "/" + str(page))

for i in range(1, 5):
    for page in range(1, 30):
        name_input = "KR/KR_" + str(i) + "/" + str(page)
        name_output = "KR_out/KR_out_" + str(i)
        if os.path.exists(name_input + ".txt"):
            if not os.path.exists(name_output):
                os.makedirs(name_output)
            parse(name_input, name_output + "/" + str(page))
