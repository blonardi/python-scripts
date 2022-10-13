import cv2 as cv
# print(cv.__version__)
path = r'/home/bauti/Desktop/python-moure/python-platzi/py-udemy/contorno.jpg'
imagen = cv.imread(path)
grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
threshold = 


#Mostrar
cv.imshow('imagen original',imagen)
cv.imshow('imagen en gris',grises)

cv.waitKey(0)
cv.destroyAllWindows()