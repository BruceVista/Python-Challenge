woord = input("Vul een woord in: ")
check = woord[::-1]
if woord == check: 
    print("Woord is een palindroom")
else:
    print("Geen palindroom")