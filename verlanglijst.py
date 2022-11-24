af = []
while not 'KLAAR!' in af:
  verlanglijst = input("Wat wil je op je verlanglijst: ")
  af.append(verlanglijst)
else:  
    af.remove('KLAAR!')    
    print("Jouw verlanglijst: ")
    print(sorted(af))
    