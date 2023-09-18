def sum(n):
    sum = 0
    x=1
    while x <= n:
        sum = sum + x 
        x += 1 
    return sum 

n = int(input("enter till where you want to add"))
print ("SUM : " , sum(n))
