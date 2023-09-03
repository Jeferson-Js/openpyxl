import openpyxl

# Criar a planilha
book = openpyxl.Workbook()

# Criar a página
frutas_page = book.create_sheet("Frutas")

# Criar o rodapé
frutas_page.append(['Frutas', 'Quantidade', 'Preço'])

# Adicionar os valores a cada campo da planilha
frutas_page.append(['Abacaxi', '20', 'R$ 6,00'])
frutas_page.append(['Laranja', '10', 'R$ 1,00'])
frutas_page.append(['Maça', '3', 'R$ 26,00'])
frutas_page.append(['Melancia', '3', 'R$ 46,00'])
frutas_page.append(['Pera', '7', 'R$ 9,00'])
frutas_page.append(['Limão', '2', 'R$ 10,00'])

# Salvar as alterações feitas.
book.save('Planilha de frutas.xlsx')
