from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from backend.llm_module import generate
from backend.audio_module import tts_model
from backend.turndetect import is_silent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# FREE dummy STT (replace later with Whisper if needed)
class DummySTT:
    def recognize(self, audio):
        return "Hello, this is a free local AI assistant"

stt = DummySTT()

@app.websocket("/ws/audio")
async def audio_ws(ws: WebSocket):
    await ws.accept()
    while True:
        audio = await ws.receive_bytes()
        audio_np = np.frombuffer(audio, dtype=np.float32)

        if is_silent(audio_np):
            continue

        text = stt.recognize(audio_np)
        reply = generate(text)
        voice = tts_model.synthesize(reply)

        await ws.send_bytes(voice)



