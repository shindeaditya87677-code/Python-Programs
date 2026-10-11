#find the missing number
#method1:
numbers=[1,2,4,6,3,7,8]
n=8
for i in range(1,n+1):
   if i not in numbers:
        print("missing number is:",i)
        
#method2:
def missingnum(numbers,n):
    num1 = (n * (n + 1)) // 2
    num2=0
    for num in numbers:
        num2+=num
    return num1-num2
numbers=[1,2,4,6,3,7,8]
n=8
print("Missing Number:",missingnum(numbers,n))