# Student ID: 700757140
#       CRN :23476

def fullname(first_name, last_name):
  full_name= first_name+" "+last_name
  return full_name

class MyClass:
    def string_alternative(self,full_name):
       b = "";
       c = 0;
       for x in full_name:
           if c==0:
             b+=x
             c = 1
           else:
             c = 0
       return b

def main():
    # Creating an instance of MyClass
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    my_instance = MyClass()

    # Calling the my_method of the instance
    full_name=fullname(first_name,last_name)
    print(my_instance.string_alternative(full_name))

if __name__ == "__main__":
    # Calling the main function when the script is executed
    main()

