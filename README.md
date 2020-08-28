# Covid-Guard
An AI model to detect if people are following social distancing & wearing masks for safety.
<img src="Images/Logo.ico" alt="Covid Guard logo" title="Covid Guard" align="right" height="60" />
[](https://img.shields.io/github/forks/snjydas/Covid-Guard?style=social) ![](https://img.shields.io/github/stars/snjydas/Covid-Guard?style=social) ![](https://img.shields.io/github/watchers/snjydas/Covid-Guard?style=social) <br>

![](https://img.shields.io/github/repo-size/snjydas/Covid-Guard) ![](https://img.shields.io/github/license/snjydas/Covid-Guard?color=red)<br>
![](https://img.shields.io/github/issues/snjydas/Covid-Guard?color=green) ![](https://img.shields.io/github/issues-pr/snjydas/Covid-Guard?color=green) ![](https://img.shields.io/github/downloads/snjydas/Covid-Guard/total) ![](https://img.shields.io/github/last-commit/snjydas/Covid-Guard) ![](https://img.shields.io/github/contributors/snjydas/Covid-Guard)

## Content
- [Overview](#overview)
- [Getting Started](#Getting Started)
- [Installation](#installation)
- [Demo](#demo)
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
        |______ Images: [Demo1.jpeg, Demo3.png, Demo4.png, Interface.PNG]
        |______ GIFs: [NO_Mask.1.jpg, NO_Mask.2.jpg, NO_Mask.3.jpg ...]      

      |__ Face Detector
        |______ WithMask: [Mask.1.jpg, Mask.2.jpg, Mask.3.jpg ....]
        |______ NO_Mask: [NO_Mask.1.jpg, NO_Mask.2.jpg, NO_Mask.3.jpg ...]

      |__ Images
        |______ [test.1.jpg, test.2.jpg, test.3.jpg , test.4.jpg , test.5.jpg , ....]
        
      |__ Images
        |______ [test.1.jpg, test.2.jpg, test.3.jpg , test.4.jpg , test.5.jpg , ....]

### Getting Started
<hr/>
- Clone the repo and cd into the directory


```sh
$ git clone "https://github.com/snjydas/Covid-Guard"
$ cd Covid Guard
```
### Download Model Weights
<hr/>
Please Download yolov3 model weights by from: [pjredddie.com](https://pjreddie.com/media/files/yolov3.weights) and save the yolov3.weights inside the ./Model Directory.

### Install tensorflow and all the other required libraries 
<hr/>


```sh
$ pip install tensorflow
$ pip install EasyTkinter
$ pip install opencv-python
$ pip install keras
$ pip install Pillow
$ pip install imutils
$ pip install numpy
```sh
Or
```sh
$ pip install -r requirements.txt 
```

### To run the Application
<hr/>

```sh
$ cd Covid Guard
$ python "Covid Guard.py"
```


### Start

<p align="center">
<img src="Demo/start.gif", width="640">
</p>



### Demo

<p align="center">
    <img src="Demo/start.gif", width="600">
    <br>
    <sup></sup>
</p>


### Real time face mask detecting

<div align="center" style="height:400px"> 
<img src=' ' width="90%">
<h4><a href="">Video source :- Why are some wearing face masks?</a></h4>
</div>

## Social Distancing Detector

<div align="center" style="height:400px"> 
<img src=' ' width="80%">
<h4><a href=" ">Video source :- Pedestrian(sample)</a></h4>
</div>

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

```bash
╔═╗╔╦╗╔═╗╦ ╦  ╦ ╦╔═╗╔╦╗╔═╗
╚═╗ ║ ╠═╣╚╦╝  ╠═╣║ ║║║║║╣
╚═╝ ╩ ╩ ╩ ╩   ╩ ╩╚═╝╩ ╩╚═╝
╔═╗╔╦╗╔═╗╦ ╦  ╔═╗╔═╗╔═╗╔═╗
╚═╗ ║ ╠═╣╚╦╝  ╚═╗╠═╣╠╣ ║╣
╚═╝ ╩ ╩ ╩ ╩   ╚═╝╩ ╩╚  ╚═╝
```

</p>
