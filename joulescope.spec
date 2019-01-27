# -*- mode: python -*-

# Configuration file for PyInstaller
# See https://pyinstaller.readthedocs.io/en/stable/index.html
# > pip install pyinstaller
# > pyinstaller joulescope.spec

import sys
import ctypes.util
import os

block_cipher = None
specpath = os.path.dirname(os.path.abspath(SPEC))

if sys.platform.startswith('win'):
    EXE_NAME = 'joulescope'
    BINARIES = [  # uses winusb which comes with Windows
        ('C:\\Windows\\System32\\msvcp100.dll', '.'),
        ('C:\\Windows\\System32\\msvcr100.dll', '.'),
    ]
elif sys.platform.startswith('darwin'):
    EXE_NAME = 'joulescope_launcher'
    BINARIES = [(ctypes.util.find_library('usb-1.0'), '.')]
else:
    EXE_NAME = 'joulescope_launcher'
    BINARIES = []  # sudo apt install libusb-1

a = Analysis(['joulescope_ui/__main__.py'],
             pathex=[],
             binaries=BINARIES,
             datas=[('joulescope_ui/config_def.json5', 'joulescope_ui')],
             hiddenimports=['secrets', 'numpy.core._dtype_ctypes'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['matplotlib', 'scipy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=EXE_NAME,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='joulescope_ui/resources/icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='joulescope')

if sys.platform.startswith('darwin'):
    # https://blog.macsales.com/28492-create-your-own-custom-icons-in-10-7-5-or-later
    # iconutil --convert icns joulescope_ui/resources/icon.iconset
    # hdiutil create ./dist/joulescope.dmg -srcfolder ./dist/joulescope.app -ov
    app = BUNDLE(coll,
                 name='joulescope.app',
                 icon='joulescope_ui/resources/icon.icns',
                 bundle_identifier=None,
                 info_plist={
                     'CFBundleVersion': '0.2.1',
                 })
