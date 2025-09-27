#!/bin/bash

# Speech Recognition & Voice Output App Startup Script

echo "🎤 Starting Speech Recognition & Voice Output App..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies. Please check your internet connection and try again."
    exit 1
fi

echo "✅ Dependencies installed successfully!"

# Start the Streamlit app
echo "🚀 Starting the application..."
streamlit run ma.py

echo "🎉 Application started! Open your browser to the URL shown above."