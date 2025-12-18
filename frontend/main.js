const ws = new WebSocket("ws://localhost:8000/ws/audio");
const audioCtx = new AudioContext();

navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
    const source = audioCtx.createMediaStreamSource(stream);
    const processor = audioCtx.createScriptProcessor(4096, 1, 1);

    source.connect(processor);
    processor.connect(audioCtx.destination);

    processor.onaudioprocess = e => {
        ws.send(e.inputBuffer.getChannelData(0).buffer);
    };
});

ws.onmessage = e => {
    const audio = new Audio(URL.createObjectURL(new Blob([e.data])));
    audio.play();
};
