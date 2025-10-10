
from datetime import date
# Lista e personave me datat e lindjes 
persona=[("Aurel",date(2016,5,21)),
("Elian",date(2021,5,20))]

#Marrim daten e sotme 
today=date.today()

#llogaritja e moshes 
for name,birthday in persona:
    age=today.year-birthday.year

    print(f"Hallo{name},du bist{age}Jahre alt!")