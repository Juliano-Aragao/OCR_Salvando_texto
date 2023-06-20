import os
import pytesseract
import cv2

img_text = cv2.imread("img/texto_1.png")

qualy = '--oem 3 --psm 6'

result = pytesseract.image_to_string(img_text, config=qualy)

# o argumento +a,  comporta para que possa ir salvando o texto abaixo de texto,  se utilizar "w"  ele sobrescreve o arquivo
with open('texto.txt', 'a+') as arquivo:
    arquivo.write(result)

print(result)

# visualizar a imagem do texto
cv2.imshow("Texto", img_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
