#This program will find the average of the list

#This is the list of ages
'''ages = [2, 22, 16, 4, 17]

#Calculating the average

#Step 1: find the sum
sum=0
for age in ages:
    sum += age
#Print the sum to verify that it is correct
print("The sum of all ages is %d" %(sum))
#Divide by length
average = sum/len(ages)
print("The average age is %d" %(average))
'''
#This program will create a list of ages (through user input)AND calculates the average

#This is a list that will store all of the users listOfAges
listOfAges=[]

#This is a variable that acts as a counter for many ages are
numberOfAges = 0

while (numberOfAges <=5):
    #This retrieves user input and stores it into a variable called 'age'
    age = input("Please enter an age:")
    #age = int(age)
    age = int(age)
    print(age)
    listOfAges.append(age)
    numberOfAges+=1

print("Here is your list:")
print(listOfAges)

'''sum = 0
for ages in numberOfAges:
    sum += age'''

'''ages = [2, 22, 16, 4, 17]

#Calculating the average

#Step 1: find the sum
sum=0
for age in ages:
    sum += age
#Print the sum to verify that it is correct
print("The sum of all ages is %d" %(sum))
#Divide by length
average = sum/len(ages)
print("The average age is %d" %(average))'''
