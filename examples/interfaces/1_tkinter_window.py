"""Giving your program a face, option 1: a desktop window, with tkinter.

tkinter ships with Python itself. Nothing to install, no account, no internet.
It draws a real window on a real machine.

WHERE THIS RUNS
---------------
On your own laptop: yes.
In a Codespace: no, and the reason is worth understanding. A Codespace is a
computer in a data centre. It has no screen, no mouse and nobody sitting in
front of it. A window has nowhere to be drawn. Some images do not even ship the
tkinter module.

That is not a bug, it is the difference between a desktop program and a server
program. Remember it for the two other files in this folder: those two draw a
web page, and a web page travels.
"""

# We try the import instead of assuming it, so the message stays useful
try:
    import tkinter as tk
except ModuleNotFoundError:
    print("tkinter is not available here.")
    print("This is normal in a Codespace. Run this file on your own machine,")
    print("or look at 2_gradio_page.py, which works everywhere.")
    raise SystemExit(0)


def audit(impressions, clicks):
    """CTR, in percent. One job, one function."""
    if impressions == 0:
        return 0.0
    return clicks / impressions * 100


def show():
    # 1. The window itself
    window = tk.Tk()
    window.title("Campaign audit")
    window.geometry("360x200")

    # 2. What goes in it. pack() places the element in the window
    tk.Label(window, text="Campaign: spring_sale", font=("Helvetica", 14)).pack(pady=10)

    ctr = audit(impressions=283000, clicks=6792)
    tk.Label(window, text="CTR: %.2f %%" % ctr, font=("Helvetica", 20)).pack(pady=10)

    # 3. A button, and the function it calls when clicked
    tk.Button(window, text="Close", command=window.destroy).pack(pady=10)

    # 4. mainloop waits for the user. The program stops here until the window closes
    window.mainloop()


show()

# What to remember
# 1. tkinter is in the standard library. No pip install, no account, no internet
# 2. It draws on a machine that has a screen. A Codespace has none
# 3. mainloop() waits for a human. Your script no longer decides when it ends
# 4. The audit() function above knows nothing about windows. That is the point:
#    the logic stays the same whatever face you put on it
