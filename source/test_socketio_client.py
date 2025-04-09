import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("✅ Connected to server")
    sio.emit("chat", {"msg": "Hello from Python client"})


@sio.event
def disconnect():
    print("❌ Disconnected from server")


@sio.on("chat_response")
def on_chat_response(data):
    print("📨 Server says:", data)


if __name__ == "__main__":
    sio.connect("http://localhost:5000")
    sio.wait()
