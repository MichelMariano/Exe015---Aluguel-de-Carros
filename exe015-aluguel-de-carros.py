# alugado e a quantidade de dias pelos quais foram alugado. Calcule o preço a pagar.
# Sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.



dias = int(input('Quantos dias Alugado? '))
km = float(input('Quantos KM Rodados? '))
pagar = (dias * 60) + (km * 0.15)

print('='*36)

print('Você percorreu {:.0f} Km. \nO Total a pagar é de R$: {:.2f}'.format(km, pagar))

print('='*36)
