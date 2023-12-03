def oblicz_cene_biletu(wiek):
    if wiek < 4:
        return 0  
    elif 4 <= wiek <= 18:
        return 10 
    else:
        return 20  


wiek_osoby1 = 3
wiek_osoby2 = 12
wiek_osoby3 = 25

cena_biletu_osoby1 = oblicz_cene_biletu(wiek_osoby1)
cena_biletu_osoby2 = oblicz_cene_biletu(wiek_osoby2)
cena_biletu_osoby3 = oblicz_cene_biletu(wiek_osoby3)

print(f"Cena biletu dla osoby o wieku {wiek_osoby1} lat: {cena_biletu_osoby1} zł")
print(f"Cena biletu dla osoby o wieku {wiek_osoby2} lat: {cena_biletu_osoby2} zł")
print(f"Cena biletu dla osoby o wieku {wiek_osoby3} lat: {cena_biletu_osoby3} zł")