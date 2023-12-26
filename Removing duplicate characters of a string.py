Input="String and String Function"#given string
words=Input.split()#split the input string into a list of words
unique_words=[]#create an emplty list to store unique words
for word in words:#iterate through each word in the list
    if word not in unique_words:#if not, add it to the unique_words list
        unique_words.append(word)
        result_string=" ".join(unique_words)#join the unique_words list into astring using space as a seperator
print( "Output:",result_string)#Output: String and Function