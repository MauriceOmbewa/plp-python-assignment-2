print("Test for sets")
print()

arrA = []
arrB = []
# arrC = []

setA = set()
setB = set()
setC = set()

lenA = int(input("How many numbers are you planning to put to set A?"))

for i in range(lenA):
    tempA = int(input("input number: "))
    arrA.append(tempA)

for val in arrA:
    setA.add(val)


# ---------------------------------
lenB = int(input("How many numbers are you planning to put to set B?"))

for i in range(lenB):
    tempB = int(input("input number: "))
    arrB.append(tempB)

for val in arrB:
    setB.add(val)

# ---------------------------------------

for v in setA:
    setC.add(v)

for v in setB:
    setC.add(v)

print(setA)
print(setB)

print(setC)