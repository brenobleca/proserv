import os
import shutil

# Move arquivos de proserv/images/images/ para proserv/images/
src_base = 'proserv/images/images'
dst_base = 'proserv/images'

moved = 0
errors = 0

for root, dirs, files in os.walk(src_base):
    for fname in files:
        src = os.path.join(root, fname)
        rel = os.path.relpath(src, src_base)
        dst = os.path.join(dst_base, rel)
        try:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
            moved += 1
            print(f'Movido: {src} -> {dst}')
        except Exception as e:
            errors += 1
            print(f'ERRO: {src} -> {e}')

# Remove diretórios vazios
for root, dirs, files in os.walk(src_base, topdown=False):
    for d in dirs:
        p = os.path.join(root, d)
        try:
            os.rmdir(p)
        except OSError:
            pass

try:
    os.rmdir(src_base)
except OSError:
    pass

print(f'\nMovidos: {moved}, Erros: {errors}')