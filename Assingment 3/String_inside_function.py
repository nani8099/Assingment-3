# Write a Python program to reverse a string.

# Sample String : "1234abcd"

# Expected Output : "dcba4321"


str = "1234abcd"   
print ("The original string  is : ",str)   
reverse_String = ""    
count = len(str)  
while count > 0:   
    reverse_String += str[ count - 1] 
    count = count - 1   
print ("The reversed string is : ",reverse_String)



# OUTPUT:
# The original string  is :  1234abcd
# The reversed string is :  dcba4321





