import os
import subprocess as sp 
from PIL import ImageGrab 
from decouple import config
from mouseinfo import screenshot
from bs4 import BeautifulSoup
import requests

from action.screenrecord import record_screen, stop_recording
import threading
#from aim.vision import describe_image
from speech_.TTS import *
from speech_.STT import *
import webbrowser
import pyautogui
import numpy as np
import cv2




programs = {
    'notepad': "Shortcuts\\Notepad++.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'word': "Shortcuts\\Word.lnk",
    'excel': "Shortcuts\\Excel.lnk",
    'powerpoint': "Shortcuts\\PowerPoint.lnk",
    'edge': "Shortcuts\\Microsoft Edge.lnk",
    'chrome': "Shortcuts\\Google Chrome.lnk",
    'sticky notes': "Shortcuts\\Sticky Notes (new).lnk"
}


def open_browser():
    os.startfile(programs['edge'])

        
def open_stickynotes():
    os.startfile(programs['sticky notes'])


def action_search(search):
    webbrowser.open("https://www.bing.com/search?q=" + search)

def open_notepad():
    os.startfile(programs['notepad'])

def open_word():
    os.startfile(programs['word'])

def open_excel():
    os.startfile(programs['excel'])

def open_ppt():
    os.startfile(programs['powerpoint'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    os.startfile(programs['calculator'])

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def youtube_search(search):
    webbrowser.open("https://www.youtube.com/results?search_query=" + search)

def open_youtube():
    webbrowser.open("https://www.youtube.com/")


def take_screenshot():
    screenshot_file = "image.png"
    image = pyautogui.screenshot("image.png")
    TTS("Screenshot saved as " + screenshot_file)

def start_screen_record():
    recording_thread = threading.Thread(target=record_screen)
    recording_thread.start()

def stop_screen_record():
    stop_recording()


