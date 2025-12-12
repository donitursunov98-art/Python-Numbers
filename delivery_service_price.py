from num2words import num2words

tolov = float(input('tolov: '))
masofa = float(input('masofa: '))
km_uchun = 0.80

umum_summa = tolov + masofa*km_uchun

print(f'umum_summa: ${umum_summa:.2f}')
print(num2words(umum_summa, lang='en', to='currency'))
print(num2words(umum_summa, lang='ru', to='currency'))
