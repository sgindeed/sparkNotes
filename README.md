## 🔥 SparkNotes – YouTube Video Summarizer with Gemini AI

📽️ **SparkNotes** is an AI-powered web app that summarizes any **YouTube video** in seconds using **Google Gemini AI** and the **YouTube Transcript API**.  
🎨 Built with **Reflex**, it offers a fast, elegant, and seamless user experience.  
🔗 Just paste a video link and get the full transcript ✍️ + an intelligent summary 📌 — all in one click!

---

### 🚀 Features

- 🔗 Paste any YouTube video URL to fetch its transcript  
- 🤖 Generate a smart AI-powered summary with Gemini 2.0 Flash  
- ⚠️ Robust error handling for invalid URLs or missing data  
- 🌑 Sleek dark UI powered by Reflex  
- ⚡ Real-time updates with a clean and fast interface

---

### 📁 Project Structure

```bash
sparkNotes/
│
├── assets/                  # Static files (e.g., preview.gif)
│   └── preview.gif
│
├── YTA/                     # Main app folder
│   └── YTA.py               # Core logic (YouTube + Gemini)
│
├── requirements.txt         # Python package dependencies
├── rxconfig.py              # Reflex configuration
└── README.md                # This file!
```

---

### 🛠️ Installation from GitHub

Follow these steps to set up SparkNotes locally:

#### 📥 Step 1: Clone the Repository
```bash
git clone https://github.com/sgindeed/sparkNotes.git
cd sparkNotes
```

#### 🧪 Step 2: Create a `.env` File
```bash
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
```

#### 📦 Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

#### 🚀 Step 4: Run the App Locally
```bash
reflex run
```

---

### 🧠 Tech Stack

| Category         | Technology                                |
|------------------|--------------------------------------------|
| UI Framework     | [Reflex](https://reflex.dev/)             |
| AI Model         | Google Gemini 2.0 Flash                   |
| Transcripts      | `youtube-transcript-api`                  |
| Language         | Python                                    |

---

### 🌍 Live Demo

> 🔜 Coming soon! 

---

### 📌 Project Link

📂 GitHub: [https://github.com/sgindeed/sparkNotes](https://github.com/sgindeed/sparkNotes)

---

### 👨‍💻 Author

**Supratim Ghosh**  
🔗 [LinkedIn](https://linkedin.com/in/supratim-ghosh-b07091241)  
💻 [GitHub](https://github.com/sgindeed)

---
