#PF-Assgn-30

def encode(message):
    flg=0;msg='';
    if len(message)==1:
        msg+=str(1)+message;
        return msg;
    for i in range(len(message)):
        if (i<len(message)-1):
            if (message[i]!=message[i+1]):
                msg+=str(i+1-flg)+message[i];
                flg=i+1;
        elif i==len(message)-1:
            if message[i]!=message[i-1]:
                msg+=str(i+1-flg)+message[i];
    return msg;
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)