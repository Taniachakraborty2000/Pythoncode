String="Welcome to Python Training"
Vowels="aeiouAEIOU"

Vowel_counts={}#Initialize an empty dictionary to store vowel counts
for char in String:
    if char in Vowels:
        
        Vowel_counts[char]=Vowel_counts.get(char,0)+1 
        #check if the character is vowel.
        #if the vowel is already in the dictionary,increment its count by 1.
        #if the vowel is not in the dictionary,add it with a count of 1
print("vowel counts",Vowel_counts)
for Vowel,count in Vowel_counts.items():
    print(f"{Vowel}{count}")

    
       
