import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import os 

from yt_dlp import YoutubeDL

PATH = os.path.expanduser("~/FILMY")

class AppGUI:
	def __init__(self):
		self.main_window = tk.Tk(className=" YouTube mp4 konwerter")
		self.main_window.configure(bg="white")
		self.main_window.geometry("500x60")

		self.input_frame = tk.Frame(self.main_window, bg="white")
		self.controls_frame = tk.Frame(self.main_window, bg="white")

		self.prompt_label = tk.Label(self.input_frame,
										  text="Link YouTube:",
										  bg="white")
		self.link_entry = tk.Entry(self.input_frame, width=50, bg="white", fg="black", relief="solid")

		self.prompt_label.pack(side="left")
		self.link_entry.pack(side="left")

		self.convert_button = tk.Button(self.controls_frame,
											 text="Pobierz",
											 command=self.convert, bg="white", fg="black", highlightthickness=0, activebackground='white', relief="solid")
		self.quit_button = tk.Button(self.controls_frame,
										  text="Wyjdz",
										  command=self.main_window.destroy, bg="white",fg="black", highlightthickness=0, activebackground='white', relief="solid")

		self.convert_button.pack(side="left")
		self.quit_button.pack(side="left")

		self.input_frame.pack()
		self.controls_frame.pack()

		tk.mainloop()

	def convert(self):
		link = self.link_entry.get()

		if len(link) > 0:
			try:
				with YoutubeDL() as ydl:
					ydl.download(link)
					showinfo("Sukces", "Film pobrany")
			except:
				showerror("Blad", "Nieprawidlowy link")			
		else:
			showerror("Blad", "Podaj link.")

os.chdir(PATH)
AppGUI()