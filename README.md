# Pixel Art Tutorial & Generator

Este projeto permite transformar imagens em pixel art, gerar tutoriais passo a passo e trabalhar com camadas, usando Python e GPU (opcional).

## Requisitos

- Python 3.11 ou 3.10
- pip
- Uma GPU NVIDIA (opcional, para aceleração)

## Instalação

1. **Clone ou baixe o projeto** para uma pasta local.
2. **Crie um ambiente virtual** (recomendado):
   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate
   ```
3. **Instale as dependências:**
   ```powershell
   pip install pillow torch
   ```
   Se quiser usar a GPU, instale o PyTorch com CUDA:
   ```powershell
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
   ```

## Como usar

### 1. Menu interativo

Execute:

```powershell
python main.py
```

### 2. Gerar pixel art

Escolha a opção 1 no menu e informe:

- Caminho da imagem (ex: C:\Users\joao_\OneDrive\Desktop\teste1234567.jpg) o windowns tem uma opção no direito de copy as path
  
<img width="318" height="561" alt="image" src="https://github.com/user-attachments/assets/eef67efd-e8a4-4321-b4f3-4930a8e2a26d" />

- Tamanho desejado (ex: 16 para 16x16)
- Se quer modo preto/cinza
- Se quer gerar camadas

O resultado será salvo na pasta `camadas`.

### 3. Tutorial passo a passo

Escolha a opção 2 no menu. O terminal irá te guiar pixel a pixel.

## Observações

- O script funciona tanto com CPU quanto GPU (detecta automaticamente).
- Para modo preto/cinza, são usados todos os tons de cinza do dicionário.
- Caso tenha alguma cor paga desbloqueada acesse **src/WPlace.py** e descomente a cor desejada
``` Python
cores = {
    "black": [1, (0, 0, 0)], (está sendo usada)
    # "dark gray": [2, (169, 169, 169)], (Não está sendo usada)
```

## Dúvidas ou problemas?

Abra uma issue ou peça ajuda!
