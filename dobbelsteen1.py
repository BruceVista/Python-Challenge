import random

aantal = int(input("Hoeveel dobbelstenen wil je rollen: "))
print("Rollen...")
totaal = 0
for x in range(aantal):
   dobbelsteen = random.randint(1, 6)
   print(dobbelsteen)  
   totaal = totaal + dobbelsteen
print("Totaal is: ", + totaal)
   