def checkRevenue(r, e, c):
    if(r == (e - c)):
        return "does not matter\n"
    if(r > (e - c)):
        return "do not advertise\n"
    if(r < (e - c)):
        return "advertise\n"
count = int(input())
result = ""
for _ in range(count):
    (r, e, c) = input().split()
    r = int(r)
    e = int(e)
    c = int(c)
    result  = result + checkRevenue(r, e, c)
print(result.rstrip(result[-1]))
