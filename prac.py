import random
lolist = []

for i in range(5):    
    lotto = []
    for j in range(7):
        number = random.randint(1,45)
        while number in lotto:
            number = random.randint(1,45)
        lotto.append(number)
    lolist.append(lotto)
lolen = list(range(len(lotto)))
print(lolist,lolen)