from storage import st_rembg, st_opencv, st_pil
from PIL import Image

gap = 20
end = 400
back_color = (255,255,255)
paper_color = (0,102,204)

for i in range(4):
    img = Image.open(f'./test/{i+1}.png')
    img_resize = img.resize((640, 480))
    img_resize.save(f'./test/{i+1}.png')

input = [f'./test/{i+1}.png' for i in range(4)]

output = st_rembg.remove_back('./img/output', input)
finally_name = st_pil.merge('./others', output, back_color, paper_color, gap, end)
print(f'saving {finally_name}')