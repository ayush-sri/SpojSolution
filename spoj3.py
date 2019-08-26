#the next palimdrome

t = int(input())


def checkPalimdrome(n):
     sum=0
     num=n
     while n>0:
         r=n%10
         sum=(sum*10)+r
         n=n//10
     if num==sum:
         return True
     else:
         return False
n=[]
for j in range(t):
    n.append(int(input()))

for i,tem in enumerate(n):
    for j in range(tem+2,1000000):
           if checkPalimdrome(j):
               print(j)
               break

