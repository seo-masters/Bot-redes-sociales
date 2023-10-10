# app.spec

block_cipher = None

a = Analysis(
    ["app/app.py"],
    pathex=["app/"],  # Reemplaza con la ruta a tu proyecto
    binaries=[],
    datas=[
        ("aut.png", "."),
        ("photo.jpg", "."),
        ("config/*", "config"),
        ("app/controller/*", "controller"),
        ("app/database/*", "database"),
        ("app/gui/*", "gui"),
        ("app/models/*", "models"),
        ("output_directory/*", "output_directory"),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="app",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    exclude_binaries=True,
)
