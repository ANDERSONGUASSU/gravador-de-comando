import time
from PyQt5.QtCore import QObject, pyqtSignal
from pynput import mouse, keyboard
import pyautogui
from src.events.mouse_events import MouseEventsHandler
from src.events.keyboard_events import KeyboardEventsHandler
from src.utils.file_operations import save_events, load_events
import os
from pynput.keyboard import GlobalHotKeys

class Recorder(QObject):
    status_changed = pyqtSignal(str)
    repeats_changed = pyqtSignal(int)
    record_button_state_changed = pyqtSignal(bool)
    stop_button_state_changed = pyqtSignal(bool)
    play_button_state_changed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.mouse_events_handler = MouseEventsHandler()
        self.keyboard_events_handler = KeyboardEventsHandler()
        self.recording = False
        self.repeats = 1  # Inicialmente, repetições definidas como 1

    def set_repeats_spinbox(self, repeats_spinbox):
        self.repeats_spinbox = repeats_spinbox
        self.repeats_spinbox.valueChanged.connect(self.set_repeats)
        self.repeats = self.repeats_spinbox.value()

    def set_repeats(self, repeats):
        self.repeats = repeats
        self.repeats_changed.emit(self.repeats)
        
    def setup_hotkeys(self):
        hotkeys = GlobalHotKeys({
            '<ctrl>+<alt>+r': self.start_recording,
            '<ctrl>+<alt>+s': self.stop_recording,
            '<ctrl>+<alt>+p': self.play_recording
        })
        hotkeys.start()
        print("Hotkeys set up: Record (<ctrl>+<alt>+r), Stop (<ctrl>+<alt>+s), Play (<ctrl>+<alt>+p)")

    def start_recording(self):
        self.recording = True
        self.mouse_events_handler.start()
        self.keyboard_events_handler.start()

        self.status_changed.emit('Recording...')
        self.record_button_state_changed.emit(False)
        self.stop_button_state_changed.emit(True)
        self.play_button_state_changed.emit(False)
        print("Recording started")

    def stop_recording(self):
        self.recording = False
        self.mouse_events_handler.stop()
        self.keyboard_events_handler.stop()

        print(f"Mouse events captured: {self.mouse_events_handler.events}")
        print(f"Keyboard events captured: {self.keyboard_events_handler.events}")

        save_events('mouse_events.pkl', self.mouse_events_handler.events)
        save_events('keyboard_events.pkl', self.keyboard_events_handler.events)

        self.status_changed.emit('Recording stopped')
        self.record_button_state_changed.emit(True)
        self.stop_button_state_changed.emit(False)
        self.play_button_state_changed.emit(True)
        print("Recording stopped and events saved")

    def play_recording(self):
        if not os.path.exists('mouse_events.pkl') or not os.path.exists('keyboard_events.pkl'):
            self.status_changed.emit('No recorded events to play')
            print("No recorded events to play")
            return

        # Obtém o número de repetições do QSpinBox
        self.repeats = self.repeats_spinbox.value()

        self.status_changed.emit(f'Playing... Repeats: {self.repeats}')

        mouse_events = load_events('mouse_events.pkl')
        keyboard_events = load_events('keyboard_events.pkl')

        for _ in range(self.repeats):
            self._play_mouse_events(mouse_events)
            self._play_keyboard_events(keyboard_events)

        self.status_changed.emit('Playback finished')
        print("Playback finished")



    def _play_mouse_events(self, events):
        if events:
            start_time = events[0][1]
            for event in events:
                event_type, event_time, *details = event
                time.sleep(event_time - start_time)
                start_time = event_time

                if event_type == 'click':
                    x, y, button = details
                    pyautogui.click(x, y, button=button.name)
                # Add other event types (move, scroll) handling if needed

    def _play_keyboard_events(self, events):
        if events:
            start_time = events[0][1]
            for event in events:
                event_type, event_time, key = event
                time.sleep(event_time - start_time)
                start_time = event_time

                if event_type == 'press':
                    try:
                        pyautogui.press(key)
                    except KeyError:
                        pyautogui.press(key.name)
                elif event_type == 'release':
                    pass

