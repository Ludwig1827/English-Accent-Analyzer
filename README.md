# 🧠 English Accent & Audio Analyzer Agent

This project is an AI agent that analyzes spoken English from public video URLs. It detects the language, classifies the accent (e.g., US, UK), summarizes the content, and enables RAG-based question answering.

Built using:
- 🧠 [LangChain](https://www.langchain.com/)
- 🎧 [OpenAI Whisper](https://github.com/openai/whisper)
- 🗣️ [SpeechBrain Accent Classifier](https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa)
- 🤖 Ollama or OpenAI LLMs
- 🛠️ LangGraph (optional multi-step orchestration)

---

## 🚀 Features

- ✅ Extract audio from public `.mp4` or streaming platforms (YouTube, Loom)
- 📝 Transcribe speech using Whisper
- 🌍 Detect if the speaker is using English and compute confidence
- 🇬🇧 Classify accent (e.g., US, UK, Australian)
- 📄 Summarize the content in bullet form
- ❓ Allow follow-up questions via a RAG pipeline

---

## 🛠️ Setup

### 1. Clone this repository
```
bash
git clone https://github.com/your-username/english-accent-analyzer.git
cd english-accent-analyzer
```

### 2. Install Python dependencies
```
pip install -r requirements.txt
```

### 3. Install system dependencies
```
sudo apt update
sudo apt install ffmpeg
```
You may also need yt-dlp for extracting audio from streaming platforms:
```
pip install yt-dlp
```


## 🚀 Run the App
```
from agent.video_analysis_agent import agent
from langchain_core.messages import HumanMessage

video_url = "https://your-video-url.com"
response = agent.invoke({"messages": [HumanMessage(content=f"Analyze this video: {video_url}")]})
print(response["messages"][-1].content)  # final output

```

## 📦 Example Output
## 🎧 Audio Analysis Results

### 🗣️ Detected Language
- **Language**: English
- **Confidence**: 100.0%

### 🎯 Accent Classification
- **Accent**: American (US)
- **Confidence**: 69.7%

### 📝 Summary of Transcription
- The speaker is an AI Engineer and graduate student at Rice University.
- They build intelligent multi-agent systems for legal and financial workflows.
- Their system leverages LangChain and vector databases for decision-making.
- They are seeking collaborators to scale this technology.






