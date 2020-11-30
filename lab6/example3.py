dic = {}
for i in range(0, 5):
  nameSalary = input("Write like 'name salary' combination your employee: ")
  name, salary = nameSalary.split()
  dic.update({name: salary})

temp_dict = {}
for key,value in dic.items():
  temp_dict[value] = key
new_list = []
for key in temp_dict:
  new_list.append(key)
new_list.sort()
new_list = new_list[-3:]
for value in new_list[::-1]:
  print(temp_dict[value])