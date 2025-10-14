import random

print("🎯 Loja gjej Numrin!")
print ("Kam zgjedhur nje numer nga numri 1 deri ne numrin 50. A mund ta gjesh cili eshte ky numer?")

sekreti=random.randint (1,50)
tentimet = 0

while True:
    tentativa = int(input("Shkruaj nje numer:"))
    tentimet +=1

    if tentativa < sekreti:
        print("Numri qe kerkon eshte me i madh ")
    elif tentativa > sekreti:
        print("Numri qe kerkon eshte me i vogel")
    else:
        print(f"🎉 Sakte! Numri ishte {sekreti}. E gjete per {tentimet} tentativa!")
        break