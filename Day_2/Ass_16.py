#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    flg=0;

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    five_needed=int(rupees_to_make/5);
    one_needed=rupees_to_make%5;
    if five_needed>no_of_five:
        temp=five_needed-no_of_five;
        if (temp*5)>no_of_one:
            flg=1;
        else:
            five_needed=no_of_five;
            one_needed= one_needed + temp*5
    if one_needed>no_of_one:flg=1;
    if flg==1:
        print(-1);
    else:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(125,22,15)