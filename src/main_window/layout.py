from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget, QSpinBox

def setup_ui(main_window, recorder):
    main_window.setWindowTitle('Mouse and Keyboard Recorder')

    layout = QVBoxLayout()

    main_window.status_label = QLabel('Press "Start Recording" to begin')
    layout.addWidget(main_window.status_label)

    main_window.record_button = QPushButton('Start Recording')
    main_window.record_button.clicked.connect(recorder.start_recording)
    layout.addWidget(main_window.record_button)

    main_window.stop_button = QPushButton('Stop Recording')
    main_window.stop_button.clicked.connect(recorder.stop_recording)
    main_window.stop_button.setEnabled(False)
    layout.addWidget(main_window.stop_button)

    main_window.play_button = QPushButton('Play Recording')
    main_window.play_button.clicked.connect(recorder.play_recording)
    main_window.play_button.setEnabled(False)
    layout.addWidget(main_window.play_button)
    
    main_window.repeats_spinbox = QSpinBox()
    main_window.repeats_spinbox.setMinimum(1)  # Definir um mínimo adequado
    main_window.repeats_spinbox.setMaximum(999999)
    main_window.repeats_spinbox.setValue(1)    # Valor inicial
    layout.addWidget(main_window.repeats_spinbox)

    container = QWidget()
    container.setLayout(layout)
    main_window.setCentralWidget(container)
    
    recorder.set_repeats_spinbox(main_window.repeats_spinbox)
    # Connect status label to recorder signals
    recorder.status_changed.connect(main_window.status_label.setText)
    recorder.record_button_state_changed.connect(main_window.record_button.setEnabled)
    recorder.stop_button_state_changed.connect(main_window.stop_button.setEnabled)
    recorder.play_button_state_changed.connect(main_window.play_button.setEnabled)
    recorder.repeats_changed.connect(main_window.repeats_spinbox.setValue)

    # Set up global hotkeys
    recorder.setup_hotkeys()
    
    
