#Second Code

# input "axrxa" 
# output:= axrxa 4
#chack start and end character if both  are same don't switch and count them else switch

string= "axrxa"  
start=0
end=len(string)-1
tempEnd=end
end=int(tempEnd/2)+1
startString=""
endString="" 
count=0
while start != end:  
    if start!=tempEnd:
        if string[start]==string[tempEnd]: 
            startString+=string[start]
            endString=string[tempEnd]+endString
            count+=2
        else: 
            startString+=string[tempEnd]
            endString=string[start]+endString
    else:
         startString+=string[start]
    start+= 1 
    if tempEnd>=end:
        tempEnd-= 1
print("output:=",startString+endString,count)
