# -*- coding: UTF-8 -*-
'''
Auto registration script for dropbox.
Takes username and password from stdin. The parameters must each end in newlines ("\n").
Opens firefox, navigates to dropbox.com, enters registration details, and selects the Free Plan Option.
Works for English and German interface.

Created on Aug 5, 2014

@author: joe
'''
from time import sleep
from sikuli.Sikuli import Screen, App, Key, addImagePath, Settings, popup
import time
import sys
import os
import subprocess
Settings.MoveMouseDelay = 0
SUPPORTED_LANGUAGES = ['english','german']
dbRegistrationBtn = "Registration_Btn.png"
firstNameInput = "First_Name_Input.png"
def configure_language():
    '''Set the correct images according to the language of the website in the current browser window.
    :return: True iff successful'''
    global dbRegistrationBtn, firstNameInput
    for lang in SUPPORTED_LANGUAGES:
        for tries in range(3):
            if screen.exists(lang+'/'+dbRegistrationBtn,2):
                dbRegistrationBtn = lang + '/' + dbRegistrationBtn
                firstNameInput = lang +'/' + firstNameInput
                return True
    return False

def start_browser(url):
    try:
        subprocess.Popen(['xdg-open', url])
    except OSError:
        print 'Opening the browser failed'

if __name__ == '__main__':
    #read username and password from stdin
    time.sleep(1) #wait 
    user = sys.stdin.readline()
    pwd = sys.stdin.readline()
    #Add path to where images shall be searched at
    ABS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    addImagePath(ABS_PATH+"/images/dropbox")
    # Start browser
    start_browser("http://www.dropbox.com")
    screen = Screen()
    successful = configure_language()
    if not successful:
        popup("Automatic registration at Dropbox failed for one of the following reasons.\n"+
              "Otherwise you can report an issue at https://github.com/joe42/CloudFusion/issues.\n"+
              "1. Firefox is not installed\n"+
              "2. You were already logged in to Dropbox\n"+
              "3. Your browser language settings are neither German nor English\n"+
              "4. Your browser is open in a different workspace\n", 
              "Error")
    screen.click(dbRegistrationBtn)
    if screen.exists(firstNameInput,2):
        screen.click(firstNameInput)
    screen.paste("John")
    screen.type(Key.TAB)
    screen.paste("Smith")
    screen.type(Key.TAB)
    screen.paste(user)
    screen.type(Key.TAB)
    screen.paste(pwd)
    screen.type(Key.TAB)
    screen.type(Key.SPACE)
    screen.click(dbRegistrationBtn)
    start_browser("http://www.dropbox.com")
