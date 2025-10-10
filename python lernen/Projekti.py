from datetime import date

def begruessung(name, alter):
    if alter < 18:
        return f"Hallo {name}! Du bist noch jung, genieß dein Leben! 🌸"
    elif alter < 40:
        return f"Hallo {name}! Du bist im besten Alter! 💪"
    else:
        return f"Hey {name}, jedes Jahr macht dich weiser. 🌟"

def beruf_motivation(beruf):
    if beruf.lower() == "programmierer" or beruf.lower() == "informatiker":
        return "Bleib dran, die Welt braucht mehr kreative Köpfe wie dich! 💻"
    elif beruf.lower() == "lehrer":
        return "Du formst die Zukunft, das ist eine riesige Verantwortung! 🍎"
    elif beruf.lower() == "ärztin" or beruf.lower() == "arzt":
        return "Du rettest Leben – was gibt es Wichtigeres? ❤️"
    elif beruf.lower() == "student":
        return "Halte durch! Dein Einsatz wird sich bald lohnen. 📚"
    else:
        return "Egal was du tust, mach es mit Leidenschaft! ✨"

def arbeits_jahre_motivation(jahre):
    if jahre < 3:
        return "Du bist noch neu, aber auf dem besten Weg, Großes zu erreichen! 🚀"
    elif jahre < 10:
        return "Wow! Du hast schon viel Erfahrung gesammelt. Weiter so! 🌱"
    else:
        return "Du bist ein Profi in deinem Bereich! Respekt für deine Ausdauer! 🏆"

# Eingaben vom Benutzer
name = input("Wie heißt du? ")
geburtsjahr = int(input("In welchem Jahr bist du geboren? "))
beruf = input("Was ist dein Beruf? ")
arbeitsjahre = int(input("Wie viele Jahre arbeitest du schon? "))

# Alter berechnen
heute = date.today()
alter = heute.year - geburtsjahr

# Ergebnisse anzeigen
print("\n----------------------------------")
print(begruessung(name, alter))
print(beruf_motivation(beruf))
print(arbeits_jahre_motivation(arbeitsjahre))
print("----------------------------------")
print(f"Alter: {alter} Jahre, Beruf: {beruf}, Arbeitsjahre: {arbeitsjahre}")
print("Bleib motiviert und glaub an dich! 💫")



