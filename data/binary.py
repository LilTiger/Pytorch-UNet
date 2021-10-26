# 将labelme的json文件批量生成dataset后 执行此文件（注意主函数中的path）
# 将多通道mask图像批量转换为单通道二值化图像并存放到指定位置
# 之后执行temp.py

import cv2
import os


def os_mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部/符号
    path = path.rstrip("/")
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功！')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + '目录已存在')
        return False


def mask2binimg(path, show=False):
    for root, dirs, files in os.walk(path):
        for name in files:
            # 遍历labelme生成的{x}_json目录
            if len(dirs) == 0:
                # 字符分割，得到Label排序序号
                filepath = os.path.split(root)[0]
                numname = os.path.split(root)[1]
                n_name = numname.replace('_json', '')

            # 处理原图img
            if name == 'img.png':
                fname = os.path.join(root, name)
                print('INFO[img]', fname)
                img = cv2.imread(fname)
                img_dst = cv2.resize(img, (640, 480))

                if show:
                    cv2.imshow('img', img_dst)
                    cv2.waitKey()
                # 根据指定路径存取二值化图片
                img_path = filepath + '/imgs/'
                os_mkdir(img_path)
                cv2.imwrite(img_path + str(n_name) + '.png', img_dst)

            # 处理Label标签图
            if name == 'label.png':
                fname = os.path.join(root, name)
                print('INFO[label]', fname)
                label = cv2.imread(fname)
                label = cv2.resize(label, (640, 480))
                gray = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)
                retVal, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
                # 显示图片
                if show:
                    cv2.imshow('label', label)
                    cv2.imshow('dst', dst)
                    if cv2.waitKey(1) & 0xff == ord('q'):
                        break
                # 根据指定路径存取二值化图片
                mask_path = filepath + '/masks/'
                os_mkdir(mask_path)
                cv2.imwrite(mask_path + str(n_name) + '.png', dst)

    print('当前图片转换完成...')
pass


if __name__ == '__main__':
    # 直接处理后将保存在data数据文件夹 注意请提前将labelme的dataset放入此文件夹
    path = '/'
    mask2binimg(path, False)







