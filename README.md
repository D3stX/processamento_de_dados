# Processamento de Dados - App Nexxus

Este programa foi desenvolvido para processar dados de um arquivo Excel e gerar um relatório em formato CSV. Ele segue as especificações fornecidas pela Nexxera.

## Funcionamento

O programa consiste em dois arquivos principais:

1. `nomeDaApp.py`: Este é o ponto de entrada principal para o programa. Ele verifica os argumentos da linha de comando e chama a função `main` do arquivo `Nexxees.py` para processar os dados.

2. `Nexxees.py`: Este arquivo contém a lógica de processamento dos dados. Ele lê o arquivo Excel, realiza o processamento necessário e gera o relatório CSV.

## Como Executar

Para executar o programa, siga estas etapas:

1. Certifique-se de ter o Python instalado no seu sistema.

2. Instale as bibliotecas `pandas` e `openpyxl` se ainda não estiverem instaladas. Você pode instalar usando o pip:

   ```
   pip install pandas openpyxl
   ```

3. Coloque os arquivos `nomeDaApp.py` e `Nexxees.py` no mesmo diretório que o arquivo Excel que você deseja processar.

4. Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão localizados.

5. Execute o seguinte comando na linha de comando:

   ```
   python nomeDaApp.py arquivo_entrada.xlsx relatorio_gerado.csv
   ```

   Substitua `arquivo_entrada.xlsx` pelo nome do seu arquivo Excel de entrada e `relatorio_gerado.csv` pelo nome do arquivo CSV que você deseja gerar.

## Observações

- Certifique-se de que o arquivo Excel de entrada siga o formato esperado pelo programa, com as colunas conforme descritas nas instruções.

- O programa gerará um arquivo de log chamado `app.log` no mesmo diretório onde os arquivos estão localizados, que registra eventos importantes durante a execução do programa.

## Exemplo de Uso

Suponha que você tenha um arquivo Excel chamado `dados.xlsx` com os dados a serem processados e queira gerar um relatório CSV chamado `relatorio.csv`. Para executar o programa, você usaria o seguinte comando:

```
python nomeDaApp.py dados.xlsx relatorio.csv
```

## Autor

Este programa foi desenvolvido por [Seu Nome].

Se encontrar algum problema ou tiver alguma dúvida, sinta-se à vontade para entrar em contato.

