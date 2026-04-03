# MindMesh – AI-Based Silent Mental Health Detection System
> ⚡ Passive, non-intrusive mental health detection without self-reporting

## 🚨 Problem
Students face increasing stress and mental health issues that often go undetected due to stigma and lack of early monitoring systems.

## 💡 Solution
MindMesh uses AI to passively monitor behavioral patterns such as screen time, sleep, and typing activity to detect early signs of stress and provide timely alerts and support.

## ⚙️ Tech Stack
- Flutter (Frontend)
- Firebase (Backend)
- Python (AI/ML)
- Google Fit API

## 🎯 Goal
To enable early detection of mental health issues and promote timely intervention in student communities.

## 🧠 How It Works
1. Collects behavioral data (screen time, sleep, typing)
2. AI model analyzes patterns
3. Detects deviations from normal behavior
4. Generates alerts and suggestions

## 🔒 Privacy
- No sensitive data stored
- Behavior patterns only analyzed
- User consent required

## 🚀 Future Scope
- AI chatbot integration
- Wearable device support
- College counseling integration

## 👥 Team
- Olivia Mukherjee – Development, AI Integration
- Priyanshu Srivastav – Project Lead & Coordination

## ▶️ How to Run

1. Clone the repository
2. Navigate to backend folder
3. Run the Flask server:
   python app.py

4. (Frontend placeholder – under development)

## 📊 Sample Input

{
  "screen_time": 9,
  "sleep_hours": 5,
  "typing_speed_drop": true
}

## 📈 Sample Output

High Stress

## 🤖 AI Logic

The system uses rule-based analysis combined with behavioral thresholds to detect stress levels:
- High screen time indicates potential burnout
- Reduced sleep suggests fatigue or anxiety
- Typing pattern changes indicate cognitive stress

These factors are combined to classify stress into Normal, Moderate, or High levels.

## 🔄 System Flow

User Data → Data Processing → AI Model → Stress Detection → Alert/Support

## ✅ Working Prototype

The system is designed as a functional prototype:

- Frontend collects user input (behavioral data)
- Backend processes data using Flask API
- AI logic analyzes patterns and returns stress level

Example Output:
Input:
{
  "screen_time": 9,
  "sleep_hours": 5,
  "typing_speed_drop": true
}

Output:
High Stress
