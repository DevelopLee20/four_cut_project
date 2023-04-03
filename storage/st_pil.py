from PIL import Image
import time

def merge(path:str, file_list:list, back_color:tuple, paper_color:tuple, pic_gap:int, end_size:int):
    '''4컷 틀을 적용시키는 함수
    path : 저장할 파일 주소
    file_list : 변환한 파일명 리스트
    back_color : 사진 배경 컬러
    paper_color : 종이 배경 컬러
    pic_gap : 사진간의 간격
    end_size : 마지막 끝의 크기
    
    return : 만든 파일명
    '''
    
    fin_pic = Image.new("RGB", (640+pic_gap*2,480*len(file_list)+pic_gap*len(file_list)+end_size), paper_color)
    
    for i in range(len(file_list)):
        background = Image.new("RGB", (640,480), back_color)
        img = Image.open(file_list[i])
        background.paste(img, (0,0), img)
        fin_pic.paste(background, (pic_gap,pic_gap+pic_gap*i+480*i))
        print(f'merge picture {i} / 4')
    
    file_name = f'{path}/{time.time()}.png'
    fin_pic.save(file_name)
    print(f'{file_name} saved.')
    
    return file_name