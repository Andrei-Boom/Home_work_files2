import os

files_txt = []
for file in os.listdir('/Users/andrei_i/PycharmProjects/HW_files_2/story/'):
    if file.endswith(".txt"):
        files_txt.append(os.path.join("", file))

dict_1 = {}

for file in files_txt:
    with open(f"/Users/andrei_i/PycharmProjects/HW_files_2/story/{file}", 'r') as list_1:
        context = list_1.readlines()
        dict_1[file] = len(context)

sorted_dict_1 = dict(sorted(dict_1.items(), key=lambda item: item[1]))

for file in sorted_dict_1:
    with open(f"/Users/andrei_i/PycharmProjects/HW_files_2/story/{file}", 'r') as list_1:
        dict_2 = {}
        a=0
        for line in list_1:
            a+=1
            f, ext = file.split('.')
            dict_2[f'Строка номер {a} файла {f}'] = line
        with open('4.txt', 'a') as list_5:
            list_5.write(f'\n{file}\n')
            list_5.write(f'{len(dict_2)}\n')
            for key, value in dict_2.items():
                list_5.write(f'{key}  {value}')