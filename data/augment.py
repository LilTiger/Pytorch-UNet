# 此处为使用albumentations进行数据增强
# 可以根据生成相同文件名的img和mask
import albumentations as A
import cv2
import os
import glob

transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.4),
    A.RandomRotate90(p=0.4),
    # 在保持图片大小不变的情况下随机crop
    A.RandomSizedCrop(min_max_height=(420, 460), height=480, width=640, p=0.4),
    A.OneOf([
        # always_apply与p=的作用相同 二者不必同时使用（暂定）
        A.GaussianBlur(blur_limit=(3, 7), always_apply=False, p=0.4),
        A.Sharpen(alpha=(0.2, 0.5), lightness=(0.5, 1.0), p=0.2),
             ])
])

# 可以同时对img和mask批量处理，但注意 在处理过程中 二者需要一一对应、一同处理
# 定义路径 注意imgs和masks路径不同
path = "./imgs/*.png"
path_1 = "./masks/*.png"

# 在imgs文件夹中遍历所有png格式的image
for jpg in glob.glob(path):
    image = cv2.imread(jpg)
    # 提取路径中的图片名*.png
    jpg_file = os.path.basename(jpg)
    # 在masks文件夹中遍历所有png格式的mask
    for masks in glob.glob(path_1):
        mask = cv2.imread(masks)
        mask_file = os.path.basename(masks)
        # 寻找 与此时的 image 同名的 mask 以一一对应原图和分割掩码
        if str(jpg_file) == str(mask_file):
            # 去除图片名中的后缀.png 以生成*_i.png形式的image和mask
            a = str(jpg_file).split('.')[0]
            for i in range(20):
                transformed = transform(image=image, mask=mask)
                transformed_image = transformed['image']
                transformed_mask = transformed['mask']
                transformed_mask = cv2.cvtColor(transformed_mask, cv2.COLOR_RGB2GRAY)

                cv2.imwrite('./img1/' + str(a) + '_' + str(i) + '.png', transformed_image)
                cv2.imwrite('./mask1/' + str(a) + '_' + str(i) + '.png', transformed_mask)


