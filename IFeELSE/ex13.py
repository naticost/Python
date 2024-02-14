sal=float(input('digite seu salário: R$ '))
Tv=float(input('digite o valor de vendas: R$'))
comi = Tv+(Tv*3/100)
if comi>1500:
  comi=comi+(comi*5/100)
Tsal = comi+sal
print(Tsal)