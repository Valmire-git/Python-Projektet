# Mittagessen und Getränk
essen=input("Was willst du zum Mittagessen? (Pizza/Spaghetti):")
getränk=input("Und was willst du zum trinken? (Cola/Wasser):")

#Mittagessen
if essen.lower()=="pizza":
    essen_text="pizza"
elif essen.lower()=="spaghetti":
    essen_text="spaghetti"
else:
    essen_text="etwas anderes"
#Getränk
if getränk.lower()=="cola":
    getränk_text="cola"
elif getränk.lower()=="wasser":
    getränk_text="wasser"

else:
    getränk_text="etwas anderes"

print(f"Dein Mittagessen ist",essen_text,"mit",getränk_text)