print (" Kalkulatori i thjeshte i Valmires")

numri1=float(input("SHkruaj numrin e pare:" ))
operacioni = input("zgjedh nje operacion (+,-,*,/): ")
numri2=float(input("Shkruaj numrin e dyte : "))

if operacioni == "+":
    print("Rezultati eshte:", numri1+numri2)
elif operacioni == "-":
    print("rezultati eshte:", numri1-numri2)
elif operacioni =="*":
    print("rezultati eshte:", numri1*numri2)
elif operacioni =="/":
    if numri2 !=0:
     print("rezultati eshte:",numri1/numri2)
    else:
       print("Rezultati eshte i papranueshm")
else:
   print("Operacioni i pavlefshm")

print("Valmire e vertet qe kalkulatori i thjeshte eshte me i lehte per ty,por per te mesuar me thell ndoshta me mire do ishte kalkulatori Pro.")