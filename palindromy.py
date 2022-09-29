word = input("Wprowadź słowo: ")

def is_palindrome(word):
    palindrom = word[::-1]
    return True if palindrom == word else False


print(is_palindrome(word))



