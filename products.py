products = []
while True:
	name = input('please enter name of product:')
	if name == 'q':
		break
	price = input('please enter price:')
	products.append([name, price])
print(products)

for p in products:
	print('the price of', p[0], 'is', p[1])