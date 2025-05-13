from flask import Flask, render_template, request
from dotenv import find_dotenv, load_dotenv
import os
import re
import time
from youtube_transcript_api import YouTubeTranscriptApi
from google.generativeai import GenerativeModel


load_dotenv(find_dotenv())

gemini_model = GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["videoUrl"]
        video_id = extract_video_id(video_url)
        try:
            transcript_chunks = fetch_transcript(video_id)  
            timestamps = generate_timestamps(transcript_chunks)  
            return render_template("index.html", timestamps=timestamps)
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html", timestamps=None)

def extract_video_id(url):
    regex = r"(youtu\.be\/|youtube\.com\/(?:watch\?v=|v\/|embed\/|watch\?.+&v=))((\w|-){11})"
    matches = re.search(regex, url)
    if matches:
        return matches.group(2)
    raise ValueError("Invalid YouTube URL")

def fetch_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id)
    return chunk_transcript(transcript)

def chunk_transcript(transcript, chunk_size=1500):
    chunks = []
    current_chunk = []
    current_length = 0

    for entry in transcript:
        text = entry.get("text", "")
        if text.startswith("["):
            continue
        minutes = int(entry["start"] // 60)
        seconds = int(entry["start"] % 60)
        formatted_time = f"{minutes:02}:{seconds:02}"
        formatted_entry = f"{formatted_time} || {text}"

        current_length += len(formatted_entry)
        if current_length > chunk_size:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_length = len(formatted_entry)

        current_chunk.append(formatted_entry)

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks

def generate_timestamps(transcript_chunks):
    timestamps = []
    
    for chunk in transcript_chunks:
        prompt = f"""
            You are an AI skilled in analyzing YouTube video content. Create up to 7 accurate timestamps from the transcript below.
            Each timestamp should represent a distinct topic or main idea in the video.
            Format:
            00:00 || Title for the first segment
            02:56 || Title for the second segment

            Transcript:
            {chunk}
        """
        try:
            response = gemini_model.generate_content(prompt)
            if response and response.text:
                timestamps.append(response.text)
            
            time.sleep(1.5) 
        except Exception as e:
            print(f"Error: {e}")
            break  

    return "\n".join(timestamps) if timestamps else "Error generating timestamps."

if __name__ == "__main__":
    app.run(debug=True, port=5000)
