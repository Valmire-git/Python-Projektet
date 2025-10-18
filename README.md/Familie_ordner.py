import os

main_folder = "Family_ordner"

Family_info = { "Samiri": r"Puna: Stadtbüro Baden\nHobi: Peshkimi, Futbolli\nData lindjes: 11.09.88",
               "Valmire" : r"Puna: Digitalisierung und IT,Spreitenbach\nHobi: Muzika,Vrapimi \nData lindjen 13.12.91",
               "Aurel" : r"SHkolla: Primarschule\nHobi: Futbolli,Muzika\nData lindjes :21.05.16",
               "Elian": r"Kindergarten \nHobi: Te luaj me makina dhe Lego\nData lindjes : 20.05.21"}
 
if not os.path.exists(main_folder):
    os.mkdir(main_folder)
    print(f"Krijova ordnerin: {main_folder}")
else:
    print(f"Ordneri '{main_folder}' ekziston tashme.")

for member, info in Family_info.items():
    path = os.path.join(main_folder,member)
    if not os.path.exists(path):
        os.mkdir(path)
        print (f"Krijova ordner: {path}")
    else:
        print(f"Ordneri: '{member}' ekziston tashme")

file_path = os.path.join (path,"info.txt")
with open(file_path, "w", encoding="utf-8") as f:
             f.write(f"Kjo eshte dosja ime personale e {member}. \n\n")
print (f"Shtova file:{file_path}")