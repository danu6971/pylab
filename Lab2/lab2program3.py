def count_vowels(s):
    
    vowels = "aeiouAEIOU" 
    count = 0  
    for char in s:  
        if char in vowels:  
            count += 1 
    return count  

print(count_vowels("Hello World"))
print(count_vowels("Python"))
print(count_vowels("Beautiful Day"))
