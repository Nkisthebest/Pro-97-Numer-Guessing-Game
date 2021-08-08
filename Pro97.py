import random
print('Number guessing game')
number=random.randint(1,9)
chances=0
print('Guess a number between 1 and 9')
print('You will get only 5 chances to guess the right numbe r!!!')
while chances <5:
    guess=int(input('Enter your guess => '))
    if guess==number:
        print('Congratulations! you win!!!' )
        break
    elif guess<number:
        print('Your guess was too low,guess a number higher than',guess)
    else:
        print('Your guess was too high,guess a number lower than',guess)
    chances+=1

if not chances<5:
    print('You lose!! the number is ',number)
