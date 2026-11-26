import urllib.request
import ssl
import os
import re

# Desabilita verificação SSL (certificado expirado no servidor)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE_URL = 'https://www.proservsystems.com.br'

# Lista de todas as imagens referenciadas nos HTML
html_images = [
    # index.html
    '/images/banner.jpg',
    '/images/servicos/portaria.png',
    '/images/servicos/limpeza.png',
    '/images/servicos/zeladoria.png',
    '/images/carro-proserv.jpg',
    '/images/icons/whatsapp.png',
    '/images/logo-g-b.png',
    '/images/proserv-logo-seo.png',
    '/images/logo-p.png',
    # Favicons
    '/images/favicon/apple-icon-57x57.png',
    '/images/favicon/apple-icon-60x60.png',
    '/images/favicon/apple-icon-72x72.png',
    '/images/favicon/apple-icon-76x76.png',
    '/images/favicon/apple-icon-114x114.png',
    '/images/favicon/apple-icon-120x120.png',
    '/images/favicon/apple-icon-144x144.png',
    '/images/favicon/apple-icon-152x152.png',
    '/images/favicon/apple-icon-180x180.png',
    '/images/favicon/android-icon-192x192.png',
    '/images/favicon/favicon-32x32.png',
    '/images/favicon/favicon-96x96.png',
    '/images/favicon/favicon-16x16.png',
    # contato.html
    '/images/backgrounds/bg-contato.png',
    # quem-somos.html
    '/images/backgrounds/bg-quem_somos.png',
    '/images/sobre/funcionaria.png',
    '/images/sobre/sistema.png',
    '/images/sobre/seguranca.png',
    '/images/sobre/manutencao.png',
    # servicos.html
    '/images/backgrounds/bg-servicos.png',
    '/images/servicos/portaria-d.png',
    '/images/servicos/limpeza-d.png',
    '/images/servicos/zeladoria-d.png',
    # envie-seu-curriculo.html
    '/images/backgrounds/bg-curriculo.png',
    '/images/icons/curriculo.png',
]

# Imagens referenciadas no CSS (style5.css)
css_images = [
    '/images/sprites/logo.png',
    '/images/sprites/contact.png',
    '/images/icons/select.png',
    '/images/sprites/social.png',
    '/images/sprites/atendimento.png',
    '/images/sprites/saiba-mais.png',
    '/images/icons/selo-20_anos.png',
    '/images/sprites/lista-sobre.png',
    '/images/logo-bg.png',
]

# Fontes do Font Awesome
fontawesome_urls = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-brands-400.eot',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-brands-400.woff2',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-brands-400.woff',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-brands-400.ttf',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-brands-400.svg',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-regular-400.eot',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-regular-400.woff2',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-regular-400.woff',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-regular-400.ttf',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-regular-400.svg',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-solid-900.eot',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-solid-900.woff2',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-solid-900.woff',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-solid-900.ttf',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-solid-900.svg',
]

# Fontes do Slick
slick_fonts = [
    'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/fonts/slick.eot',
    'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/fonts/slick.woff',
    'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/fonts/slick.ttf',
    'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/fonts/slick.svg',
]

# Ajax loader do Slick
slick_ajax = 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/ajax-loader.gif'


def download(url, dest_path):
    """Baixa um arquivo de URL para o caminho de destino."""
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
            data = response.read()
        with open(dest_path, 'wb') as f:
            f.write(data)
        print(f'OK: {dest_path} ({len(data)} bytes)')
        return True
    except Exception as e:
        print(f'ERRO: {url} -> {e}')
        return False


# Baixa imagens do HTML
for img in html_images:
    url = BASE_URL + img
    dest = 'proserv' + img
    download(url, dest)

# Baixa imagens do CSS
for img in css_images:
    url = BASE_URL + img
    dest = 'proserv' + img
    download(url, dest)

# Baixa fontes do Font Awesome
for url in fontawesome_urls:
    fname = os.path.basename(url)
    dest = os.path.join('proserv', 'css', 'webfonts', fname)
    download(url, dest)

# Baixa fontes do Slick
for url in slick_fonts:
    fname = os.path.basename(url)
    dest = os.path.join('proserv', 'css', 'fonts', fname)
    download(url, dest)

# Baixa ajax-loader do Slick
download(slick_ajax, os.path.join('proserv', 'css', 'ajax-loader.gif'))

print('\nDownload concluído!')