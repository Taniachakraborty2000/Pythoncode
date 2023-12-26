def Read_linebyline():#defining function 
    with open("ABC.txt","r") as file:#opening the given file as read mode and named as file and using with the file will autoclosed after complete performing
        for line in file:
            print(line.strip())#print every line without trailing and leading  spaces(whitespace)
Read_linebyline()#function calling