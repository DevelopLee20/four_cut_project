import cv2
import time

def camera(path:str, file_count:int):
    '''카메라 실행 시킨 후 c 입력시 촬영, 4회 촬영시 종료하는 함수
    path : 촬영 파일 저장할 위치 ( 예시 : ./img )
    file_count : 촬영하고 싶은 장 수 입력
    
    return : 촬영 파일 이름 리스트 반환(path 포함)
    '''
    file_name_list = []
    webcam = cv2.VideoCapture(0)
    
    if not webcam.isOpened():
        print("Could not open webcam")
        exit()
    
    while webcam.isOpened():
        status, frame = webcam.read()
        
        if status:
            cv2.imshow("camera", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            file_name = f"{path}/{time.time()}.png"
            cv2.imwrite(file_name, frame)
            file_count = file_count - 1
            file_name_list.append(file_name)
            print(f'{file_name} capture fin')
        
        if not file_count:
            break
    
    webcam.release()
    cv2.destroyAllWindows()
    
    return file_name_list