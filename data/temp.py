# 此函数用来将binary生成的二值化mask归一为0-1
# 因U-Net输入须为0-1 而非 0-255
import numpy as np
import glob
from PIL import Image
mask_list = glob.glob('./masks/*.png')

# 注意此函数不要重复执行，一次即可
for mask in mask_list:
    # 将图片转化为array
    label = np.array(Image.open(mask))
    new_label = label/255
    # 将array转化为图片 注意需要首先转为为uint8格式
    new_label = new_label.astype(np.uint8)
    new_label = Image.fromarray(new_label)
    new_label.save(mask)

print("Successfully normalized!")
