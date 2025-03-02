user = input("Do you want to play a game? ")

if user.lower() != "yes":
    quit()
print("Okay! Lets play :) ")
score = 0

answer = input("What CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect! ")

answer = input("What RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect! ")

answer = input("What GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect! ")

answer = input("What PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect! ")

print(f"You got {score} question correct.")
print(f"You got {(score/4)*100} %.")

