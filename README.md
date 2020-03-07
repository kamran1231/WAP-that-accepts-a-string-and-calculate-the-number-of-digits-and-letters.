# WAP-that-accepts-a-string-and-calculate-the-number-of-digits-and-letters.

str1 = input('Enter the string: ')
count_letters = 0
count_digit = 0
for i in str1:
    if i.isalpha():
        count_letters += 1
    
    elif i.isdigit():
        count_digit += 1
print('total_digit',count_digit)
print('total_letters',count_letters)
