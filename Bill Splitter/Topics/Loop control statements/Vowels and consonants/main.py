from string import ascii_lowercase
line = input()
vowels = "aeiou"
for char in line:
    if char in ascii_lowercase:
        print("vowel" if char in vowels else "consonant")
    else:
        break
