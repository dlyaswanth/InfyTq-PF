def solve(heads,legs):
    chicken_count=0
    rabbit_count=0
    if legs % 2 !=0 or heads ==0 or heads > legs:
        print('No solution')
        return 1;
    else:  
        chicken_count = int((legs + (-2*heads))/2)
        rabbit_count = int(heads - chicken_count)
    print(rabbit_count,chicken_count)
#Provide different values for heads and legs and test your program
solve(5,10)