# 1st way to solve  

''' Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference. '''

a = 17 
b = int(input("enter the number to calculate the diffrence between a given number and 17 : "))


if b != 0 : 
    if a == b:
        c=(" both the values are same ");
        
    elif b <= 17 : 
        c=(" the value is less than 17 and the compasrion between the numbers is", a-b ) 
           
    else:
        c=((b-17)*2)
else :
     c=(" input value is less than zero and the compasrion between the numbers is", a-b)

print ("1st way to solve ,", c)     
    
    
# 2nd way to solve   
''' Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference. '''

print ("\n2nd way to solve")
def difference(b):
    if b <= 17:
        return 17 - b
    else:
        return (b - 17) * 2 

print( difference(b))


