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
    
    $ python main_dyn_G.py --category fire --isTraining False --num_sections_in_test 4 --num_batches_in_test 2 --ckpt_name model.ckpt-2960
    
the 'num_sections_in_test' indicates the number of trucations of the synthesized video

the 'num_batches_in_test' indicates the number of independent synthesized videos

testing results will be saved in `./output_synthesis/fire/final_result_testing`.

(iii) Results

<p align="center">
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/fire.gif" width="350px"/> &nbsp; &nbsp;
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/light.gif" width="350px"/>  
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/waterfall.gif" width="350px"/> &nbsp; &nbsp;
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/frame.gif" width="350px"/>
</p>  

For each category, the first one is the observed video, and the other three are synthesized videos generated by the learned model. The observed video is of 60 frames in length, while the two synthesized videos are of 120 frames in length.

### (2) For action pattern synthesis

(i) Training

First, prepare your data into a folder, for example `./trainingVideo/action_dataset/animal30_running` 
  
To train a model with dataset ***animal30_running***:

    $ python main_dyn_G_motion.py --category animal30_running --isTraining True

The training results will be saved in `./output_synthesis/fire/final_result`. 

The learned models will be saved in `./output_synthesis/fire/model`. 

(ii) Testing

$ python main_dyn_G.py --category fire --isTraining False --num_sections_in_test 4 --num_batches_in_test 2 --ckpt_name model.ckpt-2960

(iii) Results

<p align="center">
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/animal.gif" width="720px"/>    
</p>  

### (3) For recovery

(iii) Results

<p align="center">
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/flag.gif" width="200px"/> &nbsp; &nbsp;
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/windmill.gif" width="200px"/> <br/>
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/ocean.gif" width="200px"/> &nbsp; &nbsp;
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/playing.gif" width="200px"/>
</p>  

### (4) For background inpainting

(iii) Results

<p align="center">
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/boat.gif" width="200px"/> &nbsp; &nbsp;
    <img src="https://github.com/jianwen-xie/Dynamic_generator/blob/master/demo/walking.gif" width="200px"/>   
</p>  

For any questions, please contact Jianwen Xie (jianwen@ucla.edu), Ruiqi Gao (ruiqigao@ucla.edu) and Zilong Zheng (zilongzheng0318@ucla.edu)
