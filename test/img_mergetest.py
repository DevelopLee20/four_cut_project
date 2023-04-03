
# 1
# 2
# 3
# 4
# target_image = Image.open('기본 이미지.jpg')  
# add_image = Image.open('넣고싶은 이미지 경로 및 이름.jpg')
# target_image.paste(im = add_image,box =(넣을 이미지 x좌표,넣을 이미지 y좌표))
# target_image.save("저장할 이미지 경로 및 이름.jpg")

from PIL import Image

background = Image.open("back.png")
foreground = Image.open("test.png")

background.paste(foreground, (0, 0), foreground)
background.save('test1.png')
background.show()