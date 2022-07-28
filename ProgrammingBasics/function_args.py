#Positional Arguments
def user_info(name, age, city):
    """This function prints name, age and city
    from an argument provided by the function."""
    print("{} is {} years old, and lives in {}".format(name, age, city))
    
user_info("Pepito Perez", 43, "Medellin")

#Keyword Arguments, differ from positional: KwArgs have predefined variables
def user_info2(name, age=0, city="Arkansas"):
    """This function prints name, age and city
    from an argument provided by the function."""
    print("{} is {} years old, and lives in {}".format(name, age, city))
    
user_info2("Pepito Perez")
user_info2(city="Tolima", name="Juana") #can be reordered

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email address is {}.".format(fname, lname, company, email))
    
application("Maria", "Fernandez", "mail@mail.com","Tech-Comp", 75000, hire_date="September 2020")
