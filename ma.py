import streamlit as st
import speech_recognition as sr
import pyttsx3
from streamlit_option_menu import option_menu

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("Listening... Please speak into your microphone.")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            st.success("Audio captured successfully.")
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Could not request results, please check your internet connection."
        except Exception as e:
            return f"An error occurred: {e}"

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit app UI
st.set_page_config(page_title="Speech & Voice App", page_icon="🎤", layout="centered")
st.markdown(
    "<style>body {background-color: #f0f2f6;}</style>",
    unsafe_allow_html=True,
)
st.title("🎤 Speech Recognition & Voice Output App")

# Content based on navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "Profile", "History", "Speech", "Settings"],
    icons=["house", "person", "clock-history", "mic", "gear"],
    menu_icon="menu-button-wide",
    default_index=0,
    orientation="horizontal",
)

def render_tab_background(tab_name):
    st.markdown(
        f"<div style='display:flex;align-items:center;justify-content:center;height:70vh;background:linear-gradient(135deg, #1e90ff, #87cefa);border-radius:15px;color:white;'>\n"
        f"<h1 style='font-size:36px;'>{tab_name}</h1>\n"
        "</div>",
        unsafe_allow_html=True,
    )

if selected == "Home":
    render_tab_background("Welcome Home")
    st.write("### Welcome to the Speech & Voice App")
    st.write(
        "This app allows you to convert speech to text and text to speech with an easy-to-use interface. Use the tabs below to explore the features!"
    )
    st.image("https://source.unsplash.com/800x400/?voice", caption="Empowering Communication")

elif selected == "Profile":
    render_tab_background("User Profile")
    st.header("Profile")
    st.write("### User Profile")
    st.write("Feature under construction.")

elif selected == "History":
    render_tab_background("Activity History")
    st.header("History")
    st.write("### Your Activity History")
    st.write("Feature under construction.")

elif selected == "Speech":
    render_tab_background("Speech Features")
    sub_selected = option_menu(
        menu_title=None,
        options=["Speech Recognition", "Voice Output"],
        icons=["mic", "volume-up"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if sub_selected == "Speech Recognition":
        st.header("Speech Recognition")
        if st.button("Start Recording"):
            text = recognize_speech()
            st.text_area("Recognized Text", value=text, height=100)

    elif sub_selected == "Voice Output":
        st.header("Voice Output")
        user_input = st.text_area("Enter text to speak", placeholder="Type something...")
        if st.button("Speak Text"):
            if user_input.strip():
                st.info("Speaking...")
                speak_text(user_input)
            else:
                st.warning("Please enter some text to speak.")

elif selected == "Settings":
    render_tab_background("App Settings")
    st.header("Settings")
    st.write("### App Settings")
    st.write("Feature under construction.")

# Footer
# st.markdown("---")
# st.markdown(
#     "Developed with ❤️ using Streamlit. Explore more apps at [Streamlit.io](https://streamlit.io)."
# )
