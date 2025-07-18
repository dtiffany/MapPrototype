import tkinter

window = tkinter.Tk()
window.title("Map_Prototype.py")
window.geometry("500x700")

# Key Binds
window.bind("<Up>", lambda event: move(1))
window.bind("w", lambda event: move(1))
window.bind("<Right>", lambda event: move(2))
window.bind("d", lambda event: move(2))
window.bind("<Down>", lambda event: move(3))
window.bind("s", lambda event: move(3))
window.bind("<Left>", lambda event: move(4))
window.bind("a", lambda event: move(4))
window.bind("<space>", lambda event: graph(OGX_coord, OGY_coord))
window.bind("<BackSpace>", lambda event: undo())
window.bind("<Delete>", lambda event: reset())

def draw_grid(canvas, width, height, spacing=10, color="#cccccc"):
    
    # Draw vertical lines
    for x in range(0, width, spacing):
        canvas.create_line(x, 0, x, height, fill=color)
    
    # Draw horizontal lines
    for y in range(0, height, spacing):
        canvas.create_line(0, y, width, y, fill=color)



OGX_coord = 200
OGY_coord = 150

x_coord_display = 0
y_coord_display = 0

graph_lines = []



lbl_header = tkinter.Label(text="Map Prototype")
author_header = tkinter.Label(text="Author: Dylan Tiffany")

lbl_header.pack(pady=10)
author_header.pack(pady=10)

# Canvas is for the graph
canvas = tkinter.Canvas(window, width=400, height=300, bg="white")
canvas.pack()

# Draw faint grid
draw_grid(canvas, 400, 300, spacing=10, color="#dddddd")


# Draw axes
canvas.create_line(200, 0, 200, 300, fill="black")  # Y-axis
canvas.create_line(0, 150, 400, 150, fill="black")  # X-axis

r = 5
dot = canvas.create_oval(OGX_coord - r, OGY_coord - r, OGX_coord + r, OGY_coord + r, fill="blue")






control_frame = tkinter.Frame(window)
control_frame.pack(pady=20)


up_btn = tkinter.Button(control_frame, text="Up", bg="#B3E6C1", fg="black", activebackground="green", activeforeground="white", command=lambda: move(1))
left_btn = tkinter.Button(control_frame, text="Left", bg="#B3E6C1", fg="black", activebackground="green", activeforeground="white", command=lambda: move(4))
right_btn = tkinter.Button(control_frame, text="Right", bg="#B3E6C1", fg="black", activebackground="green", activeforeground="white", command=lambda: move(2))
down_btn = tkinter.Button(control_frame, text="Down", bg="#B3E6C1", fg="black", activebackground="green", activeforeground="white", command=lambda: move(3))
coord_header = tkinter.Label(control_frame, text=f"({x_coord_display}, {y_coord_display})")


graph_btn = tkinter.Button(control_frame, text="Draw Graph", bg="lightblue", fg="black", activebackground="blue", activeforeground="white", command=lambda: graph(OGX_coord, OGY_coord))
reset_btn = tkinter.Button(control_frame, text="Reset", bg="#FFBBBB", fg="black", activebackground="red", activeforeground="white", command=lambda: reset())
undo_btn = tkinter.Button(control_frame, text="Undo", bg="#D8BFD8", fg="black", activebackground="white", activeforeground="white", command=lambda: undo())


up_btn.grid(row=0, column=1, padx=5, pady=15)
left_btn.grid(row=1, column=0, padx=10, pady=5)
coord_header.grid(row=1, column=1, padx=15, pady=15)
right_btn.grid(row=1, column=2, padx=10, pady=5)
down_btn.grid(row=2, column=1, padx=5, pady=15)

graph_btn.grid(row=5, column=1, padx=15, pady=15)
reset_btn.grid(row=5, column=0, padx=15, pady=15)
undo_btn.grid(row=5, column=2, padx=15, pady=15)



def move(key, event=None):
    # Key values
        # 1 = Up
        # 2 = Right
        # 3 = Down
        # 4 = Left

    global OGX_coord, OGY_coord
    global x_coord_display, y_coord_display

    step = 10 # pixels
    
    if key == 1:
        if y_coord_display < 15:
            OGY_coord -= step
            y_coord_display += 1
    elif key == 2:
        if x_coord_display < 20:
            OGX_coord += step
            x_coord_display += 1

    elif key == 3:
        if y_coord_display > -15:
            OGY_coord += step
            y_coord_display -= 1
    elif key == 4:
        if x_coord_display > -20:
            OGX_coord -= step
            x_coord_display -= 1
    
    canvas.coords(dot, OGX_coord - r, OGY_coord - r, OGX_coord + r, OGY_coord + r)

    coord_header.config(text=f"({x_coord_display}, {y_coord_display})")


def graph(x, y):


    line_id = canvas.create_line(200, 150, x, y, fill="red", width=2)
    graph_lines.append(line_id)

    '''
    x_disp = x - 200
    y_disp = 150 - y


    if x_disp == 0 and y_disp == 0:
        return
    
    if x_disp == 0:

        canvas.create_line(200,0,200,300, fill="red", width=2)
        return
    slope = y_disp / x_disp
    '''

def reset():
    for line in graph_lines:
        canvas.delete(line)
    graph_lines.clear()

def undo():
    if graph_lines:
        last_line = graph_lines.pop()
        canvas.delete(last_line)




window.mainloop()