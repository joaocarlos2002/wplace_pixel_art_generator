from src.WPlaceBot import extrair_cores
from src.tutorial_pixel_art import tutorial_pixel_art

MENU = '''\n==== MENU PIXEL ART ====
1 - Gerar pixel art (WPlaceBot)
2 - Tutorial passo a passo
0 - Sair
=======================\n'''

def main():
    while True:
        print(MENU)
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            img_path = input('Caminho da imagem: ')
            tamanho = int(input('Tamanho (ex: 16 para 16x16): '))
            modo_pb = input('Preto e branco/cinza? (s/n): ').lower() == 's'
            gerar_camadas = input('Gerar camadas? (s/n): ').lower() == 's'
            extrair_cores(img_path, tamanho=(tamanho, tamanho), preto_e_branco=modo_pb, gerar_camadas=gerar_camadas)
        elif opcao == '2':
            import os
            base_dir = os.path.dirname(os.path.abspath(__file__))
            txt_path = os.path.join(base_dir, 'src', 'camadas', 'pixel_art.txt')
            print(f'Usando arquivo padrão: {txt_path}')
            tutorial_pixel_art(txt_path)
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    main()
