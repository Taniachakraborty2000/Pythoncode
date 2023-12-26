String="To change the overall look of your document. To change the look available in  the gallery"
word_count={}#initializing a dictionary
words=String.split() #split the string into words
for word in words:
    word=word.lower()#convert word in lower case so that it can treat 'to and'To' as a same word
    word_count[word]=word_count.get(word,0)+1#count the occurrence of each word
for word,count in word_count.items():
    print(f"{word}:{count}")#print the word count