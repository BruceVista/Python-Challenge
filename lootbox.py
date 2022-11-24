import random

print("Opening lootbox")
rarity = ( "Common" , "Uncommon" , "Rare" , "Epic" , "Legendary" )
print(random.choices(rarity, weights=(50, 30, 14 ,5 ,1)))