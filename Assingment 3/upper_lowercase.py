# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12


x=input("Enter the string:- ")
def char(x):
  u=0
  l=0
  for i in x:
      if i>='a' and i<='z':
       l+=1

      if i >='A' and i<='Z':
       u+=1

  print("UpperCase characters in the String",u)
  print("LowerCase characters in the String",l)
char(x)



# OUTPUT:

# Enter the string: The quick Brow Fox
# No.of upper case characters  3
# No. of lower case characters 12





