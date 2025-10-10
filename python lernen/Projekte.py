from datetime import date

def llogarit_moshen(viti_lindjes):
    sot = date.today()
    mosha = sot.year - viti_lindjes
    return mosha

def pershendetje(emri, mosha):
    if mosha < 18:
        return f"Hej {emri}, ti je ende i/e ri/e! 🧒"
    elif mosha < 40:
        return f"Pershendetje {emri}, je në moshën më të bukur! 😎"
    else:
        return f"Hallo {emri}, çdo vit të bën më të mençur! 👑"

# pyetje për përdoruesin
emri = input("Si quhesh? ")
viti = int(input("Në cilin vit ke lindur? "))
hobi = input("Cili është hobi yt i preferuar? ")

# llogarisim moshën
mosha = llogarit_moshen(viti)

# përshëndetje sipas moshës
print(pershendetje(emri, mosha))

# përdorim for loop për humor
for i in range(3):
    print(f"{i+1}. Kujto të ndjekësh pasionin tënd për {hobi}! ❤️")

print("Mos harro: çdo ditë është një mundësi e re! 🌞")



from datetime import date

def berechne_alter(geburtsjahr):
    heute=date.today()
    alter=heute.year-geburtsjahr
    return alter

def begruessung(name,alter):
    if alter <18:
        return F"Hey {name},du bist noch jung!😊"
    elif alter < 40:
        return f"hallo {name},du bist im besten Alter!😉"
    else:
        return f"Hey {name}, jedes Jahr macht dich weiser!"
    
 #Eingaben von Benutzer
    
name=input("Wie ist dein name?")
geburtsjahr=int(input("In welchem Jahr bist du geboren?"))
Profession=("Was ist dein Profession?")
arbeiten=int(input("Seit wann arbeitest du hier?"))

    #Alter berechnen
alter=berechne_alter(geburtsjahr)

    #Begruessung
print(begruessung(name,alter))

#Motivation mit Schleife
for i in range (4):
    print(f"{i+1},Du bist der Beste Man und ich Liebe dich❤")
   
print("Denk daran: Jeden Tag ist eine neue Chance😘")
