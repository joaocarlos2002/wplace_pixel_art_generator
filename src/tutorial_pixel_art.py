import os
import keyboard

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
    "dark purple": [40, (48, 25, 52)],
    "purple": [41, (128, 0, 128)],
    "light purple": [42, (204, 153, 255)],
    "dark pink": [43, (255, 105, 180)],
    "pink": [44, (255, 192, 203)],
    "light pink": [45, (255, 182, 193)],
    "light peach": [48, (255, 229, 180)],
    "dark brown": [49, (101, 67, 33)],
    "brown": [50, (165, 42, 42)]
}

num_to_nome = {v[0]: k for k, v in cores.items()}

def tutorial_pixel_art(txt_path):
    with open(txt_path, 'r') as f:
        linhas = f.readlines()
    matriz = [linha.strip().split() for linha in linhas]
    total = sum(len(linha) for linha in matriz)
    idx = 0
    bloco = 10
    while 0 <= idx < total:
        pixels_info = []
        for i in range(idx, min(idx+bloco, total)):
            pos = i
            y = 0
            while pos >= len(matriz[y]):
                pos -= len(matriz[y])
                y += 1
            x = pos
            valor = matriz[y][x]
            cor_nome = num_to_nome.get(int(valor), 'cor desconhecida')
            pixels_info.append(f"[{i+1}] Linha {y+1}, Coluna {x+1}: {cor_nome} (cor {valor})")
        barra_len = 30
        progresso = int((idx+bloco)/total * barra_len)
        barra = '[' + '#' * min(progresso, barra_len) + '-' * max(barra_len - progresso, 0) + f'] {min(idx+bloco, total)}/{total}'
        print("\n================ PIXEL ART TUTORIAL ================")
        print(barra)
        print(f"Próximos {bloco} pixels:")
        print("---------------------------------------------------")
        for info in pixels_info:
            print(info)
        print("---------------------------------------------------")
        print("Pressione Enter para avançar, Backspace para voltar, Esc para sair.")
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'enter':
                    idx += bloco
                    break
                elif event.name == 'backspace':
                    idx = max(0, idx-bloco)
                    break
                elif event.name == 'esc':
                    print("Saindo do tutorial...")
                    return
        os.system('cls' if os.name == 'nt' else 'clear')


