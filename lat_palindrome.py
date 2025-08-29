def is_palindrome(kata):
    kata = kata.lower().replace(" ", "")
    return kata == kata[::-1]
teks = input("masukan kata: ")
if is_palindrome(teks):
    print("Palindrome")
else:
    print("Not palindrome")