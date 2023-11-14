#    FUNCIONALIDADE NECESSARIA
#
#    1) COLETAR E EXIBIR TITULO DO VIDEO
#
#    2) BAIXAR UM OU MAIS VIDEOS
#
#    3) BAIXAR UM OU MAIS AUDIO
#
#    4) CRIAR PASTA PARA CONTER VIDEOS BAIXADOS
#
#    5) REMOVER VIDEOS MAIORES QUE 3H
#
from __future__ import unicode_literals
import time
import subprocess
import youtube_dl

ydl_opts = {}

lista_link = ['https://youtu.be/m4VFSe2DImo',
                    'https://youtu.be/sarlhUK7hnw',
                    'https://youtu.be/qGCq4wrQhSg']

for link in lista_link:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info( link, download=False)
        print ('\nData de envio : %s' %(meta['upload_date']))
        print ('\nCanal: %s' %(meta['uploader']))
        print ('\nFormato : %s' %(meta['format'])) 
        print ('\nDuração em segundos : %s' %(meta['duration']))
        print ('\nTitulo : %s' %(meta['title']))
        time.sleep(3 )
        subprocess.call('clear', shell= True)
        