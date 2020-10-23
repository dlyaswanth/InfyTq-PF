#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    total_ticket_cost=no_of_adults*37550.0;
    total_ticket_cost1=no_of_children*(37550.0/3);
    total_ticket_cost=total_ticket_cost+total_ticket_cost1
    total_ticket_cost=(0.07*total_ticket_cost)+total_ticket_cost;
    total_ticket_cost=total_ticket_cost-(0.10*total_ticket_cost);
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)