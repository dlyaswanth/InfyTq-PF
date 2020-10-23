#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if quantity_ordered<1 or distance_in_kms<1:
        return -1;
    if food_type=='V':
        bill_amount=quantity_ordered*120;
    elif food_type=='N':
        bill_amount=quantity_ordered*150;
    else:
        return -1;
    if distance_in_kms>=6:
        for i in range(4,6+1):
            bill_amount+=3;
    elif distance_in_kms<6 and distance_in_kms>3:
        bill_amount+=(distance_in_kms-3)*3;
    for i in range(7,distance_in_kms+1):
        bill_amount+=6;
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)