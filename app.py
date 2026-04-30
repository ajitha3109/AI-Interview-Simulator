import streamlit as st

st.set_page_config(page_title="AI Interview Coach", page_icon="🎤", layout="centered")

st.title("🎤 AI Interview Coach")
st.caption("Multi-question AI Interview Practice System")

# -----------------------
# QUESTIONS DATABASE
# -----------------------
questions = {
    "Python": [
        "What is a decorator in Python?",
        "What is the difference between list and tuple?",
        "What is OOP in Python?"
    ],
    "AI/ML": [
        "What is machine learning?",
        "What is supervised learning?",
        "What is overfitting?"
    ],
    "HR": [
        "Tell me about yourself.",
        "What are your strengths?",
        "Where do you see yourself in 5 years?"
    ]
}

# -----------------------
# SESSION STATE
# -----------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

# -----------------------
# DOMAIN SELECT
# -----------------------
domain = st.selectbox("Select Interview Type", ["Python", "AI/ML", "HR"])

# -----------------------
# START BUTTON
# -----------------------
if st.button("🚀 Start Interview"):
    st.session_state.started = True
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []

# -----------------------
# SMART EVALUATION FUNCTION
# -----------------------
def evaluate_answer(answer, question):
    answer = answer.lower()
    score = 0

    # Python Questions
    if "decorator" in question.lower():
        if "function" in answer: score += 3
        if "modify" in answer or "extend" in answer: score += 3
        if "without changing" in answer: score += 2

    elif "list" in question.lower() or "tuple" in question.lower():
        if "mutable" in answer: score += 3
        if "immutable" in answer: score += 3
        if "square" in answer or "parentheses" in answer: score += 2

    elif "oop" in question.lower():
        if "object" in answer: score += 3
        if "class" in answer: score += 3
        if "inheritance" in answer: score += 2

    # AI/ML Questions
    elif "machine learning" in question.lower():
        if "data" in answer: score += 3
        if "model" in answer: score += 3
        if "algorithm" in answer: score += 2

    elif "overfitting" in question.lower():
        if "training" in answer: score += 3
        if "model" in answer: score += 3

    # HR Questions
    elif "tell me about yourself" in question.lower():
        if "project" in answer: score += 3
        if "skills" in answer or "experience" in answer: score += 3
        if "learning" in answer or "growth" in answer: score += 2

    else:
        if len(answer.split()) > 10:
            score += 4

    # length bonus
    score += min(len(answer.split()) / 20, 2)

    return round(min(score, 10), 2)

# -----------------------
# MAIN INTERVIEW FLOW
# -----------------------
if st.session_state.started:

    q_list = questions[domain]

    if st.session_state.index < len(q_list):

        question = q_list[st.session_state.index]

        st.subheader(f"Question {st.session_state.index + 1}")
        st.success(question)

        answer = st.text_area("✍️ Your Answer")

        if st.button("📩 Submit Answer"):

            if len(answer.strip()) < 5:
                st.warning("⚠️ Please write a proper answer")
            else:

                score = evaluate_answer(answer, question)

                st.session_state.score += score
                st.session_state.answers.append(answer)

                st.subheader("📊 Result")

                st.metric("Score for this answer", f"{score}/10")

                if score >= 7:
                    st.success("🔥 Excellent Answer")
                elif score >= 4:
                    st.warning("👍 Good Answer")
                else:
                    st.error("📉 Needs Improvement")

                st.session_state.index += 1

                st.rerun()

    else:

        st.subheader("🎯 Interview Completed!")

        final_score = st.session_state.score / len(q_list)

        st.metric("Final Score", f"{final_score:.2f} / 10")

        if final_score >= 7:
            st.success("🔥 Excellent Performance")
        elif final_score >= 4:
            st.warning("👍 Good Performance")
        else:
            st.error("📉 Needs Improvement")

        st.subheader("📝 Your Answers")

        for i, ans in enumerate(st.session_state.answers):
            st.write(f"Q{i+1}: {ans}")

        if st.button("🔄 Restart Interview"):
            st.session_state.started = False
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.answers = []