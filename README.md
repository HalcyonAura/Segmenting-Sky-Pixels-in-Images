# SegmentingSkyPixels

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
* Trained from scratch (ImageNet) (coming soon!)

## Datasets
* [SkyFinder]()
* [SUNdb]()

## Results

## Citation
Coming soon!

## Questions?
Please contact:
Cecilia La Place: cecilia.laplace@gmail.com
Aisha Urooj: aishaurooj@gmail.com
