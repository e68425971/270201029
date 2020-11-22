numbers = int(input("how many numbers: "))
evenNumbers = 0
oddNumbers = 0
for i in range(1, numbers+1):
    entry = int(input("Enter an integer: "))
    if entry % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

print("percentage of even numbers"+""+(evenNumbers/numbers)*100+"%") 
#percentage of even numbers