import random

print("\n 🎯 Loja GJEJ NUMRIN - Versioni Super Pro!")
print("kam zgjedhur nje numer nga 1 deri ne 50! a mund ta gjesh cili eshte numri ?\n")

#🎲 Numri Sekret
sekreti = random.randint (1,50)
tentimet=0

#🎮 Loja Fillon Tani.

while True:
  tentativa = int (input("Shkruaj nje numer :"))
  tentimet +=1
  diferenca =abs(sekreti - tentativa)

  if tentativa < sekreti:
   print("Numri eshte me i madh se")
  elif tentativa > sekreti:
   print("Numri qe kerkon eshte me i vogel")
  else:
   print(f"\n 🎉 Sakte! Numri ishte {sekreti}.")
  if tentimet <= 3:
      print("Ti je gjeniale 🏆")
  elif tentimet <= 7:
   print("👏Bravo je shume afer nivelit gjenialitetit")
  else:
    print("😊Ti e gjete,ska rendesi sa ke provuar,rendesi ka qe e gjete ")
    break
  
  #Komente per afersin 
  if diferenca <= 2:
    print("🌂 Ti je shume afer ☀\n")
  elif diferenca <= 5:
    print("☂ Ti je afer,por kerko ende 🌦\n")
  else:
    print("☔Je Larg, provo perseri..🌨\n")