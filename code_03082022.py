# program 1

# input 245 then check prime number and sum of them as discount 
# Example 245 is input then 
# 2 = is a prime number 
# 4 = not a prime number  
# 5 = is a prime number 
#  so sum of prime number is 2+5=7

num=input()
def discountAMT(order):
    number=order 
    billDis=0
    for x in str(number):  
        num = int(x)  
        flag = False 
        if num > 1: 
            for i in range(2, num):
                if (num % i) == 0: 
                    flag = True 
                    break 
        if flag:
            print("")
        else:
            billDis+=num 
    return (billDis)

print("output:=",discountAMT(num)) 

