product = {
    'name': 'iPhone 12',
    'stock': 24,
    'price': 65432.1
}
print(product)
print(len(product))

product['memory'] = 1024
print(product)

product['name'] = 'iPhone 12 Pro'
print(product)

print(product['name'])

print(product.get('memory'))

print(product.get('discount', 'Rus'))

print(product)

del product['stock']
print(product)