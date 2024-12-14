import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from streamlit_option_menu import option_menu

# Function to recognize speech from the microphone
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    try:
        with mic as source:
            st.info("Listening... Please speak into your microphone.")
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

# Function to recognize speech from uploaded audio file
def recognize_speech_from_file(uploaded_file):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(uploaded_file) as source:
            st.info("Processing audio...")
            audio = recognizer.record(source)
            st.success("Audio processed successfully.")
            return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Could not request results, please check your internet connection."
    except Exception as e:
        return f"An error occurred: {e}"

# Function for text-to-speech using gTTS
def speak_text_with_gtts(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    st.audio("output.mp3", format="audio/mp3")

# Streamlit app UI
st.set_page_config(page_title="Speech & Voice App", page_icon="🎤", layout="centered")
st.markdown(
    "<style>body {background-color: #f0f2f6;}</style>",
    unsafe_allow_html=True,
)
st.title("🎤 Speech Recognition & Voice Output App")

# Navigation menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Speech", "Settings"],
    icons=["house", "mic", "gear"],
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

# Home Page
if selected == "Home":
    render_tab_background("Welcome Home")
    st.write("### Welcome to the Speech & Voice App")
    st.write(
        "This app allows you to convert speech to text and text to speech with an easy-to-use interface. Use the tabs below to explore the features!"
    )
    st.image("https://source.unsplash.com/800x400/?voice", caption="Empowering Communication")

# Speech Features
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

    # Speech Recognition
    if sub_selected == "Speech Recognition":
        st.header("Speech Recognition")
        # Option 1: Voice input via microphone
        if st.button("Start Recording"):
            text = recognize_speech_from_mic()
            st.text_area("Recognized Text (from microphone)", value=text, height=100)

        # Option 2: File upload
        uploaded_file = st.file_uploader("Or upload an audio file", type=["wav", "mp3"])
        if uploaded_file and st.button("Process Audio"):
            text = recognize_speech_from_file(uploaded_file)
            st.text_area("Recognized Text (from file)", value=text, height=100)

    # Voice Output
    elif sub_selected == "Voice Output":
        st.header("Voice Output")
        user_input = st.text_area("Enter text to speak", placeholder="Type something...")
        if st.button("Speak Text"):
            if user_input.strip():
                st.info("Converting text to speech...")
                speak_text_with_gtts(user_input)
            else:
                st.warning("Please enter some text to speak.")

# Settings Page
elif selected == "Settings":
    render_tab_background("App Settings")
    st.header("Settings")
    st.write("### App Settings")
    st.write("Feature under construction.")
