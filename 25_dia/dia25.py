caracteres = {}
cadena = input('Introduce una cadena > ')
for c in cadena:
    caracteres[c] = caracteres.get(c, 0) + 1
print('\n'.join([f'{k}: {v}' for k, v in caracteres.items()]))


sales = {'apple': 2, 'orange': 3, 'grapes': 4}
for x, y in sales.items():
    print(f'{x} : {y}')

sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)
for item in sorted_sales:
    print(item)
print(sorted_sales)
