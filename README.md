# 🎤 Speech Recognition & Voice Output App

A modern, interactive web application built with Streamlit that provides speech-to-text and text-to-speech capabilities.

![Speech App Demo](https://source.unsplash.com/800x400/?voice)

## ✨ Features

- **🎤 Speech Recognition**: Convert speech to text using your microphone
- **📁 Audio File Processing**: Upload and process audio files (WAV, MP3)
- **🔊 Text-to-Speech**: Convert text to speech with natural-sounding voice
- **🎨 Beautiful UI**: Clean, modern interface with intuitive navigation
- **📱 Responsive Design**: Works on desktop and mobile devices

## 🚀 Live Demo

You can run this app on various platforms:

### Streamlit Community Cloud (Recommended)
1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy from your forked repository
5. Set the main file path to `ma.py`

### Heroku Deployment
1. Fork this repository
2. Create a new Heroku app
3. Connect to your GitHub repository
4. Add a `Procfile` with: `web: streamlit run ma.py --server.port=$PORT --server.address=0.0.0.0`
5. Deploy from GitHub

### Railway Deployment
1. Fork this repository
2. Go to [railway.app](https://railway.app)
3. Create a new project from your GitHub repo
4. Railway will automatically detect it's a Python app and deploy

## 🛠️ Local Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Microphone access (for speech recognition)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SunithNayak99/host-test.git
   cd host-test
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run ma.py
   ```

4. **Open your browser**
   - The app will automatically open in your default browser
   - Or manually go to `http://localhost:8501`

## 📋 Dependencies

- **streamlit**: Web app framework
- **speechrecognition**: Speech-to-text functionality
- **gtts**: Google Text-to-Speech
- **streamlit-option-menu**: Enhanced navigation menu

## 🎯 Usage

### Speech Recognition
1. Navigate to the "Speech" tab
2. Select "Speech Recognition"
3. Click "Start Recording" and speak into your microphone
4. Or upload an audio file (WAV/MP3 format)

### Text-to-Speech
1. Navigate to the "Speech" tab
2. Select "Voice Output"
3. Enter text in the text area
4. Click "Speak Text" to generate audio

## 🔧 Configuration

The app uses default settings, but you can modify:
- **Language**: Currently set to English ('en')
- **Audio format**: Supports WAV and MP3 files
- **Recording timeout**: Set to 5 seconds

## 📁 Project Structure

```
host-test/
├── ma.py              # Main Streamlit application
├── requirements.txt   # Python dependencies
├── runtime.txt       # Python version specification
├── README.md         # This file
└── .gitignore       # Git ignore rules
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## 🆘 Troubleshooting

### Common Issues

**Microphone not working:**
- Ensure your browser has microphone permissions
- Check your system's microphone settings

**Audio file upload fails:**
- Supported formats: WAV, MP3
- Check file size (keep under 200MB)

**Internet connection required:**
- Speech recognition uses Google's API
- Text-to-speech requires internet connection

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Speech recognition powered by [Google Speech Recognition API](https://cloud.google.com/speech-to-text)
- Text-to-speech using [Google Text-to-Speech](https://cloud.google.com/text-to-speech)

---

⭐ **Star this repository if you found it helpful!**