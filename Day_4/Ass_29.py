#PF-Assgn-29
def calculate(distance,no_of_passengers):
    total=distance/10*70;
    pas=no_of_passengers*80;
    if total>pas:
        return -1;
    else:return pas-total;
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))