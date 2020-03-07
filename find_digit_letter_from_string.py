

str1 = input('Enter the string: ')
count_letters = 0
count_digit = 0
for i in str1:
    if i.isalpha():
        count_letters += 1

    elif i.isdigit():
        count_digit += 1
print('Total digits',count_digit)
print('Total letters',count_letters)