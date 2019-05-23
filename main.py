import random
import json
import datetime

player = input("Hello! What is your name? ")

secret = random.randint(1, 30)
attempts = 0
failed_attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    failed_attempts = attempts - 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()) + " Player name: " + player + " Secret number: " + str(secret)})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        print("Attempts failed: " + str(failed_attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
