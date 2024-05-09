import pandas as pd
import logging
import sys

# Configuração do logger
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main(input_file, output_file):
    try:
        # Carregar dados do arquivo Excel
        df = pd.read_excel(input_file)
        
        # Renomear colunas
        column_names = ['Nome Empresa', 'Numero Incricao Empresa', 'Nome Banco', 'Nome da Rua',
                        'Numero do Local', 'Cidade', 'Estado', 'Forma Lancamento', 'Nome Favorecido',
                        'Data Pagamento', 'Valor Pagamento', 'Numero Documento']
        df.columns = column_names
        
        # Ordenar os registros
        df.sort_values(by='Numero Incricao Empresa', inplace=True)
        
        # Traduzir siglas dos estados
        estados = {'SC': 'Santa Catarina', 'SP': 'São Paulo', 'RJ': 'Rio de Janeiro'}  # Adicione mais estados conforme necessário
        df['Estado'] = df['Estado'].map(estados).fillna(df['Estado'])  # Mantém o valor original se não estiver na lista de estados

        # Converter datas para o formato especificado
        df['Data Pagamento'] = df['Data Pagamento'].dt.strftime('%d/%B/%Y')

        # Formatar valores
        df['Valor Pagamento'] = df['Valor Pagamento'].apply(lambda x: '{:,.2f}'.format(float(x)) if isinstance(x, (int, float)) else x)

        # Salvar o resultado no arquivo CSV de saída
        df.to_csv(output_file, index=False, sep=';')

        logging.info('Arquivo CSV gerado com sucesso.')
    except Exception as e:
        logging.error(f'Ocorreu um erro: {str(e)}')

if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)
    else:
        print("Uso: python nomeDaApp.py arquivo_entrada.xlsx relatorio_gerado.csv")
