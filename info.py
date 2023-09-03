# Importe a biblioteca
import openpyxl 

# Carregar o arquivo
book = openpyxl.load_workbook('Planilha de frutas.xlsx')

# Selecionar a página da planilha
frutas_page = book['Frutas']

# Imprimir os dados da planilha 
for rows in frutas_page.iter_rows(min_row=2, max_row=7):
    for cell in rows:
        if cell.value == 'Abacaxi':
            cell.value = 'Kiwi'

book.save('Planilha alterada.xlsx')


