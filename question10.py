def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(s.split()).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("madam"))
print(is_palindrome("nurses run"))
print(is_palindrome("breakfast"))
print(is_palindrome("mahaham"))