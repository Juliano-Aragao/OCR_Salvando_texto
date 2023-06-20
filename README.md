# OCR_Salvando_texto

# Instalaçao no Linux
sudo apt-get update
sudo apt-get install tesseract-ocr-por

# OEM 3
Significa “Motor de reconhecimento do OCR” em inglês e controla o mecanismo subjacente usado para realizar o OCR. O valor padrão é 3, que representa um mecanismo de OCR baseado em LSTM treinado com dados de imagem e texto.

# PSM 6
Significa “Modo de segmentação de página” em inglês e controla como o PyTesseract segmenta o texto da imagem original. O valor padrão é 3, que é “Totalmente automático, mas com orientação vertical limitada”. O valor 6 é “Assume um único bloco de texto vertical na imagem”. Em outras palavras, o PSM 6 é útil quando se tem um único bloco de texto vertical na imagem, como um texto em uma página de um livro

# with open('texto.txt', 'a+') as arquivo:
O argumento +a,  comporta para que possa ir salvando o texto abaixo de texto,  se utilizar "w"  ele sobrescreve o arquivo
