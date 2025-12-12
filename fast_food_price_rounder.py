from num2words import num2words

food01 = float(input("Food Price1: "))
food02 = float(input("Food Price2: "))
food03 = float(input("Food Price3: "))

natija = food01 + food02 + food03

yaxlit = round(natija, 1)

print(f'natija: ${natija:.2f}')
print({num2words(natija, lang='en', to='currency', currency='USD')})
print({num2words(natija, lang='ru', to='currency', currency='USD')})

print(f'Yaxlitlangan narx: ${yaxlit:.2f}')
print({num2words(yaxlit, lang='en', to='currency', currency='USD')})
print({num2words(yaxlit, lang='ru', to='currency', currency='USD')})
