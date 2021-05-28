import cv2
import random
import imutils

from package.HANDS import HAND_TRACKING
from package.COLORS import COLORS_ as COLORS
from package.FunctionHandler import FUNCTION_HANDLER

class YT_VLC_CONTROL_HAND_TRACKING:
    """
    WebCam sources
    """
    mobile_web_cam_url = 'https://192.168.0.100:8080/video'
    hCam, wCam = 600, 600
    START_CAM = True
    ESCAPE = 'q'
    frame = None
    
    """
    OpenCv text font style
    """
    TEXT_FONT = cv2.FONT_HERSHEY_PLAIN
    
    """
    Play Pause Action index
    """
    PLAY_PAUSE_INDEX = -1
    
    """
    Current action
    """
    CURRENT_ACTION = "NONE"
    CURRENT_ACTION_COLOR = [COLORS.RED,
                    COLORS.PINK,
                    COLORS.GREEN,
                    COLORS.YELLOW,
                    COLORS.WHITE]#(209,239,173)
    CURRENT_ACTION_COORDINATES = (30, 30)
    CURRENT_ACTION_TEXT_THICKNESS = 2
    CURRENT_ACTION_TEXT_FONTSCALE = 1
    
    """
    Min and Max Degree
    """
    DEGREE_MIN = -130
    DEGREE_MAX = -60
    
    """
    Max and Min area of hand
    """
    MAX_AREA = 900
    MIN_AREA = 100
        
    def __init__(self, CHOICE = 'youtube', WEB_CAM_SOURCE = 0):
        print("[~] INITIALISING...")
        """
        Init
        """ 
        self.CHOICE = CHOICE
        self.WEB_CAM_SOURCE = WEB_CAM_SOURCE
        
        """
        Hand tracking module inputes
        """
        self.MIN_DETECTION_CONFIDENCE = 0.75
        self.MAX_HAND = 1
        self.MIN_TRACKING_CONFIDENCE = 0.5

        """
        Initialise Modules
        """
        print("[~] INITIALISING WEBCAM....")
        ###WebCam input
        self.cap = cv2.VideoCapture(self.WEB_CAM_SOURCE)
        self.cap.set(3, self.wCam)
        self.cap.set(4, self.hCam)
        self.hand_track = HAND_TRACKING(min_detection_confidence=self.MIN_DETECTION_CONFIDENCE,
                                maxHands=self.MAX_HAND,
                                min_tracking_confidence=self.MIN_TRACKING_CONFIDENCE)
        self.fuct_hdl = FUNCTION_HANDLER(choice=self.CHOICE)

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def check_choice(self):
        if self.CHOICE in ['youtube', 'vlc']:
            return True
        if self.CHOICE not in ['youtube', 'vlc']:
            return False


    def start(self):
        VALID_CHOICE = self.check_choice()
        if VALID_CHOICE:
            print("\t[~] STARTING WEBCAM....\n")
            while self.START_CAM:
                s, self.frame = self.cap.read()
                self.frame = imutils.resize(self.frame, width=600)

                if not s:
                    print('[~] Check WebCam.')

                self.frame = cv2.flip(self.frame, 1)

                self.frame = self.hand_track.getKeyPointsWithFrame(image=self.frame)
                lmList, bbox, area = self.hand_track.findPosition(img = self.frame)

                """
                If Hand Detected!
                """
                if len(lmList) != 0:
                    self.frame, self.FRAME_RECTANGLE_COLOR = self.hand_track.draw(img = self.frame,
                                                 bbox = bbox,
                                                 draw_boundry = False,
                                                 draw_hand = True,
                                                 draw_fancy = True,
                                                 fancy_type='fancy_borderless')

                    """
                    List of Fingers
                    1 - Up
                    0 - Down
                    """
                    fingerDown = self.hand_track.fingersUp()

                    """
                    If Degree is in range of -130 to -60.
                    """
                    degree = int(self.hand_track.findDegree())

                    #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    print(f"[~](LOG): FINGER UP/DOWN: {fingerDown}, AREA: {area}, DEGREE: {degree}, LAST ACTION: {self.CURRENT_ACTION}")
                    #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                    if area > self.MIN_AREA\
                    and area < self.MAX_AREA \
                    and self.DEGREE_MIN < degree < self.DEGREE_MAX:

                        """
                        POSITION
                        [1, 1, 1, 1, 1]
                        """
                        if fingerDown[0] == 1 \
                        and fingerDown[1] == 1 \
                        and fingerDown[2] == 1 \
                        and fingerDown[3] == 1 \
                        and fingerDown[4] == 1:
                            self.CURRENT_ACTION = None

                        """
                        PAUSE, PLAY
                        [1, 1, 1, 1, 0]
                        """
                        if not fingerDown[self.PLAY_PAUSE_INDEX] \
                        and fingerDown[self.PLAY_PAUSE_INDEX + 1] == 1 \
                        and fingerDown[self.PLAY_PAUSE_INDEX + 2] == 1 \
                        and fingerDown[self.PLAY_PAUSE_INDEX + 3] == 1 \
                        and fingerDown[self.PLAY_PAUSE_INDEX + 4] == 1:
                            self.CURRENT_ACTION = self.fuct_hdl.run_play_pause()

                        """
                        FULL PAGE MODE AND ESCAPE
                        [0, 0, 0, 0, 0]
                        """
                        if fingerDown[0] == 0 \
                        and fingerDown[1] == 0 \
                        and fingerDown[2] == 0 \
                        and fingerDown[3] == 0 \
                        and fingerDown[4] == 0:
                            self.CURRENT_ACTION = self.fuct_hdl.fullPageMode()

                        """
                        FORWARD
                        [0, 1, 1, 0, 0]
                        """
                        if fingerDown[0] == 0 \
                        and fingerDown[1] == 1 \
                        and fingerDown[2] == 1 \
                        and fingerDown[3] == 0 \
                        and fingerDown[4] == 0:
                            self.CURRENT_ACTION = self.fuct_hdl.backward()

                        """
                        BACKWARD
                        [1, 1, 1, 0, 0]
                        """
                        if fingerDown[0] == 1 \
                        and fingerDown[1] == 1 \
                        and fingerDown[2] == 1 \
                        and fingerDown[3] == 0 \
                        and fingerDown[4] == 0:
                            self.CURRENT_ACTION = self.fuct_hdl.forward()

                        """
                        VOLUME DECREASE
                        [0, 0, 1, 1, 0]
                        """
                        if fingerDown[0] == 0 \
                        and fingerDown[1] == 0 \
                        and fingerDown[2] == 1 \
                        and fingerDown[3] == 1 \
                        and fingerDown[4] == 0:
                            self.CURRENT_ACTION = self.fuct_hdl.vol_dec_yt()

                        """
                        VOLUME INCREASE
                        [0, 0, 1, 1, 0]
                        """
                        if fingerDown[0] == 1 \
                        and fingerDown[1] == 1 \
                        and fingerDown[2] == 0 \
                        and fingerDown[3] == 0 \
                        and fingerDown[4] == 1:
                            self.CURRENT_ACTION = self.fuct_hdl.vol_inc_yt()

                """
                Show the Last action
                """
                cv2.putText(img = self.frame,
                            text = f"{self.CURRENT_ACTION}",
                            org = self.CURRENT_ACTION_COORDINATES,
                            fontFace = self.TEXT_FONT,
                            fontScale = self.CURRENT_ACTION_TEXT_FONTSCALE,
                            color = random.choice(self.CURRENT_ACTION_COLOR),
                            thickness = self.CURRENT_ACTION_TEXT_THICKNESS)

                """
                Display the Frame.
                """
                cv2.imshow("LIVE...",
                           self.frame)

                """
                Check for exit
                """
                self.check_exit()

        if not VALID_CHOICE:
            print('\n\n\t[!] Enter correct Choice [youtube/vlc]\n\n')
            try:quit()
            except:exit()

    def check_exit(self):
        if cv2.waitKey(1) == ord(self.ESCAPE):
            self.START_CAM = False


