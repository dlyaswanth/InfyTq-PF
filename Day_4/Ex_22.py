#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    if no_of_passengers<5:
        for i in range(0,no_of_passengers):
            str1='';
            str1+=airline+':'+source[0:3]+':'+destination[0:3]+':'+str(i+101);
            ticket_number_list.append(str1);
    else:
        for i in range(no_of_passengers-5,no_of_passengers):
            str1='';
            str1+=airline+':'+source[0:3]+':'+destination[0:3]+':'+str(i+101);
            ticket_number_list.append(str1);
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",10))