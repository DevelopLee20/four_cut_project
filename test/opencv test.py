import cv2

webcam = cv2.VideoCapture(0)
file_name = 4

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    
    if status:
        cv2.imshow("test", frame)
    
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite(f"./img/{4-file_name}.png", frame)
        file_name = file_name - 1
        print('Capture Fin')
        if not file_name:
            break
        
webcam.release()
cv2.destroyAllWindows()