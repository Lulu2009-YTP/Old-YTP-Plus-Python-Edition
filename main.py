import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import random

# Function to simulate YTP effects
def apply_ytp_effects(clip, imperson_value, waxonator_value):
    # Imperson effect: Apply speed change based on slider
    if imperson_value > 50:
        clip = clip.fx(vfx.speedx, factor=(imperson_value / 50))
    
    # Waxonator effect: Apply random cuts/concatenations based on slider
    if waxonator_value > 50:
        duration = clip.duration
        num_cuts = int(waxonator_value / 10)
        cut_points = sorted([random.uniform(0, duration) for _ in range(num_cuts)])
        clips = [clip.subclip(start, end) for start, end in zip(cut_points[:-1], cut_points[1:])]
        clip = concatenate_videoclips(clips)

    return clip

# Function to select video and apply effects
def select_video():
    filepath = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
    if filepath:
        clip = VideoFileClip(filepath)
        imperson_value = imperson_slider.get()
        waxonator_value = waxonator_slider.get()

        # Apply YTP effects based on slider values
        edited_clip = apply_ytp_effects(clip, imperson_value, waxonator_value)
        
        # Save the edited video
        edited_clip.write_videofile("output.mp4", codec="libx264")
        status_label.config(text="YTP generated and saved as output.mp4")

# Create the GUI window
root = tk.Tk()
root.title("YTP+ [beta]")

# Pooping Style label
style_label = tk.Label(root, text="Pooping Style")
style_label.pack()

# Sliders for Imperson and Waxonator
imperson_label = tk.Label(root, text="Imperson:")
imperson_label.pack()

imperson_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
imperson_slider.pack()

waxonator_label = tk.Label(root, text="Waxonator:")
waxonator_label.pack()

waxonator_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
waxonator_slider.pack()

# Buttons to select video and apply effects
select_button = tk.Button(root, text="Select Video", command=select_video)
select_button.pack()

# Label to show status
status_label = tk.Label(root, text="")
status_label.pack()

# Run the GUI
root.mainloop()
