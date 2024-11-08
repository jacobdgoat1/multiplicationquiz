import random
random_number = random.randint(1,10)
outer_count = 0
while outer_count < 5:
    num1 = random_number
    num2 = random_number
    product = num1 * num2
    print(f"Question {outer_count + 1}: What is {num1} x {num2}?")
    inner_count = 0
    while inner_count < 5:
        guess = int(input("Guess"))
        print(f"You answer: {guess:}")
        if guess == product:
            print("Correct!")
            break
        else:
            print("Incorrect. Try again")
            inner_count += 1
        outer_count += 1

