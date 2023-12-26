Input="Hell0 W0rld ! 123 * # welcome to pYtHoN"#given string
count_uppercase=0#initialization the number of uppercase
countr_lowercase=0#initialization the number of lowercase
count_specialchar=0#initialization the number of special characters
count_digits=0#initialization the number of numerical values
for char in Input:
    if char .isupper():#check if the character is in uppercase or not
        count_uppercase+=1#add 1 if the character is  in uppercase
    elif char .islower():#check if char is in lowercase or not
        countr_lowercase+=1#add 1 if the character is  in lowercase
    elif char .isdigit():#check if char is a digit or not
        count_digits+=1#add 1 if the character is  digit
    else:
        count_specialchar+=1# if the peivious three conditon does not hold then go to else part and add 1
print(" Output:UpperCase:",count_uppercase,"LowerCase:",countr_lowercase,"NumberCase",count_digits,"SpecialCase",count_specialchar)#Output:UpperCase: 5 LowerCase: 18 NumberCase 5 SpecialCase 11