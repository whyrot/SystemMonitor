import psutil
import time 
import os
import tkinter as tk
from tkinter import ttk

discoveros = os.name

root = tk.Tk()
root.title("System Monitor")
root.geometry("400x200") 

cpu_label = tk.Label(root, text="CPU: ...", font=("Verdana", 14))
cpu_label.pack(pady=10)
cpu_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=100)
cpu_bar.pack(pady=5)
ram_label = tk.Label(root, text="Ram: ...", font=("Verdana", 14))
ram_label.pack(pady=10)
disk_label = tk.Label(root, text="Disk: ...", font=("Verdana", 14))
disk_label.pack(pady=10)

def update_stats():
    cpu = psutil.cpu_percent()
    cpu_label.config(text=f"CPU: {cpu}%")
    cpu_bar["value"] = cpu
    ram = ramtotal = psutil.virtual_memory().total / (1024 **3)
    ramused = psutil.virtual_memory().used / (1024**3)
    ram_label.config(text=f'Ram Used: {ramused:.2f}GB/{ramtotal}GB')
    if discoveros == 'posix':
        disktotal = psutil.disk_usage(os.path.expanduser("~")).total  / (1024**3)
        diskused = psutil.disk_usage(os.path.expanduser("~")).used / (1024**3)
        disk_label.config(text=f'Storage Use: {diskused:.2f}GB/{disktotal:.2f}GB')
    if discoveros == "nt":
        disktotal = psutil.disk_usage("C:/").total / (1024**3)
        diskused = psutil.disk_usage("C:/").used / (1024**3)
        disk_label.config(text=f'Storage Use: {diskused:.2f}GB/{disktotal:.2f}GB')
    
    root.after(2000, update_stats)
update_stats()
root.mainloop()




   