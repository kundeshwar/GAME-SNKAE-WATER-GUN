import random
a = random.randint(1,3)
if a == 1:
    comp = 'snake'
elif a==2:
    comp = 'water'
else:
    comp = 'gun'
you = int(input("choice any one :- water(2),snake(1),gun(3)\n \t \t"))
if you == 1:
    yourchoice = 'snake'
elif you==2:
    yourchoice = 'water'
else:
    yourchoice = 'gun'
if comp == yourchoice :
    print("yourchoice is", yourchoice)
    print("computer slected",comp)
    print("game is tie, thanks for playing!")
elif(( comp=='snake' and yourchoice=='water') or (comp=='water'and yourchoice=='gun') or (comp=='gun'and yourchoice=='snake')):
    print("yourchoice is", yourchoice)
    print("computer slected",comp)
    print("you loss the game, thanks for playing!")
else:
    print("yourchoice is", yourchoice)
    print("computer slected",comp)
    print('''congrulation !
    you are win , thanks for playing!''')
