# FaceLite
Uma versão minimalista do facebook para desktop.


#### Requisitos

Os pacotes que utilizei no programa são PyQt5, sys, e os, primeiro de tudo, deve ter o python 3 instalado, funciona tanto no [Windows](https://python.org.br/instalacao-windows/), quanto no [Linux](https://python.org.br/instalacao-linux/), tambem precisa do [pip](http://excript.com/blog/gerenciador-pacotes-python-pip.html), para intalar as dependencias:

##### No Windows
> python -m pip3 install -r requeriments.txt

##### No linux
> pip3 install -r requeriments.txt

Para executa-lo no windows, de forma rapida, depois de instalar as dependencias e o script, clique com botão direito no arquivo "FaceLite.py" e vai em Enviar para>Área de trabalho, assim vai criar um atalho, logo va nas propriedades do atalho, na aba atalho>destino, vá até o inicio do texto e coloque "python", em seguida o local do script, no meu caso ficou assim:
> python "C:\Users\w7\Python\FaceLite/FaceLite.py"

No linux, você pode criar um shell script que inicie ele, logo criar um .desktop e coloca-lo na Área de trabalho, então: obs; utilize seu editor favorito, no meu caso é o nano então:
> sudo nano /usr/bin/flite

Em seguida vai abrir seu editor, dai você coloca o codigo:
>#!/bin/bash

> cd "local onde baixou o script"

> ./FaceLite.py
  
Agora para criar o .desktop devemos ir para:
> cd  /usr/share/applications

logo criamos e editamos um arquivo .desktop:
> sudo nano FaceLite.desktop

Em seguida colocamos as infos do programa.

>[Desktop Entry]

>Type=Application

>Encoding=UTF-8

>Name=FaceLite

>Comment=" "

>Exec=flite

>Icon=/home/user/Downloads/FaceLite/icons/face.png

>Terminal=false

>Categories=Network;

Assim que salvar o arquivo basta ir no seu menu na categoria Internet que vai encontra-lo lá. OBS: na parte Icon, eu coloquei um exemplo, você deve por o local do seu download.
