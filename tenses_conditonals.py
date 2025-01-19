import streamlit as st
import random

##############################################################################
# 1) PAGE CONFIG -- No 'theme' param to avoid older Streamlit TypeError
##############################################################################
st.set_page_config(
    page_title="Grammar Genius App",
    layout="wide"
)

##############################################################################
# 2) SESSION STATE
##############################################################################
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Tenses"
if "selected_item_key" not in st.session_state:
    st.session_state.selected_item_key = None
if "answers" not in st.session_state:
    st.session_state.answers = []
if "submitted_questions" not in st.session_state:
    st.session_state.submitted_questions = set()
if "review_mode" not in st.session_state:
    st.session_state.review_mode = False
if "randomized_messages" not in st.session_state:
    motivational_sentences = [
        "You're on fire! 🔥",
        "Keep smashing it! 💥",
        "Fantastic answer! Your words are shining brighter now! 🌟",
        "You're a grammar wizard! Conjugations bend to your will! 🧙‍♂️",
        "Way to go, champ! That sentence just leapt off the page! 🏆",
        "Bravo! That's the spirit! Your linguistic muscles are flexing! 👏",
        "Grammar genius at work! Your sentences sparkle like diamonds! 🧠",
        "Outstanding! The grammar gods are smiling upon you now! 🥳",
        "You're unstoppable! The universe is taking notes from your syntax! 🚀",
        "Wonderful! Each answer you give writes poetry in the sky! 🎩✨",
        "You're dazzling! These sentences are lining up to be in your presence! ✨🌈",
        "Impressive! Your answers radiate confidence and linguistic flair! 💎💃",
        "Marvelous! The grammar galaxy bows before your might! 🌌🏅",
        "Astonishing! Every verb you conjure becomes a masterpiece! 🎉📚",
        "Magnificent! Even dictionaries blush at your command of words! 🦄📖",
        "Incredible! Grammarians form fan clubs in your honor! 🎶💫",
        "Stupendous! Your verb forms could charm the toughest critics! 🍀💬",
        "Glorious! Your tense usage now inspires entire textbooks! 🦋🔥",
        "Remarkable! Each reply is like a linguistic symphony in action! 🎼🌍",
        "Spectacular! Your English prowess bursts forth like cosmic fireworks! 💥🚀🎉"
    ]
    random.shuffle(motivational_sentences)
    st.session_state.randomized_messages = motivational_sentences

##############################################################################
# 3) TENSES AND CONDITIONALS DATA
#    Insert your 7 tenses & 5 conditionals data below, with new optional fields:
#    - "illustration_url": str (for each tense/conditional)
#    - usage_cases may contain:
#         "question_type": "multiple_choice" or "open_ended" (default open_ended)
#         "choices": list of possible answers (for multiple_choice)
#         "correct_choice": the correct string or "correct_index": an integer
#         "context": str for real-life scenario
##############################################################################
def sample_tenses_data():
    return {
        "1": {
            "name": "Present Simple",
            "illustration_url": "https://example.com/present_simple.png",  # Themed illustration
            "formation": {
                "Positive": "Subject + base form (e.g., 'I eat')",
                "Negative": "Subject + do not/does not + base form (e.g., 'I do not eat')",
                "Question": "Do/Does + subject + base form? (e.g., 'Do you eat?')",
                "Short answer": "'Yes, I do.' / 'No, I don't.'"
            },
            "usage_explanation": [
                "General or always true facts.",
                "Situations that are more or less permanent.",
                "Habits or things done regularly."
            ],
            "usage_cases": [
                {
                    "title": "Expressing facts",
                    "context": "Imagine you're explaining a science fact in class.",
                    "question_type": "multiple_choice",
                    "question": "Which sentence is correct for a general truth?",
                    "choices": [
                        "Water boils if you heated it up.",
                        "Water boils if you heat it up.",
                        "Water is boiling if you heat it up."
                    ],
                    "correct_choice": "Water boils if you heat it up."
                },
                {
                    "title": "Describing habits",
                    "context": "Consider your daily routine. Talk about what you do in the morning.",
                    "question_type": "open_ended",
                    "question": "What do you usually do after waking up?"
                },
                # ... up to 10 usage cases ...
            ],
            "extra_examples": [
                "I always wake up at 7 AM.",
                "My brother doesn't eat fish.",
                "The Earth revolves around the Sun."
            ]
        },
        "2": {
            "name": "Past Simple",
            "illustration_url": "https://example.com/past_simple.png",
            "formation": {
                "Positive": "Subject + past form (e.g., 'I ate')",
                "Negative": "Subject + did not + base form (e.g., 'I did not eat')",
                "Question": "Did + subject + base form? (e.g., 'Did you eat?')",
                "Short answer": "'Yes, I did.' / 'No, I didn't.'"
            },
            "usage_explanation": [
                "Completed actions in the past.",
                "Actions that happened at a specific time.",
            ],
            "usage_cases": [
                {
                    "title": "Completed action at a specific time",
                    "context": "Think about your last holiday. How do you describe it?",
                    "question_type": "multiple_choice",
                    "question": "Which is correct for describing a completed event?",
                    "choices": [
                        "I travel to Spain last year.",
                        "I traveled to Spain last year.",
                        "I will travel to Spain last year."
                    ],
                    "correct_choice": "I traveled to Spain last year."
                },
                {
                    "title": "A specific past event",
                    "question_type": "open_ended",
                    "context": "Remember your last birthday celebration.",
                    "question": "What did you do on your last birthday?"
                },
                # ... more usage cases ...
            ],
            "extra_examples": [
                "I visited my grandparents last weekend.",
                "They watched a movie yesterday."
            ]
        },
        # ... 5 more tenses ...
    }

def sample_conditionals_data():
    return {
        "0": {
            "name": "Zero Conditional",
            "illustration_url": "https://example.com/zero_conditional.png",
            "formation": {
                "Positive": "If + present simple, present simple",
                "Negative": "If + present simple, present simple (negative)",
                "Question": "Do/Does + subject + base form in each clause",
                "Short answer": "N/A"
            },
            "usage_explanation": [
                "Facts always true under certain conditions.",
                "General truths or cause-and-effect relationships."
            ],
            "usage_cases": [
                {
                    "title": "General truths",
                    "context": "Explain a routine consequence with If... then structure.",
                    "question_type": "open_ended",
                    "question": "If you don't water plants, what usually happens?"
                },
                {
                    "title": "Scientific facts",
                    "context": "Think about simple cause-effect in science.",
                    "question_type": "multiple_choice",
                    "question": "If you heat ice, what happens?",
                    "choices": [
                        "It melts",
                        "It froze",
                        "It is melting"
                    ],
                    "correct_choice": "It melts"
                }
            ],
            "extra_examples": [
                "If you freeze water, it becomes ice.",
                "If you touch a hot stove, you get burned."
            ]
        },
        # ... 4 more conditionals ...
    }

# For demonstration, let's use the sample data above:
tenses_data = sample_tenses_data()
conditionals_data = sample_conditionals_data()

##############################################################################
# 4) HELPER: THEME & FONT SIZE
##############################################################################
def generate_css(theme: str, font_size: str) -> str:
    """Generate dynamic CSS for Dark/Light theme and bigger font sizes."""
    # Increase sizes so they're obviously different:
    font_map = {
        "Small": "16px",
        "Medium": "20px",
        "Large": "24px"
    }
    selected_font_size = font_map.get(font_size, "20px")  # default to Medium

    if theme == "Light":
        main_bg = "#ffffff"
        main_color = "#000000"
        sidebar_bg = "#f0f0f0"
        sidebar_color = "#000000"
    else:
        main_bg = "#000000"
        main_color = "#ffffff"
        sidebar_bg = "#013369"
        sidebar_color = "#ffffff"

    css = f"""
    <style>
    :root, html, body, [data-testid="stAppViewContainer"], 
    [data-testid="stAppViewBody"], [data-testid="stMarkdownContainer"],
    .stMarkdown, [class^="css-"], [data-testid="stHeader"], [data-testid="stSidebar"], 
    .css-1oe6wy4, .block-container {{
        background-color: {main_bg} !important;
        color: {main_color} !important;
        font-size: {selected_font_size} !important;
    }}

    /* Headings remain orange, scaled up by 1.25 */
    h1, h2, h3 {{
        color: #ff5722 !important;
        font-family: "Trebuchet MS", sans-serif;
        font-size: calc({selected_font_size} * 1.25) !important;
    }}

    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg} !important;
        color: {sidebar_color} !important;
    }}
    [data-testid="stSidebar"] * {{
        font-size: {selected_font_size} !important;
        color: {sidebar_color} !important;
    }}

    main > div {{
        padding-top: 20px;
    }}
    </style>
    """
    return css

##############################################################################
# 5) CORE HELPER FUNCTIONS
##############################################################################
def reset_questions():
    st.session_state.answers = []
    st.session_state.submitted_questions = set()
    st.session_state.review_mode = False
    random.shuffle(st.session_state.randomized_messages)

def get_current_data():
    """Return the dictionary and item key for whichever Tense/Conditional is chosen."""
    if st.session_state.selected_category == "Tenses":
        if st.session_state.selected_item_key:
            return tenses_data, st.session_state.selected_item_key
        else:
            return None, None
    else:
        if st.session_state.selected_item_key:
            return conditionals_data, st.session_state.selected_item_key
        else:
            return None, None

##############################################################################
# 6) SIDEBAR: Category, Theme, Font Size
##############################################################################
st.sidebar.title("Grammar Categories")

# Category radio
category = st.sidebar.radio("Select a category:", ["Tenses", "Conditionals"])
st.session_state.selected_category = category

# Build the selection
if st.session_state.selected_category == "Tenses":
    st.sidebar.subheader("Select a Tense")
    tense_options = ["Select a tense..."] + [f"{key}. {tenses_data[key]['name']}" for key in tenses_data]
    selected_option = st.sidebar.selectbox("Choose a tense to practice:", tense_options)
    if selected_option != "Select a tense...":
        current_key = selected_option.split('.')[0].strip()
        if current_key != st.session_state.selected_item_key:
            st.session_state.selected_item_key = current_key
            reset_questions()
    else:
        st.session_state.selected_item_key = None
        reset_questions()
else:
    st.sidebar.subheader("Select a Conditional")
    conditional_options = ["Select a conditional..."] + [f"{key}. {conditionals_data[key]['name']}" for key in conditionals_data]
    selected_option = st.sidebar.selectbox("Choose a conditional to practice:", conditional_options)
    if selected_option != "Select a conditional...":
        current_key = selected_option.split('.')[0].strip()
        if current_key != st.session_state.selected_item_key:
            st.session_state.selected_item_key = current_key
            reset_questions()
    else:
        st.session_state.selected_item_key = None
        reset_questions()

# Theme choice
theme_choice = st.sidebar.radio("Choose a Theme:", ["Dark", "Light"], index=0)
# Font Size choice
font_size_choice = st.sidebar.radio("Font Size:", ["Small", "Medium", "Large"], index=1)

# Apply dynamic CSS
css_string = generate_css(theme_choice, font_size_choice)
st.markdown(css_string, unsafe_allow_html=True)

##############################################################################
# 7) SCREENS
##############################################################################
def show_welcome():
    """Welcome screen."""
    st.title("Welcome to the Grammar Genius Game! 🎉✨🎮")
    st.write("""
    Get ready to boost your English grammar skills in a fun and interactive way!

    1. Use the sidebar to choose either Tenses or Conditionals.
    2. Select which Tense/Conditional you want to practice.
    3. Read how it's formed, when to use it, and see extra examples.
    4. Answer the questions, receiving motivational feedback each time.
    5. Once you finish all questions, you'll earn a special badge!

    Let's begin!
    """)

def show_review(data_dict, item_key):
    """Review screen: show answered questions, each with a trophy 🏆."""
    st.header("Review Your Answers")
    usage_cases = data_dict[item_key]["usage_cases"]
    for i, case in enumerate(usage_cases):
        answer_key = f"answer_{item_key}_{i}"
        st.write(f"**{case['title']}**")
        st.write(f"Question: {case['question']}")
        user_answer = st.session_state.get(answer_key, "")
        st.write(f"Your answer: {user_answer} 🏆")
    st.write("Feel free to pick another item from the sidebar if you want.")

def show_explanation_and_questions():
    data_dict, item_key = get_current_data()
    if not data_dict or not item_key:
        return

    info = data_dict[item_key]

    # Themed illustration at the top, if provided
    if "illustration_url" in info and info["illustration_url"]:
        st.image(info["illustration_url"], width=200)

    st.header(info["name"])
    st.subheader("How is it formed?")
    for form_type, form_rule in info["formation"].items():
        st.markdown(f"**{form_type}:** {form_rule}")

    st.subheader("When do we use it?")
    for usage in info["usage_explanation"]:
        st.write("- " + usage)

    # More Examples
    if "extra_examples" in info and info["extra_examples"]:
        with st.expander("More Examples"):
            for ex in info["extra_examples"]:
                st.write("- " + ex)

    usage_cases = info["usage_cases"]
    total_questions = len(usage_cases)
    answered_count = len(st.session_state.answers)

    if st.session_state.review_mode:
        show_review(data_dict, item_key)
        return

    st.write("### Practice Questions")
    colA, colB = st.columns(2)
    colA.metric("Questions Answered", f"{answered_count}")
    colB.metric("Total Questions", f"{total_questions}")

    progress_val = int((answered_count / total_questions) * 100)
    st.progress(progress_val)

    # If user completed all usage cases
    if answered_count == total_questions:
        st.success(f"You've answered all {total_questions} questions for {info['name']}!")
        st.markdown(f"**Badge Unlocked:** *{info['name']} Expert!* 🏆")

        if st.button("Review Your Answers"):
            st.session_state.review_mode = True
        return

    # Display usage cases
    for i, case in enumerate(usage_cases):
        question_type = case.get("question_type", "open_ended")  # default
        answer_key = f"answer_{item_key}_{i}"
        submit_key = f"submit_{item_key}_{i}"

        if submit_key in st.session_state.submitted_questions:
            # Already answered
            st.write(f"**{case['title']}**")
            if "context" in case:
                st.write(f"Context: {case['context']}")
            st.write(case["question"])
            user_answer = st.session_state.get(answer_key, "")
            st.write(f"Your answer: {user_answer}")
            continue

        # Show context if provided
        st.write(f"**{case['title']}**")
        if "context" in case:
            st.write(f"Context: {case['context']}")
        st.write(case["question"])

        if question_type == "multiple_choice":
            # Provide a selectbox or radio with possible choices
            choices = case.get("choices", [])
            correct_choice = case.get("correct_choice", None)  
            # For correctness, we store user selection in session_state
            st.session_state.setdefault(answer_key, "")  # ensure it's in state

            # Show the multiple choice
            user_answer = st.selectbox(
                "Select your answer:",
                ["-- Select --"] + choices,
                key=answer_key
            )
        else:
            # open-ended
            st.text_input("Your answer:", key=answer_key)

        if st.button("Submit", key=submit_key):
            user_answer = st.session_state.get(answer_key, "")
            st.session_state.answers.append(user_answer)
            st.session_state.submitted_questions.add(submit_key)

            msg_index = len(st.session_state.answers) - 1
            if msg_index < len(st.session_state.randomized_messages):
                msg = st.session_state.randomized_messages[msg_index]
            else:
                msg = st.session_state.randomized_messages[-1]

            # Check correctness if multiple_choice
            if question_type == "multiple_choice":
                correct_choice = case.get("correct_choice", None)
                if correct_choice and user_answer == correct_choice:
                    st.success("Correct! " + msg)
                elif user_answer == "-- Select --":
                    st.warning("You haven't selected an option yet.")
                    # Remove from answered to allow retry
                    st.session_state.answers.pop()
                    st.session_state.submitted_questions.remove(submit_key)
                    st.stop()  # re-render
                else:
                    st.warning("Incorrect. Try again?")
                    # Remove from answered to allow retry
                    st.session_state.answers.pop()
                    st.session_state.submitted_questions.remove(submit_key)
                    st.stop()
            else:
                # open-ended, always accept & show motivational message
                if msg[0].isupper():
                    new_msg = f"{msg[0].lower() + msg[1:]}"
                else:
                    new_msg = msg
                st.success(new_msg)

            st.write(f"Your answer: {user_answer}")

##############################################################################
# 8) MAIN
##############################################################################
def main():
    if st.session_state.selected_item_key is None:
        show_welcome()
    else:
        show_explanation_and_questions()

if __name__ == "__main__":
    main()

