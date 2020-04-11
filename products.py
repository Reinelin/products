# Import data
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if 'product,price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)

# user input
products = []
while True:
	name = input('please enter name of product:')
	if name == 'q':
		break
	price = input('please enter price:')
	products.append([name, price])
print(products)

# print price of records
for p in products:
	print('the price of', p[0], 'is', p[1])

# write data
with open('products.csv', 'w') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

