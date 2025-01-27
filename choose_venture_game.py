name = input('Tpe your name:')

print('welcome', name, 'to this venture')
answer = input(
    'you are on a dirt road, it has come to an end and you can go left or right, which way would you like to go(left/right)? '
).lower()

if answer == "left":
    answer == input('You come to a river, you can walk around it or swim across, Type walk to walk around and swim to swim across').lower()
    if answer== "swim":
        print('You swim across and you were eaten by crocodile')
    elif answer == "walk":
        print('you walked for many miles and you lost the game')
    else:
        print('not a valid option. You loose')

elif answer == "right":
    answer = input('you came to a bridge it looks wobbly, do you want to cross it or head back (cross/back)?').lower()
    if answer== "back":
        print('You go back to the main road, and loose!')
    if answer == "cross":
        answer = input('you choose to cross the bridge, you meet a stranger will you talk to them (yes/no)? ').lower()

        if answer== "yes":
            print('you talked to the stranger and they give you silver. YOU WIN')
        elif answer=="no":
            print("you Ignored the stranger, and you loose")
        else:
            print("not a valid option. You loos!")
        
       

    else:
        print('not a valid option. You loose')
else:
    print('not a valid option. You loose')