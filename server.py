import socket
import threading
from server_config import HOST, PORT, LISTENER_LIMIT

def main():
    """
    The main entry point for the server script. This function sets up a socket and attempts to bind it to the specified HOST and PORT.
    If the binding fails, it returns an error message in the form of a dictionary.
    If the binding is successful, the server is set to listen for incoming connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
    except Exception as e:
        return {"error":f"Unable to bind to {HOST} and {PORT} - {str(e)}"}
    
    server.listen(LISTENER_LIMIT)
