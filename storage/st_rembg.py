from rembg import remove
from PIL import Image
import time

def remove_back(path:str, input_name_list:list):
    '''rembg 기반 누끼따고 저장하는 함수
    path : 파일의 주소 입력 ( 예시 : ./img )
    input_name_list : 입력 이미지의 이름 리스트
    
    return : 이미지 전환이 끝난 출력 이름 리스트(path 포함)
    '''
    output_name_list = []
    
    for input_name in input_name_list:
        input = Image.open(f'{input_name}')
        output = remove(input)
        file_name = f'{time.time()}'
        output.save(f'{path}/{file_name}.png')
        print(f'{file_name} is saved')
        output_name_list.append(f'{path}/{file_name}.png')
        print(f'{file_name} is successed change.')
    
    return output_name_list