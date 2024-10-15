#Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "". A string is palindromic if it reads the same forward and backward.
def firstpal(word):
    for i in word:
        if(pal(i)):
            return i
def pal(s):
    return s==s[::-1]
word=["abc", "car", "ada", "racecar", "cool"]
print(firstpal(word))

Output: "ada"
