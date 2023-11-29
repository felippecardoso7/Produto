# Produto instruções

# Estrutura do produto
Produto ={'Descrição': '', 'Preço':0.0, 'Quantidade':0.0, 'Disponivel': False}

 # Entrada
 print('\n\t\t\t -- Produto do Mercado --\n')
 Produto['Nome'] =input('informe o nome: ')
 Produto['Preço'] =float(input(('informe o Preço')))
 Produto['Quantidade'] =float(input(('informe a Quantidade')))
 Produto['Disponivel'] = False

# Processamento
total = 'Preço'+'Quantidade'


 # Saida
print(f'Nome......{Produto["Nome"]}')
print(f'Preço......{Produto["Preço"]}')
print(f'Quantidade......{Produto["Quantidade"]}')
print(f'Disponivel Ativo......{Produto["Ativo"]}')
print(f'Produto + Quantidade  = total')

