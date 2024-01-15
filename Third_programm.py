# Student ID: 700757140
#       CRN :23476

#Question 3

Score=float(input("Enter the Score : "))
if Score>100:
   print("Enter a valid Score")  
elif Score >= 90 :
  print("Grade A")
elif Score>=80:
  print("Grade B")  
elif Score>=70:
  print("Grade C")  
elif Score>=60:
  print("Grade D")  
elif Score<60 and Score>=0:
  print("Grade F")
else:
  print("Enter a valid Score") 
   
  