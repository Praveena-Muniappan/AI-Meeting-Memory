
import os
import whisper


class MeetingTranscriber:
    """
    Handles speech-to-text transcription
    using OpenAI Whisper.
    """

    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        """
        Transcribe an audio file.

        Parameters
        ----------
        audio_path : str
            Path to the audio file.

        Returns
        -------
        dict
            Contains transcript and language.
        """

        if not os.path.exists(audio_path):
            raise FileNotFoundError(
                f"Audio file not found: {audio_path}"
            )

        result = self.model.transcribe(audio_path)

        return {
            "transcript": result["text"].strip(),
            "language": result["language"]
        }


if __name__ == "__main__":

    transcriber = MeetingTranscriber()

    output = transcriber.transcribe("sample.mp3")

    print(output["language"])
    print(output["transcript"])
