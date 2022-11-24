import random
chips = 10
while True:
    inzet = []
    while not "stop" in inzet and chips > 0:
        inzet.append(input("Op welke getellen wil je inzetten asl je klaar bent met inzetten type 'stop': ").lower())
        chips -= 1 
        if chips == 0:
            print("Chips zijn op")
        if 'stop' in inzet:
            chips += 1
            inzet.remove('stop')
            win = random.randint(0, 36)
            print(win)
            if str(win) in inzet:
              print("WINNER")
              chips += 35
              print("You now have: ",chips)
            else:
                print("HELAAS")
                print("You now have: ",chips)
            if chips == 0:
                print("GAME OVER")
                break
            opnieuw = input("Wilt u door gaan 'ja' of 'nee': ").lower()
            if opnieuw == 'nee':
                print("Uw eindscore is: ",chips)
                break