'''Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference.'''

a = 17 
b = int(input("enter the number to calculate the diffrence between a given number and 17 : "))

if b != 0 : 
    if a == b:
        print(" both the values are same ");
    
    elif a > b :
        print (" the value is less than 17 and the compasrion between the numbers is", a-b ) 
        
    elif a < b :
        print (" the value is greater than 17 and the compasrion between the numbers is", b-a)
        
else :
    print (" inpute value is less than zero and the compasrion between the numbers is", a-b)
    
    