from pynput import mouse
import time


class MouseEventsHandler:
    def __init__(self):
        self.events = []
        self.listener = None  # Inicialmente o listener é None

    def start(self):
        if self.listener is None:
            self.listener = mouse.Listener(on_click=self.on_click)
            self.listener.start()
            print("Mouse listener started")
        else:
            print("Mouse listener is already running")

    def stop(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
            print("Mouse listener stopped")
            print(f"Captured mouse events: {self.events}")
        else:
            print("Mouse listener is not running")

    def on_click(self, x, y, button, pressed):
        if pressed:  # Capture only when button is pressed (not released)
            event = ('click', time.time(), x, y, button)
            self.events.append(event)
            print(f"Mouse click event: {event}")
