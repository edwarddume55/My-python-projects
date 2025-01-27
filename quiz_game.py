
print ('welcome to my quiz game')

playing = input('Do you want to play the game? ')

if playing.upper() != 'YES':
    quit()
print("Okay let's start:")
score = 0

answer = input("What does GIF statnds for? ")
if answer.lower() == "graphics interchange format":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does CPU statnds for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does RAM statnds for? ")
if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does ROM statnds for? ")
if answer.lower() == "read only memory":
    print('Correct')
    score += 1
else:
    print('Incorrect')

print( 'you got ' + str(score) + ' correct' + 'which is ' + str((score/4)*100) + ('%.'))