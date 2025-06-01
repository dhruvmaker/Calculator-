import random

print("💖 Welcome to the Love Calculator 💖")
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

# Generate a random love score between 50 and 100
love_score = random.randint(50, 100)

print(f"\n{name1} ❤️ {name2}")
print(f"Your love score is: {love_score}%")

# Cute message
if love_score > 90:
    print("You are a perfect match! 💍")
elif love_score > 70:
    print("You both are great together! 💕")
elif love_score > 50:
    print("There is potential ❤️‍🔥")
else:
    print("Love is complicated... 😅")