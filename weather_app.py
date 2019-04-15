#!/usr/bin/python3

import tkinter as tk
import platform

# Root window definition
root = tk.Tk()
root.winfo_toplevel().title("Weather App")

# Icon definition
if platform.system == "Windows":
  root.iconbitmap(r"./assets/Graphicloads-Colorful-Long-Shadow-Cloud.ico")

# Canvas definition
canvas_attr = {
  "height": 700,
  "width": 800
}
canvas = tk.Canvas(root, **canvas_attr)
canvas.pack()

# Top Frame definition
frame_place = {
  "relx": 0.5, # Percentage of screen offset on x (both sides)
  "rely": 0.1, # Percentage of screen offset on y (both sides)
  "relwidth": 0.75, # Percentage of screen size on x (both sides)
  "relheight": 0.1, # Percentage of screen size on x (both sides)
  "anchor": "n"
} # Note that 0.1 of the screen on both sides of x and y add to
  # 0.2 of the screen size and 0.8 + 0.2 = 1 (100% of screen)
  # These values scale with the size of the window (hence rel)
frame_attr = {
  "bg": "#80c1ff",
  "bd": 5
}
frame = tk.Frame(root, **frame_attr)
frame.place(**frame_place)

# Entry definition
entry_attr = {
  "font": 40
}
entry_place = {
  "relwidth": 0.65,
  "relheight": 1
}
entry = tk.Entry(frame, **entry_attr)
entry.place(**entry_place)

# Button definition
# Button attributes dictionary
button_attr = {
  "text": "Test Button",
  "font": 40
}
button_place = {
  "relx": 0.7,
  "relwidth": 0.3,
  "relheight": 1
}
# Define button with dictionary unpacking (and keyword parameters)
button = tk.Button(frame, **button_attr)
button.place(**button_place)

# Bottom Frame definition
bottom_frame_place = {
  "relx": 0.5, # Percentage of screen offset on x (both sides)
  "rely": 0.25, # Percentage of screen offset on y (both sides)
  "relwidth": 0.75, # Percentage of screen size on x (both sides)
  "relheight": 0.6, # Percentage of screen size on x (both sides)
  "anchor": "n"
} # Note that 0.1 of the screen on both sides of x and y add to
  # 0.2 of the screen size and 0.8 + 0.2 = 1 (100% of screen)
  # These values scale with the size of the window (hence rel)
bottom_frame_attr = {
  "bg": "#80c1ff",
  "bd": 10
}
bottom_frame = tk.Frame(root, **bottom_frame_attr)
bottom_frame.place(**bottom_frame_place)

# Label definition
label_attr = {
  "text": "This is a label",
  "bg": "white"
}
label_place = {
  "relwidth": 1,
  "relheight": 1
}
label = tk.Label(bottom_frame, **label_attr)
label.place(**label_place)

# Execute main loop, bring up window
root.mainloop()