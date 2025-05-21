@tool
def extract_audio_from_video_url(url: str) -> str:
    """
    Extract audio from a public video URL (direct .mp4 or streaming platform like Loom/YouTube).
    Returns the local path to the extracted audio file (.wav or .mp3).
    """
    def is_direct_mp4(url: str) -> bool:
      return url.strip().lower().endswith(".mp4")
    try:
        if is_direct_mp4(url):
            # Download the MP4 video
            response = requests.get(url, stream=True)
            response.raise_for_status()

            tmp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            with open(tmp_video.name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Extract audio using moviepy
            clip = VideoFileClip(tmp_video.name)
            audio_path = tmp_video.name.replace(".mp4", ".wav")
            clip.audio.write_audiofile(audio_path)
            return audio_path

        else:
            # Use yt-dlp to download and extract audio from streaming URL
            tmp_dir = tempfile.mkdtemp()
            command = [
                "yt-dlp",
                "-x", "--audio-format", "mp3",
                "-o", os.path.join(tmp_dir, "%(title)s.%(ext)s"),
                url
            ]
            subprocess.run(command, check=True)

            # Find the downloaded .mp3 file
            files = os.listdir(tmp_dir)
            audio_files = [f for f in files if f.endswith(".mp3")]
            if not audio_files:
                raise FileNotFoundError("No MP3 file found in the output directory.")

            return os.path.join(tmp_dir, audio_files[0])

    except Exception as e:
        return f"❌ Error extracting audio: {str(e)}"
