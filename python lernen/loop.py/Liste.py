#Liste.py

from datetime import date as Date

#---Eingabe von Namen (getrennt mit Komma)---
print("[A]Hapa bllokun e pyetjes")
eingabe=input("Schreibe die Namen,getrennt mit Komma:")

#---Namen in eine Liste umwandeln---
print("[B] Hapa bllokun e emrave")
namen=eingabe.split(",")

#---Schleife über die Liste---
print("[C]Hapa bllokun e ndarjeve") 
for name in namen:
    print("Hallo",name.strip(),"! Ich hoffe, es geht dir gut")

 #---DItelindjet---
print("[D]Hapa bllokun e ditelindjeve") 

from datetime import date

persona=[("Aurel",date(2016,5,21)),("Elian",date(2021,5,20))]
    
today=date.today()
for name,birthday in persona:
        age=today.year-birthday.year
        if(today.month,today.day)<(birthday.month,birthday.day):
            age-=1
            print(f"Hallo{name},du bist{age}Jahre alt!")