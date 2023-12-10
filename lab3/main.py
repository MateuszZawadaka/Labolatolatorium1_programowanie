# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



#zad1
#listaImion=["Kasia", "Mateusz", "Adam", "Lucjan"]

#sorted_list = sorted(listaImion)


#print(sorted_list)

#b
#sorted_list.append("Mateusz")
#sorted_list.append("Kasia")

#ostatnie_imie=sorted_list.pop()

#c
#sorted_list.insert(3, "Tomasz")
#print(sorted_list)

#rev = sorted_list.reverse()
#print(sorted_list *2)

#Zad2
# print("podaj imie: ")
# imie = input()
# print("Witaj: ", imie)
# print("podaj wiek: ")
# wiek = input()
# print("Twoj wiek to: ", wiek)

# print("Podaj nazwisko: ")
# nazwisko=input()
# print("inicjaly: ", imie[0], nazwisko[0])

# print("podaj jakis tekst: ")
# text=input()
# print(text * 5)
# print("Podaj drugi tekst: ")
# text2=input()
# text3= text + text2
# print(text3)
# lista={"jojka": 10, "kukakula": 5, "stek": 43}
# print(lista)
# suma = sum(lista.values())
# print(suma)

rachunki={"wrzesien": 50, "pazdziernik": 65, "listopad": 53, "grudzien": 85}
print(rachunki)

print(sum(rachunki.values()))
print(max(rachunki.values()))
print(min(rachunki.values()))
avg=(sum(rachunki.values())/ len(rachunki))

last = rachunki["grudzien"]

if last > avg:
    print("Zacznij oszczedzać")
else:
    print("jest ok")
