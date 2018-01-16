# Paste your code into this box
print('Please think of a number between 0 and 100!')
answer=''
l = 0
h = 100
guess=(h+l)//2
print('is your secret number 50?')
while answer!='c':
    answer=input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if answer=='c': 
        print('Game over. Your secret number was: '+str(guess))
        break
    elif answer!='l'and answer!='h' and answer!='c':
        print('Sorry, I did not understand your input.')
    elif answer=='h':
        h=guess
    elif answer=='l':
        l=guess
    guess=(h+l)//2
    print('Is your secret number '+str(guess)+'?')