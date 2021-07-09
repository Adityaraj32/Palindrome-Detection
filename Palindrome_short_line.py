def isPalindrome(s):
    return s == s[::-1]

pail_word = input("Enter the palindrome: ")
result = isPalindrome(pail_word)

if result:
    print("yes,this is a palindrome")
else:
    print("no,this is not a palindrome")