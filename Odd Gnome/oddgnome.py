def getPosition(data):
    for i in range(1, len(data)):
        if(data[i] != (data[i - 1] + 1)):
            return i + 1
    return -1
result = ""
count = int(input())
for _ in range(count):
    data = input().split()
    data = [int(d) for d in data]
    data.pop(0)
    result = result + str(getPosition(data)) + "\n"
print(result.rstrip("\n"))
