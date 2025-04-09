from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, send, emit

from source.employees.routes import initialize_routes as initialize_employee_routes
from source.projects.routes import initialize_routes as initialize_project_routes
from source.customers.routes import initialize_routes as initialize_customer_routes
from source.daily_logs.routes import initialize_routes as initialize_daily_log_routes
from source.project_budgets.routes import initialize_routes as initialize_project_budgets_routes

app = Flask(__name__)
api = Api(app)

initialize_employee_routes(api)
initialize_project_routes(api)
initialize_customer_routes(api)
initialize_daily_log_routes(api)
initialize_project_budgets_routes(api)

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('chat_response', {'msg': 'Welcome to the chat!'})


@socketio.on('chat')
def handle_chat(data):
    print(f"Chat event received: {data}")
    # Send the response to all connected clients
    emit('chat_response', {'msg': f"Echo: {data['msg']}"}, broadcast=True)


# @socketio.on("message")
# def handle_message(msg):
#     print(f"Message received: {msg}")
#     send(f"Server received: {msg}", broadcast=True)  # Broadcast message to all connected clients


@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")


if __name__ == "__main__":
    socketio.run(app, debug=True, logger=True, engineio_logger=True)
