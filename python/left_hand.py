'''
leftHandUp = False
rightHandUp = False
if(leftHandUp & rightHandUp):
    print("Jump!")
elif(leftHandUp or rightHandUp):
    print("one hand up but not both")
else:
    print("no hands up?")
'''
#initilizaing variables
leftHand = input("left hand up or down?")
rightHand = input("right hand up or down?")

#enter into if statement
#if both hands up print Jump
if(leftHand == "up" and rightHand == "up"):
    print("Jump!")
elif(leftHand == "down" or rightHand == "down"):
    print("one hand up but not both!")
else:
    print("no hands up!")
