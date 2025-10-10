
def begruessung ():
    print("Hallo,willkomen in der Welt der funktionen!Viel Spass")

begruessung()

def begruessung_name(name):
       
     print(f"Hallo {name}.Ich hoffe,es geht dir gut.")

begruessung()
begruessung_name("Aurel")
begruessung_name("Elian")

def summe (a,b):
     return a+b
print(summe(3,5))

def begruessung (name):
     return f"Hallo {name},ich hoffe es geht dir gut!"
print(begruessung("valmire"))

def summe(a,b):
     return a*b
print(summe(10,21))

def begruessung(name):
     return f"Hallo {name},bitte vergiss nicht dass du Heute ein Termin hast!"
print(begruessung("Samir"))

def projektet (name):
     return f"Pershendetje projektet {name} do te eksportohen sonte rreth ora 20:00 !"
print(projektet("CS dhe DIGO"))

def pijet(name):
     return f"Pijet qe i kerkuat {name} do ti sjellim pas pak"
print (pijet("Cola,IceTea"))

def summe (a,b):
     return a-b
print (summe(451.8,255.4))

def pruefe_alter (alter):
     if alter >=40:
          return"Du bist zu Alt."
     else:
          return"Du bist noch minderjährig."
print(pruefe_alter(33))

def pruefe_temperatur(temperatur):
     if temperatur>=39.9:
          return"Du hast Temperatur"
     else:
          return"du hast keine Temperatur"
print(pruefe_temperatur(36.7))

def mesazh_motivues():
     return"""Mos u dorezo! Edhe pse jeta shpesh te ve para dyerve te mbyllura forte,vazhdo e hec sepse ka shume dyer qe luten qe ti te trokasesh ne to."""
print(mesazh_motivues())


def pershendetje(emra_dhe_mosha):
     for emri,mosha in emra_dhe_mosha:
      print(f"Hej❤ {emri},ti tani je {mosha}. Me kujtohet sikur dje kur linde ti👶,je nje diell qe vazhdimisht ngroh zemren time🌞 ")
     
     persona=[("Aurel",9),("Elian",4)]
     pershendetje(persona)
