from num2words import num2words

money = int(input("Pul miqdorini kiriting ($): "))

money50 = money // 50
qoldiq = money % 50

money10 = qoldiq // 10
qoldiq = qoldiq % 10

money5 = qoldiq // 5
qoldiq = qoldiq % 5

money1 = qoldiq  

print(f'$50 kupyuradan: {money50} ta')
print(f'$10 kupyuradan: {money10} ta')
print(f'$5 kupyuradan: {money5} ta')
print(f'$1 kupyuradan: {money1} ta')

print(f'Umumiy summa: ${money}')
print({num2words(money, lang='en')}, {num2words(money, lang='ru')})
