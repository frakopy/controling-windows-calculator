import pyautogui, time
from PIL import Image


'''ORIENTAR AL ROBOT QUE REALICE LA SIGUIENTE OPERACION EN LA CALCULADORA:

-------------------> 12+23=35 <-------------------------------
'''

#Esperamos 3 segundos para tener tiempo de abrir la calculadora y que sea visible en la pantalla para que
#pyautogui.locateCenterOnScreen pueda localizar las coordenadas segun la imagen, en caso contrario que nuestra
#aplicacion (en este caso la calculadora) no sea visible entonces pyautogui no podra encontrar ninguna coincidencia
#con la imagen que le pasamos y no obetendra ninguna coordenada por lo que obtendremos el error 
# TypeError: 'NoneType' object is not iterable cuando intentemos asignar valores a X y Y 
time.sleep(3)

tiempo_entre_operaciones = 1 #1 Segundo

time.sleep(tiempo_entre_operaciones)
#Selecciono la imagen correspondiente al 1 y a su vez
#asigno a X y Y las coordenadas de la imagen en el escritorio de la pc(en este caso la calculadora)
x,y = pyautogui.locateCenterOnScreen('imagenes/1.png')
#El robot se mueve hasta esa coordenada
pyautogui.moveTo(x, y, 1)
#El robot da click en esa coordenada
pyautogui.click()

time.sleep(tiempo_entre_operaciones)
#Selecciono la imagen correspondiente al 2 y a su vez
#asigno a X y Y las coordenadas de la imagen en el escritorio de la pc(en este caso la calculadora)
x,y = pyautogui.locateCenterOnScreen('imagenes/2.png')
#El robot se mueve hasta esa coordenada
pyautogui.moveTo(x,y, 1)
#El robot da click en esa coordenada
pyautogui.click()

time.sleep(tiempo_entre_operaciones)
#Selecciono la imagen correspondiente al + y a su vez
#asigno a X y Y las coordenadas de la imagen en el escritorio de la pc(en este caso la calculadora)
x,y = pyautogui.locateCenterOnScreen('imagenes/+.png')
#El robot se mueve hasta esa coordenada
pyautogui.moveTo(x,y, 1)
#El robot da click en esa coordenada
pyautogui.click()

time.sleep(tiempo_entre_operaciones)
#Selecciono la imagen correspondiente al 2 y a su vez
#asigno a X y Y las coordenadas de la imagen en el escritorio de la pc(en este caso la calculadora)
x,y = pyautogui.locateCenterOnScreen('imagenes/2.png')
#El robot se mueve hasta esa coordenada
pyautogui.moveTo(x,y, 1)
#El robot da click en esa coordenada
pyautogui.click()

time.sleep(tiempo_entre_operaciones)
##Selecciono la imagen correspondiente al 3 y a su vez
#asigno a X y Y las coordenadas de la imagen en el escritorio de la pc(en este caso la calculadora)
x,y = pyautogui.locateCenterOnScreen('imagenes/3.png')
#El robot se mueve hasta esa coordenada
pyautogui.moveTo(x,y, 1)
#El robot da click en esa coordenada
pyautogui.click()

time.sleep(tiempo_entre_operaciones)
#Selecciono la imagen correspondiente al = y a su vez
#asigno a X y Y las coordenadas de la imagen en el escritorio de la pc(en este caso la calculadora)
x,y = pyautogui.locateCenterOnScreen('imagenes/=.png')
#El robot se mueve hasta esa coordenada
pyautogui.moveTo(x,y, 1)
#El robot da click en esa coordenada
pyautogui.click()
