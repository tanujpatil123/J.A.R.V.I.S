import customtkinter as  ctk
import tkinter as tk
from PIL import Image, ImageTk


def get_entry_value():
    value = text_entry.get()
    text_entry.delete(0, 'end')
    return value


def update_prompt(text):
    get_entry_value()
    text_entry.insert(0, text)

def update_response(text):
    lable_out.configure(text=text, wraplength=310)


def gui_appear():
    ctk.set_appearance_mode("dark")
    # Create the main window
    app = ctk.CTk()
    app.geometry("450x500")
    app.title("J.A.R.V.I.S.")

    global text_entry, lable_out

    # Load the GIF
    gif_path = "ui\\0.gif"
    gif = Image.open(gif_path)

    # Extract frames
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))  # Move to the next frame
    except EOFError:
        pass



    # Create a label to display the GIF
    gif_label = tk.Label(app)
    gif_label.pack()
    # Function to animate the GIF
    def animate_gif(frame_index):
        gif_label.config(image=frames[frame_index])
        frame_index = (frame_index + 1) % len(frames)
        app.after(50, animate_gif, frame_index)  # Adjust the delay as needed


    lable1 = ctk.CTkLabel(app, text="Response", fg_color="transparent", font=("Helvetica", 12, "bold"))
    lable1.pack()



    frame1 = ctk.CTkScrollableFrame(master=app, width=350, height=150)
    frame1.pack(expand=True)

    lable_out = ctk.CTkLabel(frame1, text="Yes Sir, what we are doing today.", fg_color="transparent", justify="left")
    lable_out.pack(pady=10, padx=10)




    frame2 = ctk.CTkFrame(master=app, width=300, height=200)
    frame2.pack(expand=True)

    lable2 = ctk.CTkLabel(frame2, text="Your Prompt", fg_color="transparent")
    lable2.pack()


    # Create a text entry widget
    text_entry = ctk.CTkEntry(frame2, placeholder_text="Ask anything......", width=300)
    text_entry.pack(pady=5, padx=10)





    # Create a send button
    send_button = ctk.CTkButton(frame2, text="Send", command=get_entry_value)
    send_button.pack(pady=5)




    # Start the animation
    animate_gif(0)


    # Run the application
    app.mainloop()


