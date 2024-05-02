#guess the cubed root of a number 
#get input from the user 
#declare var for num and answer
#declare bools found, negative and is_less to false 
num = 51
answer = 0
found = False 
negative = False
is_less = False
#guard doesn't work to prevent user abuse 
while isinstance(num, int) == False or num > 50 or num < (-50) : 
    print("Usage : input a number between -50 and 50")
    num = int(input("What number do you want to find the cubed root of ? : "))

#set bool negative 
if num < 0 :
    negative = True 

#set num to be positive to shorten list of numbers to try out 
if negative == True :
    num *= (-1)

#from 0 to num (inclusive) test every number by elevating it to the power of three
#keep track of if the result is higher than num
for i in range(num+1) :
    if i**3 == num : 
        found = True
        answer = i
        break
    if i**3 < num : 
        is_less = True 
    else :
        is_less = False 
        answer = i
        break

#if the result of the elevation is higher than num, try floats around the tipping point 
if is_less == False :
        #go to the last number where the result was inferior to num
        float(answer) 
        answer = answer - 1
        for i in range(100) :
             if answer**3 == num : 
                  found = True
                  break
             elif answer**3 > num : 
                  break
             answer += 0.01

#set back answer to original sign
if negative == True :
     answer *= (-1)

#if found is true, print answer, else five aproximation 
if found == True : 
     print("The square root of " + "%i" % num + " is " + "%.2f" % answer) 
else : 
     print("The closest result we could find was " + "%.2f" % answer)