## IF, ELSE, ELIF

idade = int(input('Digite sua idade: '))

if idade >= 16 and idade <= 17:
  pŕint('Pode votar ( ͡° ͜ʖ ͡°): ' )
elif idade >= 18:
  print('Pode votar e dirigirヽ(ﾟДﾟ)ﾉ: ')
else:
  print('Não pode votar: ')