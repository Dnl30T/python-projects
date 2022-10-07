x = 99
y = 11
z = (x<<y)
count = 0
print(z)
while z > 0:
    z = z // 10
    count = count + 1
print("The number of digits is:", count)