# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even on earth
You're in the middle of a giant maze on Mars.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your left, right and straight ahead of you.
'''

print(start)
#Starts game and asks user input
print("Type 'left' to go left or 'right' to go right or 'straight' to go straight.") # Update to match your story.
while True:
    print("Which way do you want to go? Left, right, or straight?") #prints question
    user_input = input("Type left, right, or straight.")#users' options
    if user_input == "left":
        print("You receive a rock")# if user chooses left, you recieve rock
        if user_input == "right":
            user_input = input()#users' choice
            print("You run into a mob of aliens and die.")#if user chooses right you run into a mob of aliens and die
            break
        if user_input == "straight":
            user_input = input()
            print("You find a space diamond.")#if user chooses straight, you find a space diamond
        if user_input == "right":
            user_input = input()#if user chooses right, you found your way out
            print("You found your way out! Congratulations, you may live now.")
            break
    elif user_input == "straight":
        print("You hit a dead end but don't touch the walls")#if user chooses straight, dead end, dont touch walls
        user_input = input("Type left, right, or straight.")
        if user_input == "left":
            user_input = input()
            print("You found a space dog.")
        if user_input == "straight":
            user_input = input()
            print("You found your way out! Congratulations, you may live now.")
            break
        if user_input == "right":
            user_input = input()
            print("You got stuck in a trap and time has run out. You have died.")
            break
    elif user_input == "right":
        print("You find a new path")
        user_input = input("Type left, right, or straight.")
        if user_input == "left":
            user_input = input()
            print("You found your way out! Congratulations, you may live now.")
            break
        if user_input == "straight":
            user_input = input()
            print("You tripped on a rock and died.")
            break
        if user_input == "right":
            user_input = input()
            print("You found a space ship and was able to escape the maze.")
            break
