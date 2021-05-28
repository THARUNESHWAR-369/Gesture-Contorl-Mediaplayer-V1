from HAND_GESTURE_MEDIAPLAYER_CONTROLER import YT_VLC_CONTROL_HAND_TRACKING

if __name__ == "__main__":
    controler = YT_VLC_CONTROLL_HAND_TRACKING(CHOICE='vlc', WEB_CAM_SOURCE=0)
    controler.start()