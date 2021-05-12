# Temi
#IT-140
# A program that out put your name and the year you were born in
#   when you provide your name and age.

first_name = input("What is your name?")
age = int(input("How old are you?"))
year_born = int(2021) - age

print("Hello " + first_name + "!" + " You were born in ", year_born,".")
