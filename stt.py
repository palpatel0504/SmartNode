import whisper
model = whisper.load_model("base")


def transcribe_audio(file_path):
    """
    Convert audio to text
    """

    result = model.transcribe(file_path)

    return result["text"]