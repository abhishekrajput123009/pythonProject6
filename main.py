import random as rd

x = ['rock', 'paper', 'scissor']
n = input("pick any from X :")
y = (rd.choice(x))
if n == 'rock' and y == 'paper' or n == 'paper' and y == 'scissor' or n == 'scissor' and y == 'rock':
    print('you loose !')
elif n == 'paper' and y == 'rock' or n == 'rock' and y == 'scissor' or n == 'scissor' and y == 'paper':
    print('you win !')
elif n == y:
    print('tie')
else:
    print('invalid')