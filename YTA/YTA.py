import os
import reflex as rx
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Google Gemini API key is missing. Please set it in the .env file.")

genai.configure(api_key=GEMINI_API_KEY)

def extract_video_id(url: str) -> str:
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def get_transcript(video_url: str) -> str:
    video_id = extract_video_id(video_url)
    if not video_id:
        return "⚠️ Invalid YouTube URL"
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        return f"⚠️ Error fetching transcript: {str(e)}"

def summarize_text(text: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"Summarize this transcript:\n{text}")
        return response.text
    except Exception as e:
        return f"⚠️ Error generating summary: {str(e)}"

class VideoState(rx.State):
    video_url: str = ""
    transcript: str = ""
    summary: str = ""
    loading: bool = False

    def process_video(self):
        self.loading = True
        self.transcript = get_transcript(self.video_url)
        if not self.transcript.startswith("⚠️"):
            self.summary = summarize_text(self.transcript)
        self.loading = False

def index():
    return rx.center(
        rx.vstack(
            rx.heading("🎥 YouTube Video Summarizer", size="3", color="white"),
            rx.text("Summarize any YouTube video instantly with AI!", size="3", color="gray.300"),
            rx.spacer(),
            rx.input(
                placeholder="Enter YouTube Video URL",
                on_blur=VideoState.set_video_url,
                size="3",
                width="80%",
                border="2px solid #4A5568",
                border_radius="10px",
                padding="10px",
                color="white",
                background_color="#2D3748",
            ),
            rx.button(
                "✨ Summarize Video",
                on_click=VideoState.process_video,
                color_scheme="blue",
                size="3",
                border_radius="8px",
                font_weight="bold",
                padding="12px 24px",
                background_color="#3182CE",
                color="white",
                _hover={"background_color": "#2B6CB0"},
            ),
            rx.cond(
                VideoState.loading,
                rx.spinner(size="2", color="blue.500"),
                rx.vstack(
                    rx.divider(),
                    rx.text("📄 Transcript:", weight="bold", color="white"),
                    rx.text(VideoState.transcript, wrap=True, size="1", color="gray.300"),
                    rx.divider(),
                    rx.text("📌 Summary:", weight="bold", color="blue.300"),
                    rx.text(VideoState.summary, wrap=True, size="2", color="white"),
                ),
            ),
            rx.spacer(),
            rx.text("Made with ❤️ and ⚡ by Supratim", color="gray.400", size="1"),
        ),
        padding="50px",
        background_color="#1A202C",
    )

app = rx.App()
app.add_page(index)

if __name__ == "__main__":
    app.run()
