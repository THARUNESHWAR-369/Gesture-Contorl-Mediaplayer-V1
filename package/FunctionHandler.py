
import time
import pyautogui

class FUNCTION_HANDLER:

    __CONFIDENCE = 0.687644321
    __VIEWS_PATH = r"E:\tharun2\advance gesture control (CV)\images\views.PNG"
    __SKIP_ADS_PATH = r"E:\tharun2\advance gesture control (CV)\images\skip_ads.PNG"

    def __init__(self, choice = '', delay = 0.0, pos=0) -> None:
        self.__CHOICE = choice
        print(self.__CHOICE)
        self.__DELAY = delay
        pyautogui.FAILSAFE = False

    def __clickOnTheScreen(self, CHOICE):
        if CHOICE == "youtube":
            __VIEWS = pyautogui.locateOnScreen(f"{self.__VIEWS_PATH}", 
                                    confidence=self.__CONFIDENCE)
            if __VIEWS == None:
                return None
            else:
                __LEFT, __TOP, __WIDHT, __HEIGHT = __VIEWS
                return __LEFT + __HEIGHT, __TOP + (__HEIGHT // 2) 
        return None

    def run_play_pause(self) -> str:
        if self.__CHOICE == 'youtube':
            time.sleep(self.__DELAY)
            pyautogui.press('space')
        if self.__CHOICE == 'vlc':
            pyautogui.press("space")
        return "PLAY/PAUSE"
      
    
    def fullScreen(self) -> str:
        if self.__CHOICE == 'youtube':
            time.sleep(self.__DELAY)
            pyautogui.press('f')
        if self.__CHOICE == 'vlc':
            pyautogui.press("f")
        return "FULL SCREEN"
    
    def forward(self) -> str:
        if self.__CHOICE == 'youtube':
            time.sleep(self.__DELAY)
            pyautogui.press('right')
        if self.__CHOICE == 'vlc':
            pyautogui.press("right")
        return "FORWARD"

    def backward(self) -> str:
        if self.__CHOICE == 'youtube':
            time.sleep(self.__DELAY)
            pyautogui.press('left')
        if self.__CHOICE == 'vlc':
            pyautogui.press("left")
        return "BACKWARD"
    
    def vol_inc(self) -> str:
        if self.__CHOICE == 'youtube':
            time.sleep(self.__DELAY)
            pyautogui.press('up')
        if self.__CHOICE == 'vlc':
            pyautogui.press("up")
        return "VOLUME INCREASE"

    def vol_dec(self) -> str:
        if self.__CHOICE == 'youtube':
            time.sleep(self.__DELAY)
            pyautogui.press('down')
        if self.__CHOICE == 'vlc':
            pyautogui.press("down")
        return "VOLUME DECREASE"
    
    def skip_ads(self) -> str:
        __SKIPADS = pyautogui.locateOnScreen(f"{self.__SKIP_ADS_PATH}", 
                                    confidence=self.__CONFIDENCE)
        if __SKIPADS == None:
            return "No skip Ads Found"
        else:
            __LEFT, __TOP, __WIDHT, __HEIGHT = __SKIPADS
            pyautogui.click(x=__LEFT + __HEIGHT, 
            y=__TOP + (__HEIGHT // 2) )
            return "SKIP ADS"