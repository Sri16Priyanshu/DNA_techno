from flask import Flask, request, jsonify

app = Flask(__name__)

def detect_stress(data):
    score = 0

    if data.get("screen_time", 0) > 8:
        score += 1
    if data.get("sleep_hours", 0) < 6:
        score += 1
    if data.get("typing_speed_drop", False):
        score += 1

    if score >= 2:
        return "High Stress"
    elif score == 1:
        return "Moderate Stress"
    return "Normal"

@app.route("/")
def home():
    return "MindMesh Backend Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    result = detect_stress(data)
    return jsonify({"stress_level": result})

if __name__ == "__main__":
    app.run(debug=True)
