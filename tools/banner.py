# Gera o docs/banner.png — o cabeçalho do README.
#
# As cores não foram escolhidas: foram AMOSTRADAS dos screenshots do
# produto (docs/dashboard-web.png), então o banner é a identidade do app
# e não uma arte paralela que diverge dele com o tempo.
#
#   #18181B  fundo do app
#   #1F1F22  cartão
#   #40E0D0  acento (botão "Nova vaga")
import math, os
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 340
BG    = (24, 24, 27)
TEAL  = (64, 224, 208)
TXT   = (250, 250, 250)
TXT_2 = (161, 161, 170)
RAIZ  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

base = Image.new('RGB', (W, H), BG)

# ---- Brilho teal --------------------------------------------------------
# Calculado pequeno e ampliado: um borrão de 160x43 vira degradê liso em
# 1280x340 e custa uma fração do tempo de percorrer o tamanho final.
def brilho(cx, cy, rx, ry, cor, forca):
    pw, ph = 160, 43
    mask = Image.new('L', (pw, ph), 0)
    px = mask.load()
    for y in range(ph):
        for x in range(pw):
            dx, dy = (x / pw - cx) / rx, (y / ph - cy) / ry
            d = math.sqrt(dx * dx + dy * dy)
            if d < 1:
                # cosseno em vez de linear: a borda some sem deixar o anel
                # visível que um degradê linear cria.
                px[x, y] = int(forca * 255 * (0.5 + 0.5 * math.cos(math.pi * d)))
    base.paste(Image.new('RGB', (W, H), cor), (0, 0), mask.resize((W, H), Image.BICUBIC))

brilho(0.80, 0.10, 0.52, 0.95, TEAL, 0.16)
brilho(0.14, 0.95, 0.44, 0.80, TEAL, 0.09)

d = ImageDraw.Draw(base)

# ---- Malha ---------------------------------------------------------------
for x in range(0, W, 64):
    d.line([(x, 0), (x, H)], fill=(31, 31, 34), width=1)
for y in range(0, H, 64):
    d.line([(0, y), (W, y)], fill=(31, 31, 34), width=1)

# ---- Conteúdo ------------------------------------------------------------
titulo  = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', 82)
tagline = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', 25)

def centro(txt, fonte, y, cor):
    w = d.textbbox((0, 0), txt, font=fonte)[2]
    d.text(((W - w) / 2, y), txt, font=fonte, fill=cor)

# Fio de acento acima do nome, na cor do botão principal do app.
d.rectangle([(W - 64) / 2, 84, (W + 64) / 2, 87], fill=TEAL)

centro('TrampoCerto', titulo, 116, TXT)
centro('Construction hiring, end to end.', tagline, 232, TXT_2)

saida = os.path.join(RAIZ, 'docs', 'banner.png')
base.save(saida, 'PNG', optimize=True)
print('gerado:', saida, base.size, os.path.getsize(saida) // 1024, 'KB')
