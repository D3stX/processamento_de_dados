import sys
import Nexxees

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python nomeDaApp.py arquivo_entrada.xlsx relatorio_gerado.csv")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        Nexxees.main(input_file, output_file)
