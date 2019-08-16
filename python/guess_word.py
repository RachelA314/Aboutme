# Some useful variables
import random
guesses = []
maxfails = 7
fails = 0
guess = input()

# A list of words
word_list = ["cake", "pineapple", "raspberry", "penguins", "pandas"]
word = random.choice(word_list)
# Use to test your code:
print(word)
# Converts the word to lowercase
word = word.lower()
# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word
lengthOfCurrentWord = len(word)
for char in range(lengthOfCurrentWord):
    current_word.append ("_ ")

    print(current_word)

while fails < maxfails:
	guess = input("Guess a letter: ")
guess.lower()

if guess.isalpha() == False:
    print("Please enter a letter!")
elif guess in guesses == True:
    print("You guessed %s already, try again." %(guess))
elif guess.isalpha() == True and len(guess) == 1 and guess not in guesses == True:
    guesses.append(guess)

rightAns = True

index = 0
if guess in word:
    for char in word:
        if guess == char:
        current_word[index] = guess
    index +=1
    if(index == (len(word))):
        break
else:
    fails = maxfails+1
    print("You have" + str(maxfails - fails)+ "tries left!")
print(current_word)
cword = ''.join(current_word)
print(cword)
if (cword == word):
    print("Good job")
    break

if fails == maxfails:
    print("Game Over")



if fails >= maxfails:
    print("No more guesses you lose")

else:
    print("You guessed the correct word")
    print(current_word)
    fails = fails+1
    print("You have " + str(maxfails - fails) + " tries left!")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
def say_hello():
    print("Hello from a function")
say_hello()

def say_name(name):
    print("Hello %s" %(name))
say_name("Rachel")

list1 = ["Fran", "Seyla", "Grace"]
list2 = ["dog","cat","99"]
list3 = ["fordham","barnard","queens"]
def print_list(anylist):
    for name in anylist:
        print(name)
print(list1)
print(list2)
print(list3)'''

'''def add(num1,num2):
    sum = num1 + num2
    return sum
print(add(11,7))#18
(add(100,300))#nothing

fransAge = 2019 - add(1990,7)
print(fransAge)

a = 5
def aVariable():
    a = 10
    sum = a + 10
    print(sum)
aVariable()

def print_names(names):
    for i in names:
        print(i)
print_names(list)

def process_input(answer):
    if answer == "hi":
        say_greeting()
    else:
        say_greeting()'''
