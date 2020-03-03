qtdLitros= float(input("Digite a quantidade de Litros:\n"))
combustivel= input("Digite o combustivel sendo a= Alcool, d= Diesel e g= Gasolina:\n") 
if combustivel=="a":
    vlrpago=qtdLitros*3.8997
    print("O valor pago pelo Alcool é R$ %.2f" % vlrpago)
elif combustivel=="d":
    vlrpago= qtdLitros*3.6543
    print("O valor pago pelo Diesel é R$ %.2f" % vlrpago)
elif combustivel=="g":
    vlrpago= qtdLitros*4.4009
    print("O valor pago pela Gasolina é R$ %.2f" % vlrpago)
else:
    print("Combustível Inválido!")
