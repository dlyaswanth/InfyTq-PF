def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    flg=0;
    if account_balance>=100000 and str(account_number)[0]=='1':
        if account_balance>=100000:
            if salary>25000 and loan_type=="Car" and loan_amount_expected<=500000 and customer_emi_expected<=36:
                flg=1;
                eligible_loan_amount=500000;
                bank_emi_expected=36;
            elif salary>50000 and loan_type=="House" and loan_amount_expected<=6000000 and customer_emi_expected<=60:
                eligible_loan_amount=6000000;flg=1;
                bank_emi_expected=60
            elif salary>75000 and loan_type=="Business" and loan_amount_expected<=7500000 and customer_emi_expected<=84:
                eligible_loan_amount=7500000;flg=1;
                bank_emi_expected=84
            elif (loan_type!='Car' and loan_type!='House' and loan_type!='Business') or (salary<=25000 and loan_type=="Car" and loan_amount_expected<=500000 and customer_emi_expected<=36)  or (salary<=50000 and loan_type=="House" and loan_amount_expected<=6000000 and customer_emi_expected<=60) or (salary<=750000 and loan_type=="Business" and loan_amount_expected<=7500000 and customer_emi_expected<=84):
                print("Invalid loan type or salary")
                return 1;
            if(flg==1):
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
                return 1;
    if account_balance<100000:
        print("Insufficient account balance");
        return 1;
    if str(account_number)[0]!='1':
        print("Invalid account number");
        return 1;
    if (flg==0):
        print("The customer is not eligible for the loan")
#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)