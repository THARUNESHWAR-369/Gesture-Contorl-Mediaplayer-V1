import mediapipe as mp
import cv2
from .COLORS import COLORS_ as COLORS
import random
import math


        

class HAND_TRACKING:

    BOUNDRY_COLROS = [COLORS.RED,
                      COLORS.PINK,
                      COLORS.GREEN,
                      COLORS.YELLOW,
                      COLORS.WHITE]
    BOUNDR_FANCY_COLOR = (0, 0, 0)

    RADIUS = 5

    BOUNDRY_THRESH = 20
    FANCY_THRESH = 30
    FANCY_THRESH_BORDER = 15

    BOUNDRY_THICKNESS = 1
    LINE_THICKNESS = 1
    FANCY_THICKNESS = 10

    TIP_NO = [4, 8, 12, 16, 20]
    LINES = [[0, 17],
             [17, 20],
             [0, 13],
             [13, 16],
             [0, 9],
             [9, 12],
             [0, 5],
             [5, 8],
             [0, 2],
             [2, 4]]
        
    def __init__(self, min_detection_confidence = 0.5, 
                 min_tracking_confidence = 0.5,
                 mode = False,
                 maxHands = 1):

        mp_hands = mp.solutions.hands
        
        self.mode = mode
        self.maxHands = maxHands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.tipIds = [4, 8, 12, 16, 20]
        
        self.hands = mp_hands.Hands(min_detection_confidence=self.min_detection_confidence, 
                            min_tracking_confidence=self.min_tracking_confidence,
                            max_num_hands=self.maxHands,
                            static_image_mode=self.mode)
        
    def getKeyPointsWithFrame(self, 
                              image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        self.results = self.hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)     
        return image
    
    def findPosition(self,
                     img,
                     handNo = 0):
             
        self.lmList = []
        lmlist2 = []
        XList, YList = [], []
        bbox = ()
        area = 0
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                XList.append(cx)
                YList.append(cy)
                self.lmList.append([id, cx, cy])
            xmin, xmax = min(XList), max(XList)
            ymin, ymax = min(YList), max(YList)
            bbox = (xmin, 
                    ymin,
                    xmax,
                    ymax)
            
            area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
            
        return self.lmList, bbox, area,# lmlist2

    def draw(self, 
             img = None,
             bbox = None,
             draw_boundry=False,
             draw_hand = False,
             draw_fancy = False,
             fancy_type = 'fancy_borderless'):
        
        """
        if draw_fancy == True
        fancy_type = [fancy_borderless, fancy_with_border]
        """
        
        if fancy_type == "fancy_borderless":
            draw_boundry = False
        
        if fancy_type == "fancy_with_border":
            draw_boundry = True
        
        def get_colors(l1=None,
               l2=None,
               color_mode='', 
               tip_no=None):
            COLOR = (255, 255, 255)
            if color_mode == 'line':
                if l1 == 0 \
                and l2 == 17:                
                    COLOR = COLORS.RED
                if l1 == 17 \
                and l2 == 20:
                    COLOR = COLORS.RED
                if l1 == 0 \
                and l2 == 13:
                    COLOR = COLORS.PINK
                if l1 == 13 \
                and l2 == 16:
                    COLOR =COLORS.PINK
                if l1 == 0 \
                and l2 == 9:
                    COLOR = COLORS.GREEN
                if l1 == 9 \
                and l2 == 12:
                    COLOR = COLORS.GREEN
                if l1 == 0 \
                and l2 == 5:
                    COLOR = COLORS.YELLOW
                if l1 == 5 \
                and l2 == 8:
                    COLOR = COLORS.YELLOW
                if l1 == 0 \
                and l2 == 2:
                    COLOR = COLORS.WHITE
                if l1 == 2 \
                and l2 == 4:
                    COLOR = COLORS.WHITE
                return COLOR
            
            if color_mode == 'tip':
                if tip_no == 20:
                    COLOR = COLORS.RED
                if tip_no == 16:
                    COLOR = COLORS.PINK
                if tip_no == 12:
                    COLOR = COLORS.GREEN
                if tip_no == 8:
                    COLOR = COLORS.YELLOW
                if tip_no == 4:
                    COLOR = COLORS.WHITE
                return COLOR
    
        def get_random_boundry_color():
            return random.choice(self.BOUNDRY_COLROS)
        
        BOUNDR_FANCY_COLOR = get_random_boundry_color()
        
        if draw_boundry:
            x, y, w, h = bbox
           
            cv2.rectangle(img, 
                        (x - self.BOUNDRY_THRESH, y - self.BOUNDRY_THRESH),
                        (w + self.BOUNDRY_THRESH, h + self.BOUNDRY_THRESH),
                        BOUNDR_FANCY_COLOR,
                        self.BOUNDRY_THICKNESS)
        
        if draw_fancy:
            if fancy_type == 'fancy_borderless':
                x, y, w, h = bbox
                x -= self.BOUNDRY_THRESH
                y -= self.BOUNDRY_THRESH
                w += self.BOUNDRY_THRESH
                h += self.BOUNDRY_THRESH
                            
                """
                Top left
                """
                cv2.line(img,
                        (x, y), 
                        (x + self.FANCY_THRESH, y),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                cv2.line(img, 
                        (x, y), 
                        (x, y + self.FANCY_THRESH),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                
                """
                Top right
                """
                cv2.line(img,
                        (w - self.BOUNDRY_THRESH - self.FANCY_THICKNESS, y),
                        (w, y),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
                cv2.line(img, (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2, y),
                        (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2, y + self.FANCY_THRESH),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
                
                """
                Bottom left
                """
                cv2.line(img,
                        (x, h), 
                        (x + self.BOUNDRY_THRESH, h),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                cv2.line(img, 
                        (x, h),
                        (x, h - self.BOUNDRY_THRESH),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                
                """
                Bottom right
                """
                cv2.line(img,
                        (w - self.BOUNDRY_THRESH - self.FANCY_THICKNESS, h),
                        (w, h),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
                cv2.line(img, (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2, h),
                        (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2, h - self.FANCY_THRESH),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
            
            if fancy_type == 'fancy_with_border':
                x, y, w, h = bbox
                x -= self.BOUNDRY_THRESH
                y -= self.BOUNDRY_THRESH
                w += self.BOUNDRY_THRESH
                h += self.BOUNDRY_THRESH
                            
                """
                Top left
                """
                cv2.line(img,
                        (x - self.FANCY_THRESH_BORDER, y - self.FANCY_THRESH_BORDER),
                        (x + self.FANCY_THRESH, y - self.FANCY_THRESH_BORDER),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                cv2.line(img, 
                        (x - self.FANCY_THRESH_BORDER, y - self.FANCY_THRESH_BORDER),
                        (x - self.FANCY_THRESH_BORDER, y + self.FANCY_THRESH),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                
                """
                Top right
                """
                cv2.line(img,
                        (w - self.BOUNDRY_THRESH - self.FANCY_THRESH + self.FANCY_THRESH_BORDER, y - self.FANCY_THRESH_BORDER),
                        (w + self.FANCY_THRESH_BORDER, y - self.FANCY_THRESH_BORDER),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
                cv2.line(img,
                        (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2 + self.FANCY_THRESH_BORDER, y - self.FANCY_THRESH_BORDER),
                        (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2 + self.FANCY_THRESH_BORDER, y + self.FANCY_THRESH),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
                
                """
                Bottom left
                """
                cv2.line(img,
                        (x - self.FANCY_THRESH_BORDER, h + self.FANCY_THRESH_BORDER),
                        (x + self.FANCY_THRESH, h + self.FANCY_THRESH_BORDER),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                cv2.line(img, 
                        (x - self.FANCY_THRESH_BORDER, h - self.FANCY_THRESH_BORDER*2),
                        (x - self.FANCY_THRESH_BORDER, h + self.FANCY_THRESH_BORDER),
                        BOUNDR_FANCY_COLOR, 
                        self.FANCY_THICKNESS)
                
                """
                Bottom right
                """
                cv2.line(img,
                        (w - self.BOUNDRY_THRESH - self.FANCY_THRESH + self.FANCY_THRESH_BORDER, h + self.FANCY_THRESH_BORDER),
                        (w + self.FANCY_THRESH_BORDER, h + self.FANCY_THRESH_BORDER),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
                cv2.line(img, 
                        (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2 + self.FANCY_THRESH_BORDER, h - self.FANCY_THRESH_BORDER*2),
                        (w + self.BOUNDRY_THRESH - self.FANCY_THICKNESS*2 + self.FANCY_THRESH_BORDER, h + self.FANCY_THRESH_BORDER),
                        BOUNDR_FANCY_COLOR,
                        self.FANCY_THICKNESS)
            
        if draw_hand:
            """
            Draw Lines
            """
            for l1, l2 in self.LINES:
                x1, y1 = self.lmList[l1][1], \
                    self.lmList[l1][2]
                x2, y2 = self.lmList[l2][1],\
                    self.lmList[l2][2]
                LINE_COLOR = get_colors(l1=l1,
                                        l2=l2, 
                                        color_mode = 'line')
                cv2.line(img, 
                            (x1, y1),
                            (x2, y2),
                            LINE_COLOR,
                            self.LINE_THICKNESS)
        
                """
                Draw Circle on Tip of the Finger
                """
                for tip in self.TIP_NO:
                    TIP_COLOR = get_colors(l1=l1,
                                        l2=l2,
                                        color_mode = 'tip', 
                                        tip_no=tip)
                    x, y = self.lmList[tip][1], \
                        self.lmList[tip][2]
                    cv2.circle(img,
                                (x, y),
                                self.RADIUS,
                                TIP_COLOR,
                                cv2.FILLED)       
        
        return img, BOUNDR_FANCY_COLOR
            
    def fingersUp(self):
        fingers = []
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
    
    def findDegree(self):
        x1, y1 = self.lmList[0][1], self.lmList[0][2]
        x2, y2 = self.lmList[12][1], self.lmList[12][2]
        atan2 = math.atan2(y2 - y1, x2 - x1)
        return math.degrees(atan2)
    
    def getFindegCordinate(self,
                           lmList,
                           fingerNo):
        x1, y1 = lmList[fingerNo][1:]
        return (x1, y1)
    
    def findDistance(self,
                     p1, 
                     p2, 
                     img,
                     draw=True,
                     r=15,
                     t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, 
                     (x1, y1), 
                     (x2, y2), 
                     (255, 0, 255), 
                     t)
            cv2.circle(img, 
                       (x1, y1),
                       r,
                       (255, 0, 255), 
                       cv2.FILLED)
            cv2.circle(img,
                       (x2, y2),
                       r, 
                       (255, 0, 255), 
                       cv2.FILLED)
            cv2.circle(img,
                       (cx, cy), 
                       r, 
                       (0, 0, 255), 
                       cv2.FILLED)
            length = math.hypot(x2 - x1, 
                                y2 - y1)

        return length, img, [x1,
                             y1,
                             x2,
                             y2,
                             cx, 
                             cy]
    
    
