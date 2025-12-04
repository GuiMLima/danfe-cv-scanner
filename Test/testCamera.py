from ultralytics import YOLO
import cv2

#Carrega um modelo yolov8s pré-treinado COCO (Contexto em Objetos Comuns) / Load a COCO-pretrained yolov8s model
model = YOLO("yolov8s.pt")

#Abre a câmera padrão / Open the default camera
cam = cv2.VideoCapture(0)

#Obtêm o quadro padrão da largura e da altura / Get the default frame width and height
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

while True:
    ret, frame = cam.read()

    out.write(frame)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cam.release()
cv2.destroyAllWindows()