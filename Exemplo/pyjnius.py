from jnius import autoclass

# Carregar as classes necessárias do Android
PythonActivity = autoclass('org.kivy.android.PythonActivity')
AudioManager = autoclass('android.media.AudioManager')

# Criar uma instância do objeto AudioManager
audio_manager = PythonActivity.mActivity.getSystemService(PythonActivity.AUDIO_SERVICE)

# Função para abaixar o volume
def abaixar_volume():
    audio_manager.adjustVolume(AudioManager.ADJUST_LOWER, AudioManager.FLAG_SHOW_UI)

# Função para verificar se a senha está correta
def verificar_senha(senha):
    if senha == "adx":
        return True
    else:
        return False

# Loop para aguardar comandos de voz
while True:
    comando = input("Digite um comando de voz: ")

    # Verificar se a senha está correta antes de executar os comandos
    if verificar_senha(comando):
        if comando == "abaixar volume":
            abaixar_volume()
        else:
            print("Comando não reconhecido.")
    else:
        print("Senha incorreta.")