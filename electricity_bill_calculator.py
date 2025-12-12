from num2words import num2words 

oy_boshi = float(input('dastlabki korsatkich: '))
oy_oxiri = float(input('oxirgi korsatgich: '))

narx_1kWh = 0.45

result = (oy_oxiri - oy_boshi )*narx_1kWh

print(f'result: ${result:.2f}')
print(num2words(result, lang='en'))
print(num2words(result, lang='ru'))
