 # 30 Days of Python Programming

# Exercises: Level 1

first_name = "Umar"
last_name = "Haruna"
full_name = first_name + last_name
country = "Nigeria"
city = "Kano"
age = 180
year = 2024
is_married = False
is_true = True
is_light_on = True

number1 , number2 ,number3 = 4, 10, 9

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))
print("The Length of My first Name is: ",len(first_name),"and the length of my Last name is : ",len(last_name))

num_one = 5 
num_two = 4

total = num_one + num_two

print("The sum of Number2 And Number1 is : ", total)

variable_dif = num_two - num_one

print("The Differencial of Number2 And Number1 is : ", variable_dif)

variable_product = num_two * num_one

print("The Product of Number2 And Number1 is : ", variable_product)

variable_division = num_one / num_two 

print("The Divition factor of Number1 And Number2 is : ", variable_dif)

variable_remainder = num_two % num_one

print("The Remainder of Number2 And Number1 is : ", variable_remainder)

var_exp = num_one ** num_two

print("The Exponential of Number1 to the Number2 is : ", var_exp)

floor_div = num_one // num_two 

print("The Floor Division of Number1 And Number2 is : ", floor_div)

pi =3.142

radius = 30 
area_circle = pi * (radius ** 2)

print("The Area of The Circle With Radius of", radius , " is: " ,area_circle)

circum_of_circle = 2 * pi * radius

print( "The Circumference of a circle with Radius of "  ,radius ," is : " , circum_of_circle)

radius2 = input("Please Enter The Radius Of the Circle :")

circum_of_circle2 = 2 * pi * float(radius2)

area_circle2 = pi * (float(radius2) ** 2)

print("The Area of The Circle With Radius of", radius2 , " is: " ,area_circle2)
print( "The Circumference of a circle with Radius of "  ,radius2 ," is : " , circum_of_circle2)

my_first_name = input("Please Enter your Name : ")
my_last_name = input("Please Enter Your Last name : ")
my_country = input ( "Please Enter your Country : ")
my_age = input ("Please Enter your Age : ")

message = f"Hi " + my_first_name + " " + my_last_name  +" You have a Very Cool Name" + " I See You're From a " + my_country + " What aWondaful Place " +  my_age +" Your Age are Fasinating"

print(message)