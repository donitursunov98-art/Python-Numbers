# from num2words import num2words

# harajat1 = float(input('1-kun: '))
# harajat2 = float(input('2-kun: '))
# harajat3 = float(input('3-kun: '))
# harajat4 = float(input('4-kun: '))
# harajat5 = float(input('5-kun: '))
# harajat6 = float(input('6-kun: '))
# harajat7 = float(input('7-kun: '))

# result = (harajat1 + harajat2 + harajat3 + harajat4 + harajat5 + harajat6 + harajat7)/7

# print('result, ${result:.2f}')
# print(result, lang='en', to='currency')
# print(result, lang='ru', to='currency')

from num2words import num2words

harajat1 = float(input('1-kun: '))
harajat2 = float(input('2-kun: '))
harajat3 = float(input('3-kun: '))
harajat4 = float(input('4-kun: '))
harajat5 = float(input('5-kun: '))
harajat6 = float(input('6-kun: '))
harajat7 = float(input('7-kun: '))

result = (harajat1 + harajat2 + harajat3 + harajat4 + harajat5 + harajat6 + harajat7) / 7

print(f'result: ${result:.2f}')
print(num2words(result, lang='en'))
print(num2words(result, lang='ru'))
