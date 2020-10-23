#PF-Assgn-31
def check_palindrome(word):
    if word==word[::-1]:return 1;
    else:return 0;
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")