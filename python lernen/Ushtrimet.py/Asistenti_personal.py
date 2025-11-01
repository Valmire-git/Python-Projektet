import os
# import time  # (opsionale, nëse do një pauzë të vogël)

def lista_blerjeve():
    print("\n🛒 Lista e blerjeve")
    # ... logjika jote ...
    input("\nShtyp Enter për t'u kthyer në menu...")

def kalkulator():
    print("\n🧮 Kalkulator")
    a = float(input("Numri 1: "))
    op = input("Operacioni (+,-,*,/): ")
    b = float(input("Numri 2: "))
    if op == "+": print("Rezultati:", a+b)
    elif op == "-": print("Rezultati:", a-b)
    elif op == "*": print("Rezultati:", a*b)
    elif op == "/": print("Rezultati:", a/b)
    else: print("⚠️ Operacion i pavlefshëm!")
    input("\nShtyp Enter për t'u kthyer në menu...")

def shfaq_dosjen():
    print("\n📂 Dosja familjare")
    folder = "Family_Ordner"
    if os.path.isdir(folder):
        for name in os.listdir(folder):
            print("•", name)
    else:
        print("❌ 'Family_Ordner' nuk u gjet.")
    input("\nShtyp Enter për t'u kthyer në menu...")

def menu():
    while True:
        print("\n--- MENU KRYESORE ---")
        print("[1] Lista e blerjeve")
        print("[2] Kalkulator")
        print("[3] Shfaq dosjen familjare")
        print("[4] Dil nga programi")
        zgjedhja = input("Zgjidh një opsion: ").strip()

        if zgjedhja == "1":
            lista_blerjeve()
        elif zgjedhja == "2":
            kalkulator()
        elif zgjedhja == "3":
            shfaq_dosjen()
        elif zgjedhja == "4":
            print("👋 Mirupafshim, Valmire!")
            break                    # DIL nga while True
        else:
            print("⚠️ Zgjedhje e pavlefshme!")
        # time.sleep(0.2)  # (opsionale)

if __name__ == "__main__":
    menu()   # ❗ Thirre vetëm një herë, mos e thirr nga funksionet tjera

