from TTS.api import TTS

tts_engine = TTS(
    model_name="tts_models/en/ljspeech/tacotron2-DDC",
    progress_bar=False
)

class FreeTTS:
    def synthesize(self, text):
        wav = tts_engine.tts(text)
        return wav.astype("float32").tobytes()

tts_model = FreeTTS()
