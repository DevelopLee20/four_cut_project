# from PIL import Image

# # 1. 병합할 이미지 만들기
# merged = Image.new('L', (200 * 5, 200 * 2))

# for i in range(2):
#     for j in range(5):
#         # 2. 이미지 불러오기
#         im = Image.open('mnist_' + str(5 * i  + j) + '.png')

#         # 3. 이미지 붙여넣기
#         merged.paste(im, (200 * j, 200 * i))

# # 4. 병합한 이미지 저장하기
# merged.save('mnist_merged2.png')

from PIL import Image

gap = 20
end = 200
back_color = (153,204,255)

merged = Image.new('RGB', (640+gap*2,480*4+gap*4+end), back_color)

for i in range(4):
    img = Image.open('test.png')
    merged.paste(img, (gap,gap+gap*i+480*i))

# merged.show()
merged.save('endding.png')