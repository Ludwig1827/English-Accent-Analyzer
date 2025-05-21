@tool
def get_text_from_audio(audio_path: str) -> str:
  """
  Transcribes an audio file and returns the transcribed text.
  """
  model = whisper.load_model("turbo")
  result = model.transcribe(audio_path)
  return result["text"]
