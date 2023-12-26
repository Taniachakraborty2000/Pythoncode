input="Welcome to Python Assignment"#given
Vowels="aeiouAEIOU"#vowels
count=0#initialize value
for char in input:
    if char in Vowels:#check if the character of string is in the Vowels or not
        count+=1# if the condition is sattisfy add 1
print(" Output:Total vowels are:",count)# Output:Total vowels are: 8