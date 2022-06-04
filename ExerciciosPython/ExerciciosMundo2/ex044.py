print('Vamos Calcular O Valor do Produto Conforme a Condição de Pagamento.')
preco = float(input('Qual o Valor das Compras ? R$ '))
print('CONDIÇÕES DE PAGAMENTO : "Digite o Numero Desejado" '
      '\n(1) À VISTA (dinheiro/ cheque) - 10% de Desconto'
      '\n(2) À VISTA (no cartão) - 5% de Desconto '
      '\n(3) Em Até 2x no Cartao - Sem Juros'
      '\n(4) 3x ou Mais no Cartão - 20% de Juros')
escolha = int(input('Qual Sua Escolha ?  '))
if escolha == 1:
    print('Com 10% de Desconto O Produto à Vista (dinheiro /cheque) Fica R$ {:.2f} .'.format(preco - preco * 0.10))
elif escolha == 2:
    print('Com 5% de Desconto No Cartão à Vista Fica R$ {:.2f} .'.format(preco - preco * 0.05))
elif escolha == 3:
    print('Parcelando Em até 2x No Cartão Não há juros. '
          '\nO Produto Fica R$ {:.2f} em duas vezes de R$ {:.2f} .'.format(preco, preco / 2))
elif escolha == 4:
    parcela = int(input('Em Quantas Vezes Deseja Parcelar? '))
    print('Parcelando em {}x no Cartão, cobramos 20% de Juros. '
          '\nO Produto Fica R$ {:.2f} em {} parcelas de R$ {:.2f} .'.format(parcela, preco + preco * 0.20, parcela, (preco + preco * 0.20) / parcela))
else:
    print('\033[31;1mOpção Errada ! Tente Novamente!\033[m')
