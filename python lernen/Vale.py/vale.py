from datetime import date 


def pershendetje (emri,mosha):
    if mosha <18:
        return (f"Pershendetje {emri}, Ti je shume e re!")
    elif mosha >30:
        return (f"Pershendetje {emri}, Ti je ne moshen me te mire!")
    else:
        return (f"Hey {emri}, Qdo vit te ben me te menqur")
    

def motivi_per_profesion (profesioni):
    p=profesioni.lower()
    if p in ("Programues","IT"):
       return ("Qendro,Bota ka nevoje per njerz kreativ")
    elif p =="Mesues":
       return ("Ardhmeria e botes qendron ne duart e ketij profesioni")
    else: 
        return ("Qfardo qe ti ben.Ti Je shume i forte")
    
def pervoja_punes (pervoja):
    if pervoja <2:
        return ("Ti je e re,por me rrugen me te mire per te mesuar")
    elif pervoja <10:
        return ("Wow ti ke mjaftueshm pervoje.Ne duam te mesojme nga ti")   
    else:
        return ("Super eksperience") 
#Inputet 
   
emri=input("Si quhesh?")
viti_lindjes=int(input("Ne cilin vit ke lindur?"))
profesioni=input("qfar profesioni ke? ")
vite_pervoje=int(input("Sa vite pervoje pune ke?"))

#Data ime
today=date.today()
mosha=today.year-viti_lindjes

#Fundi

print(pershendetje(emri,mosha))
print(pervoja_punes(vite_pervoje))
print(motivi_per_profesion(profesioni)) 

#Motivi
   
print(f"Mosha: {mosha} vite, Profesioni: {profesioni} ,Pervoja: {vite_pervoje}vite")
print("❤Qendro keshtu si je,je rruges se duhur ❤")






