from PIL import Image

for i in range(4):
    img = Image.open(f'{i+1}.png')
    img_resize = img.resize((640, 480))
    img_resize.save(f'{i+1}.png')