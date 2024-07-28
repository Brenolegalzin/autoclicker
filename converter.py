from cx_Freeze import setup, Executable

# Configuração básica do cx_Freeze
setup(
    name="Autoclicker",
    version="0.1",
    description="Autoclicker com interface Tkinter",
    executables=[Executable("autoclicker.py")]
)
