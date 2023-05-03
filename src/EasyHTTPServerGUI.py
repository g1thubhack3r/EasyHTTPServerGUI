import tkinter as tk
import tkinter.messagebox as msgbox
import flask
root = tk.Tk()
root.title("EasyHTTPServerGUI")
description = tk.Label(root, text="""
Enter the address where the HTTP server run in the first entry,
and the port in the second entry,
the path in the third,
and the content in the fourth.
""")
description.pack()
host = tk.Entry(root)
host.pack()
hostvar = tk.StringVar(host, "127.0.0.1")
host['textvariable'] = hostvar
port = tk.Entry(root)
portvar = tk.StringVar(port, "80")
port['textvariable'] = portvar
port.pack()
path = tk.Entry(root)
pathvar = tk.StringVar(path, "/")
path['textvariable'] = pathvar
path.pack()
content = tk.Text(root)
content.pack()
def serverrun(topw, host, port, path, content):
    app = flask.Flask(__name__)
    @app.route(path)
    def index():
        nonlocal content
        return content
    topw.destroy()
    msgbox.showinfo("Message", "Server started")
    try:
        app.run(host=host, port=port, debug=False)
    except Exception as e:
        msgbox.showerror("Error", "There is an error in the HTTP server, error message: " + str(e))
    finally:
        msgbox.showinfo("Message", "Server stopped")
runbutton = tk.Button(root, text="Run", command=(lambda: serverrun(root, hostvar.get(), int(portvar.get()), path.get(), content.get(1.0, tk.END))))
runbutton.pack()
root.mainloop()
