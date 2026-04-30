import random

questions = {
    "Python": [
        "What is Python and why is it used?",
        "Explain difference between list and tuple.",
        "What are decorators in Python?",
        "What is OOP concept?"
    ],
    "AI/ML": [
        "What is machine learning?",
        "Difference between supervised and unsupervised learning?",
        "What is overfitting?",
        "Explain Random Forest."
    ],
    "HR": [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths?",
        "Where do you see yourself in 5 years?"
    ]
}

def get_question(domain):
    return random.choice(questions[domain])