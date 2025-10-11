def lexonumrin (prompt):
    while True:
        try:
            return float (input(prompt))
        except ValueError:
         print ("Shkruaj nje numer te vlefshm!")

def plus (a,b): return a+b
def minus (a,b) : return a-b
def shumezim (a,b) : return a*b
def pjestim (a,b) : 
   if b== 0:
      raise ZeroDivisionError ("pjestimi me zero nuk lejohet🔒")
   return a/b 

def llogarit (oper):
   a=lexonumrin("Numri 1:")
   b=lexonumrin("Numri 2:")
   try:
    match oper:
         case "+" : res = plus (a,b)
         case "-" : res = minus (a,b)
         case "*" : res =shumezim(a,b)
         case "/" : res =pjestim(a,b)
         case _: print("Zgjedhja e pavlefshme"); return None
    print("✔Rezultati:",res)
    return res
   except ZeroDivisionError as e:
      print("Block",e)

def main ():
   while True:
      print("\n[+|-|*|/| q=dalje]")
      zgjedhja=input("Zgjedhja:").strip()
      if zgjedhja.lower()=="q":
         print("mirupafshim:") ;break
      llogarit(zgjedhja)

if __name__ =="__ main __":
    a=lexonumrin("shkruaj numrin e pare:")
    b=lexonumrin("shkruaj numrin e dyte:")
    print("shuma:",plus(a,b))

if __name__=="__main__":
   main()
