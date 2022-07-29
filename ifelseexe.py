# 34=27+16
""" name should be meaning full always """
num = 34
first = int(num/10)

if first%2==0:
    on=(first*first)
else:
    on=(first*first*first)
sec= num%10
if sec%2==0:
    off=(sec*sec)
else:
    off=(sec*sec*sec)
print("the ans is " ,on+off)


