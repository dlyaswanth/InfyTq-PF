#PF-Exer-15

def find_sum_of_digits(number):
    sum_of_digits=0
    while(number>0):
        sum_of_digits+=number%10;
        number//=10;
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)