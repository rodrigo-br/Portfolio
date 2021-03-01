# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/Rodrigo/Desktop/GitHub/Portfolio/Jogo_de_luta_por_turnos/code/avaliacao.py'],
             pathex=['C:\\Users\\Rodrigo\\Desktop\\GitHub\\Portfolio\\Jogo_de_luta_por_turnos\\code'],
             binaries=[],
             datas=[('C:/Users/Rodrigo/Desktop/GitHub/Portfolio/Jogo_de_luta_por_turnos/code/imagens', 'imagens/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='avaliacao',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Rodrigo\\Desktop\\GitHub\\Portfolio\\Jogo_de_luta_por_turnos\\code\\imagens\\icone.ico')
