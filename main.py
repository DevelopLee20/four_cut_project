from storage import st_rembg, st_opencv, st_pil

gap = 20
end = 200
back_color = (255,255,255)
paper_color = (153,204,255)

input = st_opencv.camera('./img/input', 4)
output = st_rembg.remove_back('./img/output', input)
finally_name = st_pil.merge('./img/fin', output, back_color, paper_color, gap, end)
print(f'saving {finally_name}')