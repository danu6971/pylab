def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]  

words = ["madam", "hello", "racecar"]

for word in words:
    if is_palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")
