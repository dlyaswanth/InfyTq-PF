#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    list1=[];
    if (num1>=num2):
        return max_num
    else:
        for i in range(num1,num2+1):
            list2=[int(k) for k in str(i)]
            sumdigit=sum(list2);
            if sumdigit%3==0 and len(str(i))==2 and i%5==0:
                list1.append(i);
    if len(list1)!=0:
        max_num=max(list1);
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)