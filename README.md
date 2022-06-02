# Gesture-control-mediaplayer

[![Maintenance](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Maintenance](https://img.shields.io/badge/Mediapipe-Traking-red.svg)](https://google.github.io/mediapipe/) 
[![Maintenance](https://img.shields.io/badge/OPENCV-Python-green.svg)](https://opencv.org/) 
[![Maintenance](https://img.shields.io/badge/CoputerVission-CV-orange.svg)]()

![adsf](images/demo.gif)


## Sample

># Play Pause Gesture
>
>![](https://github.com/THARUNESHWAR-369/Gesture-control-mediaplayer/blob/main/gesture%20position/play%20pause.png)

># Volume Increase Gesture
>
>![](https://github.com/THARUNESHWAR-369/Gesture-control-mediaplayer/blob/main/gesture%20position/volume%20increase.png)

># Volume Decrease Gesture
>
>![](https://github.com/THARUNESHWAR-369/Gesture-control-mediaplayer/blob/main/gesture%20position/volume%20decrease.png)

># Forward Gesture
>
>![](https://github.com/THARUNESHWAR-369/Gesture-control-mediaplayer/blob/main/gesture%20position/forward.png)

># Rewind Gesture
>
>![](https://github.com/THARUNESHWAR-369/Gesture-control-mediaplayer/blob/main/gesture%20position/backward.png)

># Full Screen Gesture
>
>![](https://github.com/THARUNESHWAR-369/Gesture-control-mediaplayer/blob/main/gesture%20position/fullscreen.png)

# How to use it?

> Change CHOICE to 'youtube' or 'vlc'    
> Change WEB_CAM_SOURCE to your webcam Source
> Change swipe option to True (TO enable Advance control)

> ```
> from HAND_GESTURE_MEDIAPLAYER_CONTROLER import YT_VLC_CONTROL_HAND_TRACKING
> 
> if __name__ == "__main__":
>   app = MediaPlayer_GestureRecognition(CHOICE='vlc')
>   app.start()
> ```

# Demo 
 Youtube video - https://youtu.be/aR4TvTsH3vs

# Sources
> [Mediapipe](https://google.github.io/mediapipe/solutions/hands.html)
