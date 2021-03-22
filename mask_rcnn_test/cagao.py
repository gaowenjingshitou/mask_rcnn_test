import  keras
import os
import cv2
import tensorflow as tf
print(keras.__version__)  #2.0.8
print(tf.__version__)  #1.15.0
# #
dataset_root_path = "mydata/"
# img_floder = dataset_root_path + "pic"
path = dataset_root_path + "cv2_mask"
# imglist = os.listdir(img_floder)
# print(imglist)
# count = len(imglist)

# for i in range(count):
#     # 获取图片宽和高
#     # print(i)
#
#     filestr = imglist[i].split(".")[0]
#     print(filestr)
    # mask_path = mask_floder + "/" + filestr + ".png"
    # print(mask_path)

# import os
# 
# for file in os.listdir(path):
#     name = file.split('.')[0]
#     # print(name)
#     src_name=os.path.join(path, file)
#     dst_name=os.path.join(path, '0%s'% name + ".png")
#     #print(dst_name)
#     os.rename(src_name, dst_name)


_idx = np.sum(mask, axis=(0, 1)) > 0
mask = mask[:, :, _idx]
class_ids = class_ids[_idx]