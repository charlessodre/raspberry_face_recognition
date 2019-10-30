# *** EM DESENVOLVIMENTO ***
# Reconhecimento Facial com Raspberry

<p>O objetivo deste projeto é realizar alguns estudos/testes na área de visão computacional, especialmente em reconhecimento facial, utilizando o raspberry pi 3b. </p>

<p>Neste projeto vamos utilizar o módulo face_recognition.</p>

<p>O módulo está disponível no github do criador: </p>

<p>https://github.com/ageitgey/face_recognition<p>

## Informação sobre os arquivos:

<p>helper.py - Funções de suporte diversas.<p>

## Estrutura dos diretórios:

<p>source_img/known_people - Neste diretório ficam as imagens das pessoas conhecidas. A imagem deve conter somente o rosto da pessoa (um rosto). O nome do arquivo da imagem deve ser o nome da pessoa seguido do caractere "#". Todo o texto que estiver antes do "#" será o nome utilizado para a classificação do rosto.</p>
<p>Exemplo nome do arquivo: </p>
	<p>charles#.jpeg</p>
	<p>charles_sodre#.jpeg</p>
	<p>charles_sodre#_001.jpeg</p>

<p>source_img/unknown - Neste diretório ficam as imagens das pessoas desconhecidas. A imagem pode conter vários rostos, pois verificar se existe algum rosto conhecido (informado no diretório source_img/known_people).</p>

<p>source_img/output - Neste diretório é onde será salva a imagem informando se reconheceu ou não o rosto. Os rostos que não possuírem um retângulo significa que o não foi identificado como um rosto.</p>

