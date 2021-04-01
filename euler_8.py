data = open("euler_8.txt")
number = data.read(1001)
data.close()
answer = 0
for i in range(0,985):
    num = number[0+i:13+i]
    v = 1
    for char in num:
        v *= int(char)
    if v > answer:
        answer = v
print(answer)
