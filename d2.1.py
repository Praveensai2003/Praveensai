def stair(n):
   if(n<=1):
      return n
   return stair(n-1)+stair(n-2)
s=int(input("enter the number :"))
print("no of ways",stair(s+1))
