v=['a','e','i','o','u','A','E','I','O','U']
w=input("Enter the word:")
s=[i for i in w if i in v]
print(s)
print("number of vowels:",len(s)) 
