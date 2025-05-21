import os
import tempfile
import subprocess
import requests
from moviepy.editor import VideoFileClip
from langchain_core.tools import tool
import whisper
from lingua import Language, LanguageDetectorBuilder
import torchaudio
from speechbrain.pretrained import EncoderClassifier
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.language_models import BaseLanguageModel
from langchain_ollama import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import ChatPromptTemplate
import re
from langchain_ollama import ChatOllama
from langchain.chat_models import init_chat_model
import getpass
from google.colab import userdata
from langchain_openai import ChatOpenAI

# get from the tools
from tools.extract_audio import extract_audio_from_video_url
from tools.get_text_from_audio import get_text_from_audio
from tools.detect_language import detect_language_with_confidence
from tools.classify_accent import classify_accent
from tools.summarize import summarize_text

os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

tools = [extract_audio_from_video_url, get_text_from_audio, detect_language_with_confidence, classify_accent, summarize_text]

agent = create_react_agent(model, tools=tools, prompt=prompt)





