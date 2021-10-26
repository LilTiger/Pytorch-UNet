# 此处为augementor数据增强工具
# 可以快速生成大量增强后的img和mask 但受限于生成文件名称不规范 不利于后续作为U-Net的数据集（mask和img文件名相同或存在某种规律）

# 导入数据增强工具
import Augmentor

# 确定原始图像存储路径以及掩码文件存储路径
p = Augmentor.Pipeline("./imgs/")  # 原图和mask的标签要一一对应！！扩充后的图都在原图里面新生成output的文件夹！
p.ground_truth("./masks/")  # 标签图mask

# 图像旋转： 按照概率0.8执行，最大左旋角度10，最大右旋角度10
p.rotate(probability=0.8, max_left_rotation=20, max_right_rotation=20)

# 图像左右互换： 按照概率0.5执行
p.flip_left_right(probability=0.5)

# 图像放大： 按照概率0.8执行，面积为原始图0.85倍
p.zoom_random(probability=1, percentage_area=0.8)
# p.scale(probability=1, scale_factor=1.5)  # 此中的scale操作可理解为 扩大图像尺寸

# 最终扩充的数据样本数
p.sample(4)
