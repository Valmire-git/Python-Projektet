# Intervist pune 
("Pershendetje,mire se vini ne intervisten tende te pare python Basis")

emri=input("si eshte emri juaj")
mosha=int(input("sa vjec jeni?"))
eksperienca=int(input("sa vite eksperienc i keni?"))
gjuha=input("a di python?(po/jo):")

print(f"\nFaleminderirt{emri},po analizojme pergjigjet e tua")

#kushtet e intervistet

if mosha <18:
    print("je shume i ri per kete pune")
    print("Keshille: Fokusoju shkollimit tani,dhe dikur fillo perseri me aplikimet")
elif eksperienca<2:
    print("Na vjen keq por nuk ke mjaftueshm eksperienc")
    print("Keshille:Fillo me prova dhe me projekte te vogla qe te fitosh sa me shume eksperience")
elif eksperienca>2:
    print("Wow,pervoja jote eshte e shkelqyeshme mezi presim te mesojme nga ti")
elif gjuha.lower()!="po":
    print("Duhet te dish Python per kete pozite.")
    print("Keshille: fillo me ndonje kurs ku do mesosh bazat e Python")
else:
    print("Urime",emri,"Ti je pranuar per kete pune")
    print("shpresojme shume te kemi nje Team ku do ndajme ekspreincat tona e do bashkpunojme se bashku ne qdo proces")