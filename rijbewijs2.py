from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age  

year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))
leeftijd = age(date(year , month , day))
print(leeftijd)

if leeftijd == 17:
    print("Alleen theorie examen")
if leeftijd == 18 or leeftijd == 19:
    print("A1 bewijs")
if leeftijd >= 20:
    print("A1 en A2 bewijs")  
if leeftijd < 17:
    print("Niet oud genoeg voor iets")