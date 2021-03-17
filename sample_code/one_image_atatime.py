import numpy as np
import cv2
import depth_map_utils as dutils

def one_image_completion(path, times=8):
    depth = cv2.imread(path, cv2.IMREAD_ANYDEPTH)

    depth_c = depth.astype(np.float32) / times * 0.001
    depth_c = dutils.fill_in_fast(depth_c)
    depth_c = (depth_c * times / 0.001).astype(np.uint16)

    return depth_c

if __name__ == '__main__':
    import pathlib
    from tqdm.contrib import tzip
    import datetime

    def concat_tile(im_list_2d):
        return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

    def scale_to_height(img, height):
        """幅が指定した値になるように、アスペクト比を固定して、リサイズする。
        """
        h, w = img.shape[:2]
        width = round(w * (height / h))
        dst = cv2.resize(img, dsize=(width, height))

        return dst

    dir_path = pathlib.Path('./sample_images/input')
    dpaths = sorted(list(dir_path.glob('./*.png')))
    cpaths = sorted(list(dir_path.glob('./*.jpg')))
    print(dpaths)
    vis_list = list()
    for dpath, cpath in tzip(dpaths, cpaths):
        color = cv2.imread(str(cpath), cv2.IMREAD_COLOR)
        depth = cv2.imread(str(dpath), cv2.IMREAD_ANYDEPTH)
        depth_c = one_image_completion(str(dpath))
        
        depth_vis = cv2.convertScaleAbs(np.repeat(depth[:, :, None], 3, axis=2), alpha=(255.0/65535.0))
        depth_c_vis = cv2.convertScaleAbs(np.repeat(depth_c[:, :, None], 3, axis=2), alpha=(255.0/65535.0))
        vis = cv2.vconcat([color, depth_vis, depth_c_vis])
        vis = scale_to_height(vis, 800)
        vis_list.append(vis)

        cv2.imshow('out', vis)
        cv2.waitKey(100)
    
    dt_now = datetime.datetime.now()
    dt_str = dt_now.strftime('%Y-%m-%d-%H')

    vis_all = cv2.hconcat(vis_list)
    cv2.imwrite('./sample_images/output/' + dt_str + '.png', vis_all)
    cv2.imshow('vis all', vis_all)
    cv2.waitKey(0)
