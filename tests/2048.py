#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def play():
    
    bs = webdriver.Firefox()
    bs.get('https://gabrielecirulli.github.io/2048/')
    html = bs.find_element_by_tag_name('html')

    while True:
        print('send up, right, down, left')
        html.send_keys(Keys.UP)
        time.sleep(0.3)
        html.send_keys(Keys.RIGHT)
        time.sleep(0.3)
        html.send_keys(Keys.DOWN)
        time.sleep(0.3)
        html.send_keys(Keys.LEFT)
        time.sleep(0.3)

        game_over = bs.find_element_by_css_selector('.game-message>p')
        if game_over.text == 'Game over!':
            score = bs.find_element_by_class_name('score-container')
            print('game over, score is %s' % score.text)
            print('wait 3 seconds, try again')
            time.sleep(3)
            try_again = bs.find_element_by_class_name('retry-button')
            try_again.click()

if __name__ == '__main__':
    play()
