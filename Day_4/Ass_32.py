#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    pcount=patient_medical_speciality_list.count('P');
    ocount=patient_medical_speciality_list.count('O');
    ecount=patient_medical_speciality_list.count('E');
    if pcount>ocount and pcount > ecount:speciality="Pediatrics";
    elif ocount>ecount:speciality="Orthopedics";
    else:speciality="ENT";
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[101,'P',102,'O',302,'P',305,'P']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)