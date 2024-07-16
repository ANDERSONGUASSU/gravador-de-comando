from pynput import keyboard
import time

class KeyboardEventsHandler:
    def __init__(self):
        self.events = []
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def start(self):
        self.events = []
        self.listener.start()
        print("Keyboard listener started")

    def stop(self):
        self.listener.stop()
        print("Keyboard listener stopped")
        print(f"Captured keyboard events: {self.events}")

    def on_press(self, key):
        try:
            event = ('press', time.time(), key.char)
        except AttributeError:
            event = ('press', time.time(), key)
        self.events.append(event)
        print(f"Keyboard press event: {event}")

    def on_release(self, key):
        try:
            event = ('release', time.time(), key.char)
        except AttributeError:
            event = ('release', time.time(), key)
        self.events.append(event)
        print(f"Keyboard release event: {event}")
