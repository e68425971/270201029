first = float(input("write the first car's velocity "))
second = float(input("write the second car's velocity "))
road= float(input("how many km is your road "))

result = (road / (first + second) ) * 60
print(f"they will crash {result} minutes later")