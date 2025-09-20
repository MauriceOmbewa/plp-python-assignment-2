print("This program displays summation")

count = 0
listt = []
summ = 0
result = 0

times = int(input("How many numbers are you going to add to the list? "))
# print(type(times))

while count < times:
    temp = int(input("Input number: "))
    listt.append(temp)
    count+= 1
    # summ += temp

# for n in listt:
#     result += int(n)
#     print(result)

for i in range(len(listt)):
    result += listt[i]



print("sum is: ", summ)
print("listt is: ", listt)
print("result is: ", result)