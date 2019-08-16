from random import*
#this is a LIST of women in tech
womenInTech = ["Amanda Randles", "Dr. Aprille Joy Ericsson", "Cindy Alvarez", "Dorothy Vaughan", "Jess Lee"]

#this is a FOR loop that PRINTS each name in the LIST
for women in womenInTech:
    print(women)



#one way to print out the number of women in tech in my list
print("This is the number of women attending the conference: ")
print(len(womenInTech))

#STORING THE SIZE OF THE LIST IN A VARIABLE CALLED 'numberOfWomen'
numberOfWomen = len(womenInTech)
print("This is the number of women attending the conference: %d" %( numberOfWomen))



#CHECKING TO SEE IF JESS LEE IS IN THE LIST
print("IS Jess Lee in the list")
print("Jess Lee" in womenInTech) #this will return True

#CHECKING TO SEE IF KRIS JENNER IS A WOMEN IS IN THE list
print("Is Kris Jenner a computer scientist?")
print("Kris Jenner" in womenInTech)

#Seeing a loop using the built in function called 'range'
for i in range(len(womenInTech)):
    print(womenInTech[i])

#This is how many times the for loop runs
limit = range(len(womenInTech))
for i in limit:
    print(womenInTech)
#choosing a random guest speaker
aRandomNumber = randint(0,4)#randint is a built in function that
                            #takes in a start and end
print("The rand number generator chose: %d" %(aRandomNumber))

randomGuestSpeaker = womenInTech[aRandomNumber]
print(randomGuestSpeaker)

'''anExample = "Raspberry"
print(len(anExample))
#Output: 9
print("berry" in anExample)
#Output: True
print(anExample[7])
#Output: r
print(anExample[7] + anExample[8])
#Output: ry
for letter in anExample:
    print(letter)

ages = [2, 22, 16, 4, 17]

sum=0
for age in ages:
    sum += age

Avg = (sum/len(ages))
print(Avg)'''
