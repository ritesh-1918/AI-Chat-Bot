# Multi-Function AI Assistant

A web-based AI chatbot built with Python, Flask, and the Google Gemini API. This application serves as a powerful, interactive assistant capable of answering questions, summarizing text, and generating creative content.

![image](https://github.com/user-attachments/assets/ddf3014a-4e20-410e-a6a3-f933acb89b88)


## Table of Contents
- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)

## About The Project

This project is a comprehensive AI assistant designed to showcase skills in both backend development and prompt engineering. It features a clean, user-friendly interface that allows users to select from various AI-powered functions, demonstrating how different prompts can guide an AI model to produce specific and desired outputs[8, 10].

## Key Features

- **Multiple AI Functions**: Switch between different modes to perform various tasks:
  - **❓ Ask a Question**: For factual information and general conversation.
  - **📄 Summarize Text**: To get a concise summary of any provided text.
  - **✨ Generate Creative Content**: For creating stories, poems, or ideas based on a topic.
- **Interactive UI**: A modern and responsive web interface featuring:
  - User and AI avatars.
  - Timestamps for every message.
  - A "Copy to Clipboard" button for AI responses.
- **User Feedback System**: A simple "Helpful" / "Not Helpful" feedback mechanism to evaluate AI responses.

## Built With

This project was built using a combination of modern web technologies and AI services.

*   **Backend:**
    *   [Python](https://www.python.org/)
    *   [Flask](https://flask.palletsprojects.com/)
*   **Frontend:**
    *   HTML5
    *   CSS3
    *   JavaScript
*   **AI Engine:**
    *   [Google Gemini API](https://ai.google.dev/)
*   **Deployment:**
    *   [Vercel](https://vercel.com/)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You will need to have Python 3 installed on your system.

*   **Python 3.x**
    ```
    https://www.python.org/downloads/
    ```

### Installation

1.  **Clone the repository:**
    ```
    git clone https://github.com/ritesh-1918/AI-Chat-Bot.git
    ```
2.  **Navigate to the project directory:**
    ```
    cd AI-Chat-Bot
    ```
3.  **Create and activate a virtual environment:**
    ```
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Install the required Python packages:**
    ```
    pip install -r requirements.txt
    ```
5.  **Set up your environment variables:**
    -   Rename the `backend/.env.example` file to `backend/.env`.
    -   Open the `backend/.env` file and add your Google Gemini API key:
        ```
        GEMINI_API_KEY="YOUR_SECRET_API_KEY"
        ```

## Usage

1.  **Start the Flask server:**
    ```
    python backend/app.py
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5001`.
3.  Select a function from the dropdown menu.
4.  Type your message and click "Send".

## Deployment

This application is configured for easy deployment on [Vercel](https://vercel.com/). After pushing the code to your GitHub repository, you can import the project on the Vercel dashboard.

The `vercel.json` file in the root directory handles the build and routing configuration, telling Vercel how to serve the static frontend and run the Python backend as a serverless function[1, 2].

