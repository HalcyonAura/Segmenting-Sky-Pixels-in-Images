# Segmenting Sky Pixels in Images: Analysis and Comparison

## Abstract
This work addresses sky segmentation, the task of determining sky and non-sky pixels in images, and improving upon existing state-of-the-art models. Outdoor scene parsing models are often trained on ideal datasets and produce high-quality results. However, this leads to a discrepancy when applied to the real-world images. The quality of scene parsing, particularly sky segmentation, decreases on night-time images, images involving varying weather conditions, and scene changes due to seasonal weather. We address these challenges using the RefineNet model in conjunction with two datasets: SkyFinder, and a subset of the SUN database containing the Sky regions (SUN-sky, henceforth). We achieve an improvement of 10-15\% in the average MCR compared to the prior methods on the SkyFinder dataset, and nearly 36\% improvement from an off-the-shelf model in terms of average mIOU score. Employing fully connected conditional random fields as a post processing method demonstrates further enhancement in our results. Furthermore, by analyzing models over images with respect to two aspects, time of the day and weather conditions, we find that when facing the same challenges as prior methods, our trained models significantly outperform them.

[Paper](https://arxiv.org/abs/1712.09161)
[Project](https://github.com/HalcyonAura/Segementing-Sky-Pixels-in-Images/)

## Code
The following scripts were used to analyze data, automate image replication and processing and more.
* Python scripts
* MATLAB scripts
* RefineNet files

## Models
* Improved Cityscapes (coming soon!)
* Trained from scratch (ImageNet) [1](https://drive.google.com/file/d/1Ae5nS_ZLgtoKRz_Tw6eJZoSdZE9Gy9W_/view?usp=sharing) [2](https://drive.google.com/file/d/1_9O4H1leb4_bxtmAnxyj03djnlGi_qHy/view?usp=sharing) [3](https://drive.google.com/file/d/1GL-CaSWSEn5oH_SRhVYnJhfJ10HUIhCo/view?usp=sharing)

## Datasets
* [SkyFinder](https://mypages.valdosta.edu/rpmihail/skyfinder/images/)
* [SUNdb](https://groups.csail.mit.edu/vision/SUN/)

## Results

## Citation
Coming soon!

## Questions?
Please contact:

* Cecilia La Place: cecilia.laplace@gmail.com
* Aisha Urooj: aishaurooj@gmail.com
