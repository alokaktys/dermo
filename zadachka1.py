file = list(open("scientist.txt", "r").read().split("\n"))
#открываем файл с учеными (всеми)
file1 = list(open("scientist.txt", "r").read().split("\n"))
#открываем файл с учеными (оригинальными)
krasivi_file = []
krasivi_file1 = []
avtori = []
avtor = ""
for i in range(len(file) - 1):
    krasivi_file.append(list(map(str, file[i].split("#"))))
for i in range(len(file1) - 1):
    krasivi_file1.append(list(map(str, file1[i].split("#"))))
#приводим файлы в читабельный вид
for i in krasivi_file1:
    if i[1] == "Аллопуринол":
        avtor = i
        break
#находим оригинального автора
for i in krasivi_file:
    if i[1] == "Аллопуринол" and i!= avtor:
        avtori.append(i)
#находим подельников
print("Разработчиками Аллопуринола были такие люди:")
print(avtor[0],"-",i[2])
for i in avtori:
    print(i[0],"-",i[2])
print("Оригинальный рецепт принадлежит:",avtor[0])
#выводим ответ
file.close()
file1.close()
#закрываем файлы