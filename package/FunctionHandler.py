
import time
import pyautogui

class FUNCTION_HANDLER:
    def __init__(self, choice = '', delay = 0.0, pos=0):
        self.choice = choice
        print(self.choice)
        self.play_pause_c, self.full_screen_c, self.vol_up, self.vol_down, self.ford, self.backd = 0, 0, 0, 0, 0, 0
        self.YT_THRESH = 55
        self.screen_width, self.screen_height = pyautogui.size()
        self.DELAY = delay
        self.pos = pos

    def run_play_pause(self):
        self.play_pause_c += 1
        #print(self.play_pause_c, self.choice)
        if self.play_pause_c == 1:
            if self.choice == 'yotube':
                try:
                    pyautogui.click(x=self.screen_width//2, y=self.screen_height//2)
                except:
                    pyautogui.press('k')
            if self.choice == 'vlc':
                pyautogui.press("space")
            time.sleep(self.DELAY)
        if self.play_pause_c > 1:
            self.play_pause_c = -1
        time.sleep(self.DELAY)
        return "PLAY/PAUSE"
    
    def fullPageMode(self):
        self.full_screen_c += 1
        if self.full_screen_c == 1:
            try:
                pyautogui.press('f')
            except:
                pyautogui.press('f')
            time.sleep(self.DELAY)
        if self.full_screen_c > 1:
            self.full_screen_c = -1
        time.sleep(self.DELAY)
        return "FUll SCREEN/FUll SCREEN EXIT"
    
    def forward(self):
        self.ford += 1
        if self.ford == 1:
            try:
                pyautogui.press('right')
            except:
                pyautogui.press('right')
            time.sleep(self.DELAY)
        if self.ford > 1:
            self.ford = -1
        time.sleep(self.DELAY)
        return 'FORWARD'
    
    def backward(self):
        self.backd += 1
        if self.backd == 1:
            try:
                pyautogui.press('left')
            except:
                pyautogui.press('left')
            time.sleep(self.DELAY)
        if self.backd > 1:
            self.backd = -1
        time.sleep(self.DELAY)
        return 'BACKWARD'
    
    def vol_dec_yt(self):
        self.vol_down += 1
        if self.vol_down == 1:
            try:
                pyautogui.press('down')
            except:
                pyautogui.press('down')
            time.sleep(self.DELAY)
        if self.vol_down > 1:
            self.vol_down = -1
        time.sleep(self.DELAY)
        return 'VOLUME DECREASED'
    
    def vol_inc_yt(self):
        self.vol_up += 1
        if self.vol_up == 1:
            try:
                pyautogui.press('up')
            except:
                pyautogui.press('up')
            time.sleep(self.DELAY)
        if self.vol_up > 1:
            self.vol_up = -1
        time.sleep(self.DELAY)
        return 'VOLUME INCREASED'
        
    def forward_v2(self):
        try:
            pyautogui.press('right')
        except:
            pyautogui.press('right')
        time.sleep(self.DELAY)
        return 'FORWARD'
    
    def backward_v2(self):
        try:
            pyautogui.press('left')
        except:
            pyautogui.press('left')
        time.sleep(self.DELAY)
        return 'BACKWARD'
    
    def vol_inc_yt_v2(self):
        try:
            pyautogui.press('up')
        except:
            pyautogui.press('up')
        time.sleep(self.DELAY)
        return 'VOLUME INCREASED'
    
    def vol_dec_yt_v2(self):
        try:
            pyautogui.press('down')
        except:
            pyautogui.press('down')
        time.sleep(self.DELAY)
        return 'VOLUME DECREASED'
