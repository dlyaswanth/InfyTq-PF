#PF-Assgn-33
from collections import OrderedDict 
def find_common_characters(msg1,msg2):
    cmstr='';flg=0;
    newmsg1=''.join(OrderedDict.fromkeys(msg1));
    newmsg2=''.join(OrderedDict.fromkeys(msg2));
    for i in newmsg1:
        for j in i:
            if j in newmsg2:
                cmstr+=j;flg=1;
    return cmstr if flg==1 else -1;
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)