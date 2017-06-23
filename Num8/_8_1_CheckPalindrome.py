def main():
    str=input("enter a string\n")
    isPalindrome=True
    for i in range(0,len(str)):
        print(i)
        if str[i]!=str[len(str)-i-1]:

            isPalindrome=False
            break;

    print(str,"is Palindrome?",isPalindrome)

main()