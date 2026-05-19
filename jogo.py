import random # gives us tools for picking random numbers
secret= random.randint(1,20) # a <=secret<= b
tries= 0
guess= 0 # start with a value that cannot be the secret (since secret is 1..20)
max_attempts= 5

print("I'm thinking of a number between 1 and 20")
print(f"You have a maximum of {max_attempts} attemps to guess it!\n")


# Repeat until the user guesses the secret number.
while guess != secret and tries < max_attempts:
	text= input("Take a guess: ") # input() returns text (a string)
	guess= int(text) #convert the text to a number
	tries= tries + 1 # add 1 try (written long-form for clarity)


# Give a hint using if/elif/else.
	if guess < 1 or guess > 20:
		print("That number is out of range. Try again.")
	elif guess < secret:
		print("Too low, try again.")
	elif guess > secret:
		print("Too high, try again.")
		
		
#- Comportamento após o fim do loop (fora do while)
if guess == secret:
	print(f"\nFantastic! You got it in {tries} tries!")
else:
	print(f"\nGame Over! You've used all {max_attempts} attempts.")
	print(f"The secret number was: {secret}")
	

			
		
		
	
		
      
