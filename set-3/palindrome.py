def isPalindrome(string):
    copy_string = string
    reversed_string = string[::-1]
    if (copy_string == reversed_string):
        print(f"{string} is palindrome!")
    else:
        print(f"{string} is not palindrome!")


isPalindrome("madam")
isPalindrome("rahul")
isPalindrome("jahaj")
