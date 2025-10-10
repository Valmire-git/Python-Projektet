from datetime import date
def begruessung (name,alter):
    if alter >18:
      return f"Hallo {name},du bist immer noch Jung."
    elif alter <40:
       return f"Hallo,{name},Du bist im besten Alter."
    else:
       return f"hey{name},jedes Jahr macht dich weisser."   

def beruf_motivation (beruf):
   if beruf.lower()=="programmierer" or beruf.lower()=="Informatiker":
      return f"Bleib dran,die Welt braucht mehr kreative Köpfe wie dich"
   if beruf.lower()=="Lehrer":
      return f"Du formst die Zukunft,das ist eine riesige verantwortung."
   else:
      return f"Egal was tust du,mach es mit Leidenschaft."
   
   
def arbeits_jahre_motivation (jahre):
      if jahre <2:
         return f"DU bist noch neu,aber auf dem besten Weg,Grosses zu erreichen!"
      elif jahre >10:
          return f"Du hast schon viel Erfahrung"
      
#Eingaben vom Benutzer
name=input("Wie heisst du? ")
geburtsjahr=int(input("In welchem Jahr bist du geboren? "))
beruf=input("Was ist dein Beruf?")
arbeitsjahre=int(input("Wie viele Jahre arbeitest du schon"))

#ALter berechnen
Heute=date.today()
alter=Heute.year-geburtsjahr

#Ergebnisse anzeigen

print("\n---------------------------")
print(begruessung(name,alter))
print(beruf_motivation(beruf))
print(arbeits_jahre_motivation(arbeitsjahre))
print("---------------------------------------")

print(f"Alter: {alter},Beruf: {beruf},arbeitsjahre: {arbeitsjahre}")
print("Bleib motiviert und glaub an dich!")
