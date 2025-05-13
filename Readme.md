# 🎬 YouTube Timestamp Generator

Generate structured timestamps for YouTube videos using AI. This Flask web app extracts video transcripts and summarizes key sections into clickable timestamps, enhancing video navigation and viewer engagement.([Reddit][1], [Exemplary AI][2])

---

## 🚀 Features

* Extracts transcripts from YouTube videos using their URLs.
* Processes transcripts in chunks for efficient handling.
* Utilizes Google's Gemini AI model to generate concise timestamps.
* User-friendly web interface built with Flask.
* Deployable on platforms like Render.([Exemplary AI][2], [Hugging Face][3], [GitHub][4], [Reddit][1])

---

## 🖥️ Demo

Experience the live application here:
👉 [yt-timestamp-generator.onrender.com](https://yt-timestamp-generator.onrender.com)

---

## 📦 Installation

### Prerequisites

* Python 3.7 or higher
* A Google API key for Gemini AI (set as `GOOGLE_API_KEY` in `.env`)
### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/extremecoder-rgb/yt-timestamp-generator.git
   cd yt-timestamp-generator
   ```



2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```



4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add your Google API key:

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```



5. **Run the Application**

   ```bash
   python app.py
   ```



Access the application at `http://localhost:5000`.

---

## 🛠️ Usage

1. Navigate to the application's homepage.
2. Enter the URL of the YouTube video you wish to process.
3. Click the "Generate Timestamps" button.
4. View the generated timestamps, each indicating a distinct segment of the video.([Ilya Rodionov][5])

---

## 🌐 Deployment on Render

To deploy this application on [Render](https://render.com):

1. **Set the Start Command**

   In the Render dashboard, set the start command to:

   ```bash
   gunicorn app:app --bind 0.0.0.0:$PORT
   ```



2. **Ensure `gunicorn` is in `requirements.txt`**

   Add the following line to your `requirements.txt` if it's not already present:

   ```
   gunicorn
   ```



3. **Configure Environment Variables**

   In the Render dashboard, add your `GOOGLE_API_KEY` as an environment variable.

---

## 📂 Project Structure

```plaintext
yt-timestamp-generator/
├── app.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
└── venv/
```



---



