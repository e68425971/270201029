grades = [[50, 90, 60], [15, 60, 75], [99, 95, 91]]

talentedİdiot = []
studentid = 1

for student in grades:
  first = student[0] * 30 / 100
  second = student[1] * 30 / 100
  third = student[2] * 40 / 100
  total = first + second + third

  print("The student's gpa: " + str(total))
  
  if total >= 90.00:
    talentedİdiot.append(str(studentid))

  studentid += 1
    
print(talentedİdiot)