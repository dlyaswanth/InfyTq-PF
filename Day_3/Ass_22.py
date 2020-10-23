#PF-Assgn-22
def find_leap_years(given_year):
    list_of_leap_years=[];
    for i in range(given_year,given_year+100):
        if (i%4==0 and i%100!=0) or i%400==0:
            list_of_leap_years.append(i);
        if len(list_of_leap_years)==16:
            break;
    return list_of_leap_years
list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)