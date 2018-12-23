# Learning Dynamic Generator Model by Alternating Back-Propagation Through Time

This repository contains a tensorflow implementation for the paper "[Learning Dynamic Generator Model by Alternating Back-Propagation Through Time](http://www.stat.ucla.edu/~jxie/DynamicGenerator/DynamicGenerator_file/doc/DynamicGenerator.pdf)".

Project Page: (http://www.stat.ucla.edu/~jxie/DynamicGenerator/DynamicGenerator.html)

## Reference
    @article{DG,
        author = {Xie, Jianwen and Gao, Ruiqi and Zheng, Zilong and Zhu, Song-Chun and Wu, Ying Nian},
        title = {Learning Dynamic Generator Model by Alternating Back-Propagation Through Time},
        journal={The Thirty-Third AAAI Conference on Artificial Intelligence (AAAI)},
        year = {2019}
    }
  
 ## Requirements
- Python 2.7 or Python 3.3+
- [Tensorflow r1.0+](https://www.tensorflow.org/install/)
- [Scipy](https://www.scipy.org/install.html)
- [pillow](https://pillow.readthedocs.io/en/latest/installation.html)

## Usage

### (1) For dynamic texture synthesis

(i) Training

First, prepare your data into a folder, for example `./trainingVideo/dynamicTexture/fire` 
  
To train a model with dynamic texture ***fire***:

    $ python main_dyn_G.py --category fire --isTraining True

The training results will be saved in `./output_synthesis/fire/final_result`. 

The learned models will be saved in `./output_synthesis/fire/model`. 


(ii) Testing for dynamic texture synthesis  
    
    $ python main_dyn_G.py --category fire --isTraining False --net_type scene --image_size 64 --output_dir ./output --ckpt ./output/rock/checkpoints/model.ckpt-82000

testing results will be saved in `./output/rock/test/synthesis`

  
