import numpy as np
import matplotlib.pyplot as plt

path = 'dane_1.txt.txt'

plik = [wpis.replace("\n", "").split(";") for wpis in open(path, 'r', encoding='utf-8').readlines()]

# kluby o dlugiej nazwie(do 5 liter) i dlugie (powyzej)

kluby_dlugie = []
kluby_krotkie = []

for wpis in plik:
    if len(wpis[1]) > 5:
        kluby_dlugie.append(wpis[1])
    else:
        kluby_krotkie.append(wpis[1])

ilosc_k_d = len(kluby_dlugie)
ilosc_k_k = len(kluby_krotkie)
rodzaje = [ilosc_k_d, ilosc_k_k]
kluby = ['Kluby o długiej nazwie', 'Kluby o krótkiej nazwie']
kluby = tuple(kluby)

# podzial na klubuy z miasta konczace sie na ow i pozostale

miasta = []
miasta_na_ow = []
miasta_nie_na_ow = []

for wpis in plik:
    miasta.append(wpis[2])

for miasto in miasta:

    if miasto[-1] == 'w':
        if miasto[-2] == 'o':
            miasta_na_ow.append(miasto)
    else:
        miasta_nie_na_ow.append(miasto)

ilosc_na_ow = len(miasta_na_ow)
ilosc_nie_na_ow = len(miasta_nie_na_ow)
rodzaje_2 = [ilosc_na_ow, ilosc_nie_na_ow]
kluby_2 = ['Kluby kończące się na ów', 'Kluby zakończone inaczej']
kluby_2 = tuple(kluby_2)

# wielkosc id dla kazdego z klubow

for wpis in plik:
    if wpis[0] == "Id_klubu" and wpis[1] == "Nazwa":
        id_3 = []
        kluby_3 = []
    else:
        id_3.append(wpis[0])
        kluby_3.append(wpis[1])

kluby_3 = tuple(kluby_3)

# podzial na kluby dla mlodziezy, od 18 roku i od 21 roku zycia

klub_dla_mlodziezy = []
klub_od_18 = []
klub_od_21 = []

for wpis in plik:
    if wpis[4] == 'Mlodziez':
        klub_dla_mlodziezy.append(wpis[1])
    elif wpis[4] == '18':
        klub_od_18.append(wpis[1])
    elif wpis[4] == '21':
        klub_od_21.append(wpis[1])

ilosc_kdm = len(klub_dla_mlodziezy)
ilosc_od_18 = len(klub_od_18)
ilosc_od_21 = len(klub_od_21)
rodzaje_3 = [ilosc_kdm, ilosc_od_18, ilosc_od_21]
kluby_4 = ['Kluby dla młodzieży', 'Kluby od 18 lat', 'Kluby od 21 lat']
kluby_4 = tuple(kluby_4)

#powierzchnia klubow

for wpis in plik:
    if wpis[3] == "Wielkosc":
        kluby_5 = []
        powierzchnia = []
    else:
        powierzchnia.append(int(wpis[3]))
        kluby_5.append(wpis[1])

kluby_dict = dict(zip(kluby_5, powierzchnia))
kluby_dict_sort = {k: v for k, v in sorted(kluby_dict.items(), key=lambda item: item[1])}
kluby_sort = kluby_dict_sort.keys()
powierzchnia_sort = kluby_dict_sort.values()
kluby_sort = tuple(kluby_sort)

# kluby ze srednia powierzchnia oraz ze srednim id

powierzchnia_d_M = []
powierzchnia_d_18 = []
powierzchnia_d_21 = []
id_d_M = []
id_d_18 = []
id_d_21 = []

for wpis in plik:
    if wpis[4] == 'Mlodziez':
        powierzchnia_d_M.append(int(wpis[3]))
        id_d_M.append(int(wpis[0]))
    elif wpis[4] == '18':
        powierzchnia_d_18.append(int(wpis[3]))
        id_d_18.append(int(wpis[0]))
    elif wpis[4] == '21':
        powierzchnia_d_21.append(int(wpis[3]))
        id_d_21.append(int(wpis[0]))

kluby_5 = ('Kluby dla Mlodziezy', 'Kluby dla 18', 'Kluby dla 21')


sum_1 = 0
sum_2 = 0
sum_3 = 0
print(powierzchnia_d_M)
for pow in powierzchnia_d_M:
    sum_1 += pow

for pow in powierzchnia_d_18:
    sum_2 += pow

for pow in powierzchnia_d_21:
    sum_3 += pow

sum_4 = 0
sum_5 = 0
sum_6 = 0

for id in id_d_M:
    sum_4 += id

for id in id_d_18:
    sum_5 += id

for id in id_d_21:
    sum_6 += id

srednia_pow_M = sum_1 / len(powierzchnia_d_M)
srednia_pow_18 = sum_2 / len(powierzchnia_d_18)
srednia_pow_21 = sum_3 / len(powierzchnia_d_21)
srednia_id_M = sum_4 / len(id_d_M)
srednia_id_18 = sum_5 / len(id_d_18)
srednia_id_21 = sum_6 / len(id_d_21)

srednia_id = [srednia_id_M, srednia_id_18, srednia_id_21]
srednia_powierzchnia = [srednia_pow_M, srednia_pow_18, srednia_pow_21]
position = np.arange(len(srednia_id))

# wykres 1

plt.bar(kluby, rodzaje,)
plt.title('Ilosc klubów o długiej i krótkiej nazwie', fontsize=16, color='#323232')
plt.xlabel('Kluby', fontsize=12, color='purple')
plt.ylabel('Ilość', fontsize=12, color='green')
plt.show()

# wykres 2

plt.bar(kluby_2, rodzaje_2,)
plt.title('Ilość klubów w miastach zakończonych na ów', fontsize=16, color='#323232')
plt.xlabel('Klub', fontsize=12, color='purple')
plt.ylabel('Ilość', fontsize=12, color='green')
plt.show()

# wykres 3

plt.figure(figsize=(100, 10))
plt.bar(kluby_3, id_3, color='#969696')
plt.xlabel('Klub', fontsize=12, color='#323232')
plt.ylabel('Id', fontsize=12, color='#323232')
plt.title('Liczba id dla każdego z klubów', fontsize=16, color='#323232')
plt.show()

# wykres 4

plt.bar(kluby_4, rodzaje_3)
plt.xlabel('Kluby dla', fontsize=12, color='purple')
plt.ylabel('Ilość', fontsize=12, color='red')
plt.title('Zestawienie klubów ze względu na minimalny wiek', fontsize=16, color='#323232')
plt.show()

# wykres 5

plt.figure(figsize=(100, 10))
plt.bar(kluby_sort, powierzchnia_sort, color='#969696')
plt.xlabel('Klub', fontsize=12, color='#323232')
plt.ylabel('Id', fontsize=12, color='#323232')
plt.title('Porównanie powierzchni każdego z klubów', fontsize=16, color='#323232')
plt.show()

# wykres 6

plt.figure(figsize=(100, 10))
plt.bar(position, srednia_powierzchnia, color='lightslategrey', label = 'Średnia powierzchnia klubów')
plt.bar(position, srednia_id, color='wheat', label = 'Średnia liczba id')
plt.xticks(position, kluby_5)
plt.xlabel('Kluby dla', fontsize=12, color='#323232')
plt.ylabel('Średnia', fontsize=12, color='#323232')
plt.title('Zestawienie średniej powierzchni klubów oraz ich id dla kategorii wiekowych', fontsize=16, color='#323232')
plt.legend()
plt.show()