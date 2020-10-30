# Covid-Guard
An AI model to detect if people are following social distancing & wearing masks for safety.
<img src="Images/Logo.ico" alt="Covid Guard logo" title="Covid Guard" align="right" height="60" />
[](https://img.shields.io/github/forks/snjydas/Covid-Guard?style=social) ![](https://img.shields.io/github/stars/snjydas/Covid-Guard?style=social) ![](https://img.shields.io/github/watchers/snjydas/Covid-Guard?style=social) <br>

![](https://img.shields.io/github/repo-size/snjydas/Covid-Guard) ![](https://img.shields.io/github/license/snjydas/Covid-Guard?color=red)<br>
![](https://img.shields.io/github/issues/snjydas/Covid-Guard?color=green) ![](https://img.shields.io/github/issues-pr/snjydas/Covid-Guard?color=green) ![](https://img.shields.io/github/downloads/snjydas/Covid-Guard/total) ![](https://img.shields.io/github/last-commit/snjydas/Covid-Guard) ![](https://img.shields.io/github/contributors/snjydas/Covid-Guard)

## Content
- [Overview](#overview)
- [Setup](#setup)
- [Installation](#installation)
- [Run](#run)
- [Output](#output)
- [Features](#features)
- [Reference](#reference)
- [License](#license)
- [Contributor](#contributor)



### **`Folder structure`**
<hr/>

📁 Covid Guard<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 📁 Demo <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 📁 Face Detector <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 📁 Images <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 📁 Model <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 📁 Output <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --Covid Guard.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --Home.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --main.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --requirements.txt <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --running_video_file.py.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --video_recorder.py <br/>

      |__ Demo
        |______ Images: [Demo1.jpeg, Demo3.png, Demo4.png, Interface.PNG, Code Snippet.PNG]
        |______ GIFs: [Gif_1.gif, Start.gif, Gif_2.gif]      

      |__ Face Detector
        |______ deploy.prototxt
        |______ res10_300x300_ssd_iter_140000.caffemodel

      |__ Images
        |______ [background.jpg, Load.gif, Logo.ico, TrojanWave.png]
        
      |__ Model
        |______ [coco.names, mask_detector.model, Model.png, README.txt, yolov3.cfg ]
          
      |__ Output
        |______ [ Gif_1.mp4, Gif_2.mp4, Loading.mp4]


## Overview

- In the present scenario due to Covid-19, there is no efficient face mask detection applications which are now in high demand for transportation means, densely populated areas, residential districts, large-scale manufacturers and other enterprises to ensure safety. 
- Amidst the COVID-19 situation,  maintaining social distancing and wearing  masks is ignored. And, no  data is recorded to ﬁnd out which regions  are violating the same. If there is some  way to get this data, necessary  actions can be taken. Well, rest easy as our  solution does this for you!
#### The proposed system can be used in real-time applications which require face-mask & social distancing detection for safety purposes.
#### The system can be integrated with embedded systems for application in airports, railway stations, offices, schools, and public places to ensure that public safety guidelines are followed.

## Setup

- Clone the repo and cd into the directory


```sh
$ git clone "https://github.com/snjydas/Covid-Guard"
$ cd Covid Guard
```

### Download Model Weights
<hr/>

Please download the yolov3 model weights by from [pjredddie.com](https://pjreddie.com/media/files/yolov3.weights) & save the yolov3.weights inside the ./Model Directory.

## Installation


```sh
$ pip install tensorflow
$ pip install EasyTkinter
$ pip install opencv-python
$ pip install keras
$ pip install Pillow
$ pip install imutils
$ pip install numpy
```
Or

```sh
$ pip install -r requirements.txt 
```

## Run

```sh
$ cd Covid Guard
$ python "Covid Guard.py"
```
<p align="center">
<img src="Demo/Start.gif", width="640"></p>
<p align="center">     
Demo: Running The Application
</p>

## Output

<p align="center">
<img src="Demo/Gif_1.gif", width="640"></br>
Output: Single Person
</p>
</hr></br>

<p align="center">
<img src="Demo/Gif_2.gif", width="640"></br>
Output: Multiple Persons In Single Frame
</p>

## Features

- Live video surveillance to fight against covid-19 spread
- The project can be integrated with embedded systems for application in airports, railway stations, offices, schools, and public places to ensure that public safety guidelines are followed.
- Real time face mask detection and for social distancing tracking the crowd movement across the day time.
- Hot-spot area can be monitored by security forces from central station.
- If AI based solution used by authority, then there will be less chance to infect security forces.


## Reference

- [Pyimagesearch - fine tuning resnet with keras tensorflow and deep-learning](https://www.pyimagesearch.com/2020/04/27/fine-tuning-resnet-with-keras-tensorflow-and-deep-learning/)
- [Tensorflow - Guide](https://www.tensorflow.org/guide/)
- [Keras - Guide](https://keras.io/guides/)

## License

Licensed under the [MIT License](LICENSE)

## Contributor

<p align="center">

|                                                                                                                                                                                                                   <a href="https://github.com/snjydas"><img src="https://avatars.githubusercontent.com/snjydas" width="150px" height="150px" /></a>                                                                                                                                                                                                                    |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                             **[Sanjay Das](https://github.com/snjydas)**                                                                                                                                                                                                                                                              |
| <a href="https://twitter.com/snjy_das"><img src="https://i.ibb.co/kmgQVyW/twitter.png" width="32px" height="32px"></a> <a href="https://github.com/snjydas"><img src="https://cdn.iconscout.com/icon/free/png-256/github-108-438008.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/snjydas251297"><img src="https://i.ibb.co/zmYNW4p/facebook.png" width="32px" height="32px"></a> <a href="https://https://www.linkedin.com/in/snjydas/"><img src="https://i.ibb.co/Kx2GSrT/linkedin.png" width="32px" height="32px"></a> |

<hr/>

<p align="center">

|                                                                                                                                                                                                                   <a href="https://github.com/abhi526691"><img src="https://avatars.githubusercontent.com/abhi526691" width="150px" height="150px" /></a>                                                                                                                                                                                                                    |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                             **[Abhishek Pandey](https://github.com/abhi526691)**                                                                                                                                                                                                                                                              |
| <a href="https://twitter.com/Abhi10548"><img src="https://i.ibb.co/kmgQVyW/twitter.png" width="32px" height="32px"></a> <a href="https://github.com/abhi526691"><img src="https://cdn.iconscout.com/icon/free/png-256/github-108-438008.png" width="32px" height="32px"></a> <a href="https://www.instagram.com/_abhishek__pandey___/"><img src="https://i.ibb.co/zmYNW4p/instagram.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/abhishek-pandey-1515aa171/"><img src="https://i.ibb.co/Kx2GSrT/linkedin.png" width="32px" height="32px"></a> |

<hr/>

```bash
                                                      ╔═╗╔╦╗╔═╗╦ ╦  ╦ ╦╔═╗╔╦╗╔═╗
                                                      ╚═╗ ║ ╠═╣╚╦╝  ╠═╣║ ║║║║║╣
                                                      ╚═╝ ╩ ╩ ╩ ╩   ╩ ╩╚═╝╩ ╩╚═╝
                                                      ╔═╗╔╦╗╔═╗╦ ╦  ╔═╗╔═╗╔═╗╔═╗
                                                      ╚═╗ ║ ╠═╣╚╦╝  ╚═╗╠═╣╠╣ ║╣
                                                      ╚═╝ ╩ ╩ ╩ ╩   ╚═╝╩ ╩╚  ╚═╝
```

</p>
