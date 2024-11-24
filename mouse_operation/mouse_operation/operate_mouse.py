#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui
import time


def move_cursor():
    # Display size
    print(pyautogui.size())

    # Move to target position
    pyautogui.moveTo(500, 600, 0.8, pyautogui.easeOutQuad)
    time.sleep(0.3)
    pyautogui.moveTo(700, 200, 0.8, pyautogui.easeOutQuad)