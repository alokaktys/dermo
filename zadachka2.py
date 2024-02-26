file = list(open("scientist.txt", "r").read().split("\n"))
#открываем файл с учеными (всеми)
dati1 = []
krasivi_file = []
for i in range(len(file) - 1):
    krasivi_file.append(list(map(str, file[i].split("#"))))
#приводим файл в читабельный вид
for i in krasivi_file:
    dati1.append(i[2])
dati1 = sorted(dati1)
otsort = []
for i in dati1:
    for j in krasivi_file:
        if i in j:
            otsort.append(j)
            break
print(otsort)
#сортируем файл по дате
for i in range(5):
    print(otsort[i][0]+":",otsort[i][1])
file.close()
#закрываем файл