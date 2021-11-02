# 使用imgaug进行数据增强
# Note: 如果是带有mask的分割任务 Augmentor更为方便易用
import cv2
from imgaug import augmenters as iaa
import glob

seq = iaa.Sequential([
    # Sometimes 可表示此种增强的概率
    iaa.Sometimes(
        0.5, iaa.Crop(px=(0, 20))),  # 以0.5的概率，从每侧裁剪图像0到20px（随机选择）
    iaa.Fliplr(0.5),  # 0.5概率水平翻转图像
    iaa.GaussianBlur(sigma=(0, 3.0)),  # 使用0到3.0的sigma模糊图像
    # iaa.Resize((0.5, 1.5)),  # 将w和h在0.5-1.5倍范围内resize
    iaa.Affine(
        scale=(0.5, 1.5),  # 缩放到50%到150%
        rotate=(-45, 45))  # 旋转-45到45度
])

# # 测试单个图像的增强效果
# img = cv2.imread('image.png')
# for i in range(10):
#     img_aug = seq.augment_image(img)
#     cv2.imwrite('test.png', img_aug)

# 批量 从文件夹 读取图像，并放入一个list中

# 首先声明一个空的列表
img_list = []
for jpg_file in glob.glob('./imgs/*.png'):
    # 向列表中添加元素
    img_list.append(cv2.imread(jpg_file))
    # 每张图片增强十次
    for i in range(10):
        imgs_aug = seq.augment_images(img_list)
        for img in enumerate(imgs_aug):
            # 此时增强后的十张图片合并入imgs中的训练数据集
            cv2.imwrite(jpg_file.replace('.png', '') + '_' + str(i) + '.png', img)
