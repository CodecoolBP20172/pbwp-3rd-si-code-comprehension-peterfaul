import random # Find and loading the random module

guessesTaken = 0 # Initialize 0 to guessesTaken variable

print('Hello! What is your name?') # Use print function to write the given string to console
myName = input() # Assign value of myName variable as an input function

number = random.randint(1, 20) # Assign a random value (from 1 to 20) to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # Write the strings to console with value of myName variable addition

while guessesTaken < 6: # Repeat execution as long as the expression is true
    print('Take a guess.') # Use print function to write the given string to console
    guess = input() # Assign value of guess variable as an input function
    guess = int(guess) # Convert/cast the value of guess to integer

    guessesTaken += 1 # Increase the value of guessesTaken variable by 1

    if guess < number: # Execution depends on the given condition(guess variable less than the number variable)
        print('Your guess is too low.') # Use print function to write the given string to console

    if guess > number: # Execution depends on the given condition(guess variable more than the number variable)
        print('Your guess is too high.') # Use print function to write the given string to console

    if guess == number: # Execution depends on the given condition(guess variable equals exactly number variable)
        break # Exiting from the conditional execution

if guess == number: # Execution depends on the given condition(guess variable equals exactly number variable)
    guessesTaken = str(guessesTaken) # Convert/cast the value of guessesTaken to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # Write the given strings to console with two value additions

if guess != number: # Execution depends on the given condition(guess variable is not equals number variable)
    number = str(number) # Convert/cast the value of number variable to string
    print('Nope. The number I was thinking of was ' + number) # Write the strings to console with value addition
