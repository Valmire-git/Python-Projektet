print("kalkulatori valmires")
num1=float(input("Shkruaj numrin e pare: "))
num2=float(input("shkruaj numrin e dyte: "))

print("Zgjidh veprimin")
print("1.Mbledhja (+)")
print("2.Zbritja (-)")
print("3.Shumezimi (*)")
print("4.Pjestimi (/)")

zgjedhja=input("zgjidh (1/2/3/4): ")

if zgjedhja =="1":
 print("Rezultati eshte:", num1+num2)
elif zgjedhja =="2":
    print("Rezultati eshte", num1-num2)
elif zgjedhja =="3":
   print("Rezultati eshte: ",num1*num2)
elif zgjedhja=="4":
   if num2 !=0:
    print("Rezultati eshte:",num1/num2)
   else:
     print("zgjedhja e pavlefshme!!!!")