
import socket

HOST = "0.0.0.0"
PORT = 5000
LOG_FILE = "simulation_log.txt"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(1)

print(f"Listening on port {PORT}...")
print(f"Saving events to {LOG_FILE}")

try:
    while True:
        conn, addr = server.accept()
        print(f"\nConnected: {addr}")

        with conn:
            while True:
                data = conn.recv(1024)

                if not data:
                    print("Client disconnected.")
                    break

                message = data.decode("utf-8", errors="replace")

                print("Received:", message)

                with open(LOG_FILE, "a", encoding="utf-8") as file:
                    file.write(message)
                    file.flush()

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    server.close()
