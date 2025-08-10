
from PIL import Image
import os
import torch

cores = {
    "black": [1, (0, 0, 0)],
    "dark gray": [2, (169, 169, 169)],
    "gray": [3, (128, 128, 128)],
    "medium gray": [4, (192, 192, 192)],
    "light gray": [5, (211, 211, 211)],
    "white": [6, (255, 255, 255)],
    "deep red": [7, (139, 0, 0)],
    "dark red": [8, (128, 0, 0)],
    "red": [9, (255, 0, 0)],
    "light red": [10, (255, 102, 102)],
    "dark orange": [11, (255, 140, 0)],
    "orange": [12, (255, 165, 0)],
    "gold": [13, (255, 215, 0)],
    "yellow": [14, (255, 255, 0)],
    "light yellow": [15, (255, 255, 224)],
    "dark goldenrod": [16, (184, 134, 11)],
    "goldenrod": [17, (218, 165, 32)],
    "light goldenrod": [18, (238, 221, 130)],
    "dark olive": [19, (85, 107, 47)],
    "olive": [20, (128, 128, 0)],
    "light olive": [21, (192, 255, 62)],
    "dark green": [22, (0, 100, 0)],
    "green": [23, (0, 128, 0)],
    "light green": [24, (144, 238, 144)],
    "dark teal": [25, (0, 128, 128)],
    "teal": [26, (0, 128, 128)],
    "light teal": [27, (178, 255, 255)],
    "dark cyan": [28, (0, 139, 139)],
    "cyan": [29, (0, 255, 255)],
    "light cyan": [30, (224, 255, 255)],
    "dark blue": [31, (0, 0, 139)],
    "blue": [32, (0, 0, 255)],
    "light blue": [33, (173, 216, 230)],
    "dark indigo": [34, (75, 0, 130)],
    "indigo": [35, (75, 0, 130)],
    "light indigo": [36, (100, 100, 255)],
    # "dark slate blue": [37, (72, 61, 139)],
    # "slate blue": [38, (106, 90, 205)],
    # "light slate blue": [39, (132, 112, 255)],
    "dark purple": [40, (48, 25, 52)],
    "purple": [41, (128, 0, 128)],
    "light purple": [42, (204, 153, 255)],
    "dark pink": [43, (255, 105, 180)],
    "pink": [44, (255, 192, 203)],
    "light pink": [45, (255, 182, 193)],
    # "dark peach": [46, (255, 218, 185)],
    # "peach": [47, (255, 229, 180)],
    "light peach": [48, (255, 229, 180)],
    "dark brown": [49, (101, 67, 33)],
    "brown": [50, (165, 42, 42)],
    # "light brown": [51, (222, 184, 135)],
    # "dark tan": [52, (144, 124, 100)],
    # "tan": [53, (210, 180, 140)],
    # "light tan": [54, (238, 221, 130)],
    # "dark beige": [55, (245, 222, 179)],
    # "beige": [56, (255, 228, 196)]
    # "light beige": [57, (255, 239, 204)],
    # "dark stone": [58, (123, 104, 83)],
    # "stone": [59, (181, 101, 29)],
    # "light stone": [60, (204, 204, 204)],
    # "dark slate": [61, (72, 61, 139)],
    # "slate": [62, (106, 90, 205)],
    # "light slate": [63, (132, 112, 255)],
}

def extrair_cores(imagem_path, tamanho=(50, 50), preto_e_branco=False, gerar_camadas=True):

    img = Image.open(imagem_path)
    pixel_art = img.resize(tamanho, Image.NEAREST)
    largura, altura = tamanho
    if preto_e_branco:
        pixel_art = pixel_art.convert('L') 
        pixel_art = pixel_art.convert('RGB')
        gray_keys = ['black', 'dark gray', 'gray', 'medium gray', 'light gray', 'white']
        bw_cores = {k: v for k, v in cores.items() if k in gray_keys}
        cor_lista = [v[1] for v in bw_cores.values()]
        cor_nums = [v[0] for v in bw_cores.values()]
    else:
        pixel_art = pixel_art.convert('RGB')
        cor_lista = [v[1] for v in cores.values()]
        cor_nums = [v[0] for v in cores.values()]
    pixels = torch.tensor(pixel_art.getdata(), dtype=torch.float32, device='cuda')
    camadas = []
    pasta_camadas = os.path.join(os.path.dirname(__file__), 'camadas')
    if not os.path.exists(pasta_camadas):
        os.makedirs(pasta_camadas)
    cor_tensor = torch.tensor(cor_lista, dtype=torch.float32, device='cuda')
    cor_nums_tensor = torch.tensor(cor_nums, dtype=torch.int32, device='cuda')

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    pixels = torch.tensor(pixel_art.getdata(), dtype=torch.float32, device=device)
    cor_tensor = torch.tensor(cor_lista, dtype=torch.float32, device=device)
    cor_nums_tensor = torch.tensor(cor_nums, dtype=torch.int32, device=device)

    dist = torch.cdist(pixels.unsqueeze(0), cor_tensor.unsqueeze(0)).squeeze(0)
    min_indices = torch.argmin(dist, dim=1) 
    cor_final = cor_tensor[min_indices].to('cpu')
    cor_num_final = cor_nums_tensor[min_indices].to('cpu')

    matriz_numeros = []
    for linha in range(altura):
        camada = Image.new('RGBA', tamanho, (0, 0, 0, 0))
        linha_numeros = []
        for x in range(largura):
            i = linha * largura + x
            cor_valor = tuple(int(v.item()) for v in cor_final[i])
            camada.putpixel((x, linha), cor_valor + (255,))
            linha_numeros.append(int(cor_num_final[i].item()))
        if gerar_camadas:
            caminho_camada = os.path.join(pasta_camadas, f'camada_linha_{linha+1}.png')
            camada.save(caminho_camada)
            camadas.append(camada)
            print(f'Camada linha {linha+1} salva em {caminho_camada}.')
        matriz_numeros.append(linha_numeros)

    imagem_final = Image.new('RGBA', tamanho, (0, 0, 0, 0))
    if gerar_camadas:
        for camada in camadas:
            imagem_final = Image.alpha_composite(imagem_final, camada)
    else:
        for linha in range(altura):
            for x in range(largura):
                i = linha * largura + x
                cor_valor = tuple(int(v.item()) for v in cor_final[i])
                imagem_final.putpixel((x, linha), cor_valor + (255,))

    imagem_final.save(os.path.join(pasta_camadas, 'imagem_final.png'))
    print(f'Imagem final salva em {os.path.join(pasta_camadas, "imagem_final.png")}.')

    txt_path = os.path.join(pasta_camadas, 'pixel_art.txt')
    with open(txt_path, 'w') as f:
        for linha in matriz_numeros:
            f.write(' '.join(str(num) for num in linha) + '\n')
    print(f'Matriz de pixels salva em {txt_path}.')

# extrair_cores("C:\\Users\\joao_\\OneDrive\\Desktop\\teste1234567.jpg", tamanho=(150, 150), preto_e_branco=True, gerar_camadas=False)