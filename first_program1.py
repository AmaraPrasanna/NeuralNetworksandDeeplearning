# Student ID: 700757140
#       CRN :23476


#Question 1A

Str = list(input("Enter the string 'Python': "))

if len(Str) >= 2:
    # deleting the first two characters
    del Str[:2]
    # Reverse the resultant string
    reversed_string = Str[::-1]
    print("Reversed String:", ''.join(reversed_string))

    


