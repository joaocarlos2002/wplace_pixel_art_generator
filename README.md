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

- Caminho da imagem
- Tamanho desejado (ex: 16 para 16x16)
- Se quer modo preto/cinza
- Se quer gerar camadas

O resultado será salvo na pasta `camadas`.

### 3. Tutorial passo a passo

Escolha a opção 2 no menu e informe o caminho do arquivo txt gerado (ex: `camadas/pixel_art.txt`). O terminal irá te guiar pixel a pixel.

## Observações

- O script funciona tanto com CPU quanto GPU (detecta automaticamente).
- Para modo preto/cinza, são usados todos os tons de cinza do dicionário.

## Dúvidas ou problemas?

Abra uma issue ou peça ajuda!
