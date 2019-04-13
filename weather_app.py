import tkinter as tk

# Root window definition
root = tk.Tk()
root.winfo_toplevel().title("Weather App")

# Icon definition
root.iconbitmap(r"./assets/Graphicloads-Colorful-Long-Shadow-Cloud.ico")

# Canvas definition
canvas_attr = {
  "height": 700,
  "width": 800
}
canvas = tk.Canvas(root, **canvas_attr)
canvas.pack()

# Frame definition
frame_place = {
  "relx": 0.1, # Percentage of screen offset on x (both sides)
  "rely": 0.1, # Percentage of screen offset on y (both sides)
  "relwidth": 0.8, # Percentage of screen size on x (both sides)
  "relheight": 0.8 # Percentage of screen size on x (both sides)
} # Note that 0.1 of the screen on both sides of x and y add to
  # 0.2 of the screen size and 0.8 + 0.2 = 1 (100% of screen)
  # These values scale with the size of the window (hence rel)
frame_attr = {
  "bg": "#80c1ff"
}
frame = tk.Frame(root, **frame_attr)
frame.place(**frame_place)

# Button definition
# Button attributes dictionary
button_attr = {
  "text": "Test Button",
  "bg": "gray"
}
# Define button with dictionary unpacking (and keyword parameters)
button = tk.Button(frame, **button_attr)
button.pack()

# Label definition
label_attr = {
  "text": "This is a label",
  "bg": "yellow"
}
label = tk.Label(frame, **label_attr)
label.pack()

# Entry definition
entry_attr = {
  "bg": "green"
}
entry = tk.Entry(frame, **entry_attr)
entry.pack()

# Execute main loop, bring up window
root.mainloop()