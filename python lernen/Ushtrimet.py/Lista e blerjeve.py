# Lista e blerjeve 🛒
# Krijuar nga Valmire 😊

import os

file_name = "lista.txt"  # emri i file-it ku do ruajmë produktet

# Nëse ekziston file, e lexon dhe e mbush listën ekzistuese
shopping_list = []
if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        shopping_list = [line.strip() for line in f.readlines()]
        print("📂 Lista ekzistuese u ringarkua nga file.")

while True:
    print("\n--- MENU ---")
    print("1️⃣  Shto një produkt")
    print("2️⃣  Fshi një produkt")
    print("3️⃣  Shfaq listën")
    print("4️⃣  Ruaj & Dil")

    zgjedhja = input("\nZgjedh një opsion (1-4): ")

    if zgjedhja == "1":
        produkt = input("Shkruaj emrin e produktit që dëshiron të shtosh: ")
        shopping_list.append(produkt)
        print(f"✅ '{produkt}' u shtua në listë!")

    elif zgjedhja == "2":
        produkt = input("Shkruaj emrin e produktit që dëshiron të fshish: ")
        if produkt in shopping_list:
            shopping_list.remove(produkt)
            print(f"❌ '{produkt}' u fshi nga lista.")
        else:
            print("⚠️ Ky produkt nuk ndodhet në listë!")

    elif zgjedhja == "3":
        print("\n🛍️ Lista aktuale e blerjeve:")
        if len(shopping_list) == 0:
            print("Lista është bosh!")
        else:
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

    elif zgjedhja == "4":
        with open(file_name, "w", encoding="utf-8") as f:
            for produkt in shopping_list:
                f.write(produkt + "\n")
        print(f"💾 Lista u ruajt me sukses në '{file_name}'! 👋")
        break

    else:
        print("❗ Zgjedhje e pavlefshme, provo përsëri!")
