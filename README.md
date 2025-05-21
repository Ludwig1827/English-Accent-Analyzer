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

```bash
git clone https://github.com/your-username/english-accent-analyzer.git
cd english-accent-analyzer


### 2. Install dependencies












