#Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "". A string is palindromic if it reads the same forward and backward.
def first_palindromic_string(words):
    for word in words:
        if word == word[::-1]:  # Check if the word is a palindrome
            return word
    return ""  # Return an empty string if no palindrome is found

# Test with example input
words = ["abc", "car", "ada", "racecar", "cool"]
print(first_palindromic_string(words))

Output: "ada"
