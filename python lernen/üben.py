# Mittagessen und Getränke

essen=input("Was willst du heute zum Mittagessen? (Fisch/Rindfleisch):")
getränk=input("Was willst du zum trinken? (Redbul/Bier):")
if essen.lower()=="fisch":
    essen_text="Fisch"
elif essen.lower()=="rind Fleisch":
    essen_text="Rind Fleisch"
else:
    essen_text="etwas anderes"

#Getränk
if getränk.lower()=="redbul":
    getränk_text="Redbul"
elif getränk.lower()=="bier":
    getränk_text="Bier"
else:
    getränk_text="etwas anderes"
    
print(f"Heute will ich",essen_text,"mit",getränk_text)