"""Guess Dice Game"""
import random

roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print(f'Correct! They rolled a {roll}!')
else:
    print(f"You didn't guess correctly! They rolled a {roll}")
