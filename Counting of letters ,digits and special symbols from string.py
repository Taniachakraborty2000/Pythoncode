Input="P@#yn26at^&i5ve"#given string
count_letter=0#initialization of count of letter
count_digit=0#initialization of count of digit
count_symbol=0#initialization of count of symbols
for char in Input:
    if char .isalpha():#check if character is an alphabet or not
        count_letter+=1#add 1 if the charater is a alphabet
    elif char .isdigit():#check if charater is a digit or not
        count_digit+=1#add 1 if the character is a digit
    else:#if  in the previous part the conditon does not hold it comes to else part
        count_symbol+=1#add 1
print("Output:Chars=",count_letter,"Digits=",count_digit,"Symbol=",count_symbol)#Output:Chars= 8 Digits= 3 Symbol= 4