## Image Processing for Basic Depth Completion (IP-Basic)
Depth completion is the task of converting a sparse depth map D<sub>sparse</sub> into a dense depth map D<sub>dense</sub>. This algorithm was originally created to help visualize 3D object detection results for [AVOD](https://arxiv.org/abs/1712.02294).

An accurate dense depth map can also benefit 3D object detection or SLAM algorithms that use point cloud input. This method uses an unguided approach (images are ignored, only LIDAR projections are used). Basic depth completion is done with OpenCV and NumPy operations in Python. For more information, please see our paper: [In Defense of Classical Image Processing: Fast Depth Completion on the CPU](https://arxiv.org/abs/1802.00036).

Please visit [https://github.com/kujason/scene_vis](https://github.com/kujason/scene_vis) for 3D point cloud visualization demos on raw KITTI data.

If you use this code, we would appreciate if you cite our paper:
[In Defense of Classical Image Processing: Fast Depth Completion on the CPU](https://arxiv.org/abs/1802.00036)

```
@inproceedings{ku2018defense,
  title={In Defense of Classical Image Processing: Fast Depth Completion on the CPU},
  author={Ku, Jason and Harakeh, Ali and Waslander, Steven L},
  booktitle={2018 15th Conference on Computer and Robot Vision (CRV)},
  pages={16--22},
  year={2018},
  organization={IEEE}
}
```

## Abstract
This repository is forked from https://github.com/kujason/ip_basic \
I added a sample code for one image at a time. (./sample_code)

![2021-03-17-16](https://user-images.githubusercontent.com/47411597/111439963-38308b80-8749-11eb-9ca3-465d4a112c0e.png)
