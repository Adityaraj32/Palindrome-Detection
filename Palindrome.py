# function which reverse the string

def isPalindrome():
    while True:
        palindrome = input("Enter the palindrome: ")
        if palindrome == palindrome[::-1]:
            print("Yes, this is a palindrome")
        else:
            print("No, this is not a palindrome\n")
        
        exit_not = input("Do you want to exit yes or no?: ")
        if exit_not == "yes" or exit_not == "Yes" :
            break
        else:
            continue

# running the function

isPalindrome()()