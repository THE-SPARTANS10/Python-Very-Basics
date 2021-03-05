secret_word="Python"
max_try=3
guess_count=0
is_out_of_guesses=False
guess=""
while secret_word != guess:
    guess=input("Enter your guess: ")
    guess_count+=1
    if guess_count==max_try and guess != secret_word:
        is_out_of_guesses=True
        break

if is_out_of_guesses:
    print("You are out of guesses!!!")
else:
    print("You guessed it right!!")