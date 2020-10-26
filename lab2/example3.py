lessonNumber=int(input("write your lesson number: "))
gpa=float(input("write your gpa: "))

if lessonNumber < 47 and gpa < 2:
  print("Not enough number of lectures and GPA!")

elif lessonNumber >= 47 and gpa < 2:
  print("Not enough GPA!")

elif lessonNumber < 47 and gpa >= 2:
  print("Not enough number of lectures")

elif lessonNumber >= 47 and gpa >= 2:
  print("GRADUATED!")

else:
  print("wth")