#This project takes in a question and an answer and assigns it
#to a dictionary.
#while loop
#use a variable as a condition to exit out of while loop
addQues = "YES"
#initilizalize dictionary
inputDictionary = {}
#inputDictionary = {}
listOfAnswers = []

while True:
    #variable to take in the question
    key = input("Type in a question: ")

    #variable to take in answer
    answer = input("Answer: ")

    while answer == "":
        print("Not valid answer, try again")
        print(key)
        answer = input("Answer: ")

    #set key:answer
    inputDictionary[key] = answer
    #               'Diana' = 30
    addQues = input("Do you want to add another question?")
    if addQues == "no":
        newUser = input("Do you want to add a new user? ")
        newUser2 = input("Do you want me to give you a question? ")

        if newUser == "yes":
            listOfAnswers.append(inputDictionary)
            inputDictionary = {}
            continue
        elif newUser == "no":
            listOfAnswers.append(inputDictionary)

        if newUser2 == "yes":
            newUser2 = input("What is your favorite color?")
            answer = input("Answer: ")
            inputDictionary = {}
            continue
        elif newUser2 == "no":
            listOfAnswers.append(inputDictionary)
            break

#print_list
print(listOfAnswers)
