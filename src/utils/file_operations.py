import pickle


def save_events(filename, events):
    with open(filename, 'wb') as f:
        pickle.dump(events, f)
    print(f"Events saved to {filename}")


def load_events(filename):
    with open(filename, 'rb') as f:
        events = pickle.load(f)
    print(f"Events loaded from {filename}")
    return events
