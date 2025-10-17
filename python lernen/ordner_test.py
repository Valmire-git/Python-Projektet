from pathlib import Path

#Rruga ku do ta krijojme nje dosje (desktop)
pfad=Path.home()/"Desktop"/"Python_Test"

#Nese nuk egziston,krijohet automatikisht

pfad.mkdir(exist_ok=True)
print("Dosja u krijua me sukses:",pfad)

#Krijo file brenda tyre 

for i in range (1,6):
    file_path=pfad/f"dokumente_{i}.txt"
    file_path.write_text(f"Kjo eshte skedari numer {i}.")
    print(f"krijova:{file_path.name}")

print("U krijuan 5 dokumente me sukses✔")