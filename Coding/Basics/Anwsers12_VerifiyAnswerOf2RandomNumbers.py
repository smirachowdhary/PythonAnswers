import random

random_number1 = random.randint(100,1000)
random_number2 = random.randint(1,100)
wrong = 0
right = 0

i = 0
while i > 20:
    print(f"{random_number1} * {random_number2}")
    User_answer = int(input("Enter Answer(No commas or you'll get your question wrong):"))
    if random_number1 * random_number2 == User_answer:
        print("You are correct!!")
        right+=1
    else:
        print("Sorry, you are wrong. Try again(this is your last chance).")
        Last_chance = int(input("Enter Answer(No commas or you'll get your question wrong):"))
        if random_number1 * random_number2 == Last_chance:
            print("You are correct!!")
            right+=1
        else:
            print(f"Sorry, you are wrong. The real answer is {random_number1 * random_number2}.")
            wrong+=1
    i+=1
print(f"Out of 20 questions, you got {wrong} wrong and {right} right.")