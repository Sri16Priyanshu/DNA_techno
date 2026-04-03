# Simple AI placeholder

def detect_stress(data):
    if data.get("screen_time", 0) > 8:
        return "High Stress"
    return "Normal"
