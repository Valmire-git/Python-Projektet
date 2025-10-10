# Ushtrime 1
# ---a deshrion kafe ?---
pije=(input("a deshrion kafe sot? Po/Jo:"))
if pije. lower()=="po":
   sheqer=int(input("sa luge sheqer deshiron?"))
   if sheqer =="0":
      print("kafeja jote eshte e idhet")
   else:
    print("kafeja jote eshte gati me", sheqer, "luge sheqer")
else:
 print("ska problempa kafe sot")

#---Kaffe---
 getränk=input("Willst du Kaffe heute? Ja/Nein")
 if getränk.lower()=="ja":
   zucker=int(input("wie viel Löffel Zucker mochtest du?"))
   if zucker==0:
     print("Dein Kaffe ist bitter")
   else:
     print("Dein Kaffe ist mit",zucker,"Löffeln zucker")
 else:
     print:(f"Kein Problem,heute kein Kaffe") 
     #---Essen---
     essen=input("Was willst du heute zum Mittagessen? (Pizza/Spaghetti/Reis):")
     if essen.lower()=="pizza":
       print("Dein Mittagessen ist Pizza")
     elif essen.lower()=="spaghetti":
             print("Dein Mittagessen ist Spagheti")
     elif essen.lower()=="reis":
       print("Dein Mittagessen ist Reis")
     else:
      print("Kein Problem,heute hat kein Mitagessen")