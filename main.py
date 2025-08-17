import psutil
import time 
import os
import tkinter as tk
from tkinter import ttk

discoveros = os.name

#create main screen
root = tk.Tk()
root.title("System Monitor")
root.geometry("400x200") 

#sets labels for each part
cpu_label = tk.Label(root, text="CPU: ...", font=("Verdana", 14))
cpu_label.pack(pady=10)
cpu_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=100)
cpu_bar.pack(pady=5)
ram_label = tk.Label(root, text="Ram: ...", font=("Verdana", 14))
ram_label.pack(pady=10)
disk_label = tk.Label(root, text="Disk: ...", font=("Verdana", 14))
disk_label.pack(pady=10)

#gathers information to monitor
def update_stats():
    #gets and prints cpu info
    cpu = psutil.cpu_percent()
    cpu_label.config(text=f"CPU: {cpu}%")
    cpu_bar["value"] = cpu
    #gets and prints ram info
    ramtotal = psutil.virtual_memory().total / (1024 **3)
    ramused = psutil.virtual_memory().used / (1024**3)
    ram_label.config(text=f'Ram Used: {ramused:.2f}GB/{ramtotal:.2f}GB')
    
    #detects the OS and prints disk into
    if discoveros == 'posix':
        disktotal = psutil.disk_usage(os.path.expanduser("~")).total  / (1024**3)
        diskused = psutil.disk_usage(os.path.expanduser("~")).used / (1024**3)
        disk_label.config(text=f'Storage Use: {diskused:.2f}GB/{disktotal:.2f}GB')
    if discoveros == "nt":
        disktotal = psutil.disk_usage("C:\\").total / (1024**3)
        diskused = psutil.disk_usage("C:\\").used / (1024**3)
        disk_label.config(text=f'Storage Use: {diskused:.2f}GB/{disktotal:.2f}GB')
    
    #loops every 2 secs
    root.after(2000, update_stats)

#runs everything
update_stats()
root.mainloop()
