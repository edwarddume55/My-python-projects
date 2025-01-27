
print ('welcome to my quiz game')

playing = input('Do you want to play the game? ')

if playing.upper() != 'YES':
    quit()
print("Okay let's start:")
score = 0
correct = 0

answer = input("What does GIF stands for? ")
if answer.lower() == "graphics interchange format":
    print('Correct')
    score += 5
    correct += 1
else:
    print('Incorrect')

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 5
    correct +=1
else:
    print('Incorrect')

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct')
    score += 5
    correct +=1
else:
    print('Incorrect')

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print('Correct')
    score += 5
    correct +=1
else:
    print('Incorrect')

print( 'you got ' + str(correct) + ' correct' + 'which is ' + str((score/20)*100) + ('%.'))