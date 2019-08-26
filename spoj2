pri = []
limit=1000000
t=int(input())
for i in range(limit):
    pri.append(True)
pri.__setitem__(0,False)
pri.__setitem__(1,False)
#multiples of 2
p=1
for i in range(2,limit):
   if i*2<=limit-1:
       pri.__setitem__(i*2,False)
   if i*3<=limit-1:
       pri.__setitem__(i*3,False)

   if i * 5 <= limit-1:
       pri.__setitem__(i * 5, False)

   if i * 7 <= limit-1:
       pri.__setitem__(i * 7, False)

   if i * 11 <= limit-1:
       pri.__setitem__(i * 11, False)
   if i * 13 <= limit - 1:
       pri.__setitem__(i * 13, False)

for i in range(t):
    m, n = map(int,input().split())
    print()
    if n-m<=100000:
      for index in range(m, n + 1):
         if pri.__getitem__(index):
            print(index)


