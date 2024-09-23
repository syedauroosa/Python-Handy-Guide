print("helloworld")

#Data type of string, we have multiple datatype in python, string, boolean, list and xyz

#string concatination

firstName: str = "Uroosa"
lastName: str = "Nouman"
print("Mrs", firstName, lastName)
#print("Mrs", + firstName + "   " + lastName)

# to make easy
# use F string 
print(f'Mrs  {firstName} {lastName}, i am happy, i am fine, i am strong, everything comes to me at perfect time, univere and i are align')

#need explaination of this code
print("Mrs "   + firstName +  "   " + lastName)

#for method we can identify with dot (.)
#1 firstName.
#dir word also used for method

print (dir(firstName))

#will make wrods in capooital letters in upper case method
print(firstName.upper())

#will make wrods in SMALL letters in lOWER case method
print(lastName.lower())

#will make FIRST alphabet capital wrods in letters in upper case method
print(firstName.title())

#create variable 
message: str = "I am writing handy python for biginners"
print(message)
 
#update variable        

# if you're updating variable dont need to assign variable type, otherwise it will show you are assigning multiple values 
#if updating variable example in line 43, it will give you same value till line 42 (pervious value) 

message :str = "my book's first page is completed" 
print(message)


#backslash can change paragrapgh
message :str = "my book's \f first page is completed" 
print(message)

#Multiple variables with multiple values

student1 : str ="Uroosa" 
student2 : str = "Samiha"
student3 : str = "fatima"


#assign one varible for multiple values
#creating list for multiple values.
#we  will import list from typing
#will create variable, will allow the value as str or int.
#all values will store in square brackets 
# all values will be seprarted through comma ("sami" , "ayshi")
# all values will wrape with inverted commas e.g ("samiha")

from typing import List
Students : List[str] =["Uroosa", "samiha", "fatima"]
print(Students)

#index number 
#positive indexing left to right 0-...
#negative indexing right to left ...-1


#                            0,   1,          2   
Students : List[str] =["Uroosa", "samiha", "fatima"]
#                           3       2          1                        

#print values with index number
#index number will print in square bracets e.g. [0], [2]
print(Students[0])

# also can print negative indexing
print(Students[-1])


# also can apply methods on index   
# for method will close the value with small brackets e.g =.title()
# as you can see in the picture using small brackets after Print ()
#anything is you want to print you will write inside small brackets e.g print("Hello - world")
#if indside small brackets you are adding index number as you can see the syntax print(Students[-2])
# if adding index and method inside print the syntax will beexample, print(Students[-2].title())


print(Students[-2].title())
print(Students[2].upper())
print(Students[1].lower())      