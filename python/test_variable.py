print("Variable Example")'''

#string variable for my name
my_name = "Rachel"
#integer variable for my my_age
my_age = 17

#print my name and age
print(my_name)
print(my_age)

#asking user how old their mom is
my_moms_age = input("How old is your mom?")
print(my_moms_age)

#print my_name, my_age, my_moms_age
print("Hello my name is %s.I am %d years old. My mother is %s years old." %(my_name, my_age, my_moms_age))
'''
print("An Example on Counters")

#initilizaing variables
#i increments by 1 and is the counter.
#num_loop increments by 1. keep track of iterations
num_guesses = 0
num_loop = 0
while True:
    num_guesses += 1 #increments by 1
    num_loop += 1

    print("You made %d guesses. This is loop number %d" %(num_guesses, num_loop))
    if(num_guesses == 100):
        print("num_guesses has reached 100. Loop will stop")
        break
