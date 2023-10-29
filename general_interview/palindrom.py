def ispalindrome(string):
    string = string.lower()
    first,last = 0,len(string)-1
    while(first<last):
        if (string[first] == string[last]):
            first+=1
            last-=1
        else:
            return "The string is not palindrome"
        return "The String is Palindrome"
    
print(ispalindrome("Malayalam"))