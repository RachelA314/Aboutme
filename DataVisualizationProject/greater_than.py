list = [2,5,6,3,8,12,1,9] #list of numbers

list2 = [] #empty list for greater numbers

#for loop to go through list and find numbers greater than 5
for i in list:
        if i >= 5:    #numbers 5 and > added to list with append
            list2.append(i)
            print(list2)
#prints list2 of greater numbers

#sum is 0
sum = 0
#for loop to find sum in list2
for num in list2:
    sum += num
# adds numbers together in list2

    average = sum/len(list2)
 #finds average number, divides sum by length of list2

#prints average number
print(average)
