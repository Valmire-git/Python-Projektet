# Lista e blerjeve 🛒
# Krijuar nga Valmire 😊

shopping_list = []  # lista bosh ku do ruajmë produktet

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
        print("👋 Ruajta listën dhe po dal...")
        break

    else:
        print("❗ Zgjedhje e pavlefshme, provo përsëri!")
