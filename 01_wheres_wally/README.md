### WheresWally

This repository contains the proposed solution for the WheresWally problem. 

The folder is distributed as follow:

- aug_data[folder]: Some additional image generated for extra training;
- evaluation[folder]: From the training dataset, after the filtering, the masks were generated for visual inspection validation to check if the mask was annotated correctly;
- fixed_training[folder]: Some images were annotated wrongly. This folder contains those images, but with the fixed annotation, performed manually;
- test_evaluation[folder]: After the training, the test images were predicted, and the mask and centroids were generated. In this folder, we save those images with this data;
- proposed_solution.ipynb[notebook]: Notebook file, with the proposed solution, contains all the method and steps to perform the method;
- single_loss_best.h5[keras weights]: Weights saved from the best model, considering the minimal loss;
- TestSet, TrainingSet, ReferenceData[folder]: Data provided by the challenge.

#Approachs overview and samples

To run the notebook, it us necessary to install the **requitiments.txt**, the following command:

`$ jupyter notebook`

then run the notebook **proposed_solution.ipynb**

## Problem Overview

The problem is from a certain image, we should detect where is wally, and the wally is placed in a large range of position and rotation. The Figure below shows an example. On the right is a generate mask just for visualization as additional is required to create the centroid of the detect wally.

<p align="center">
  <img width="640" height="480" src="evaluation/1.png">
</p>



Some images were annotated wrongly, so those images were discarded. In a forward process, the annotated images were fixed manually. Since we have few images (120 images), more images were generated, around 4k images, to help generalize the training. The figure below shows some of the augmentation data. 

<p align="center">
  <img width="270" height="290" src="aug_data/wally_054_0.jpg">
</p>








The proposed solution was based on a segmentation Convolutional Neural Network. The model was designed with Keras with Tensorflow backend.  Additional tools for evaluation and data handled were OpenCV, Numpy, Pandas, MatplotLib, JSON, and other minors. 

The model contains ten layers. They are composed basically of convolutional layers, pooling layers for feature encoding, and upsampling layers. The figure below shows an overview of the model. 



<p align="center">
  <img width="270" height="290" src="model.png">
</p>



The model predicts works as a segmentation, prediction the foreground (1 or the wally) and the background (0). For the training was used the Cross Binary entropy, due to the binary approach. Due to some hardware limitations, the model was trained on the **Collab**[[1](https://drive.google.com/file/d/1ZP01a4LbOW5ibXqYvaDGC7_RuKmN216X/view?usp=sharing)]. The results fro from the training are: [**loss: 0.0134 - MSE: 0.0040**]. The figure below shows a sample of an input image and the predicted image.



<p align="center">
  <img width="500" height="200" src="prediction.png">
</p>



With the predicted mask, we need some post-processing to get the contour and centroids. To solve this problem, we used OpenCV. From the generated masks, we get all the contours, the boundaries of each white object on the mask. Since the prediction can generate some artifacts, such as regions wrongly classified as wally, we only considered the contour with the most significant region area. From those boundaries, we extract the centroids of the lower and upper pixels on the x-axis and y-axis. The Figures below show some samples of the images predicted. 



<p align="center">
  <img width="500" height="200" src="test_evaluation/23.png">
  <img width="500" height="200" src="test_evaluation/13.png">
  <img width="500" height="200" src="test_evaluation/29.png">
</p>
