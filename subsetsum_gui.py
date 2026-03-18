import tkinter as tk
from tkinter import messagebox

# Konfigurasi Data
nums = [3, 7, 5, 2, 6, 8]
target = 24

class SubsetSumGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualisasi Backtracking: Subset Sum")
        self.root.geometry("700x450")
        self.root.configure(bg="#f0f2f5")

        # Header
        self.title_label = tk.Label(root, text=f"Mencari Subset Berjumlah: {target}", 
                                    font=("Helvetica", 16, "bold"), bg="#f0f2f5", pady=10)
        self.title_label.pack()

        # Canvas Angka
        self.canvas = tk.Canvas(root, width=650, height=150, bg="white", highlightthickness=2, highlightbackground="#d1d5db")
        self.canvas.pack(pady=10)

        # Panel Informasi
        self.info_frame = tk.Frame(root, bg="#f0f2f5")
        self.info_frame.pack(pady=10)

        self.status_msg = tk.Label(self.info_frame, text="Siap memulai...", font=("Courier", 12), fg="#4b5563", bg="#f0f2f5")
        self.status_msg.pack()

        self.path_label = tk.Label(self.info_frame, text="Current Path: []", font=("Arial", 12, "bold"), bg="#f0f2f5")
        self.path_label.pack()

        self.sum_label = tk.Label(self.info_frame, text="Current Sum: 0", font=("Arial", 12), bg="#f0f2f5")
        self.sum_label.pack()

        # Tombol Kontrol
        self.start_btn = tk.Button(root, text="Mulai Pencarian", command=self.start_process, 
                                   bg="#3b82f6", fg="white", font=("Arial", 10, "bold"), padx=20)
        self.start_btn.pack(pady=5)

        self.selected = []
        self.rects = []
        self.texts = []
        self.draw_numbers()

    def draw_numbers(self):
        self.canvas.delete("all")
        self.rects.clear()
        self.texts.clear()
        
        # Logika Rata Tengah
        canvas_width = 650
        spacing = 90
        total_width = (len(nums) - 1) * spacing
        start_x = (canvas_width - total_width) / 2
        
        for i, num in enumerate(nums):
            x = start_x + i * spacing
            y = 75
            
            # Gambar Kotak
            rect = self.canvas.create_rectangle(x-35, y-35, x+35, y+35, fill="#ffffff", outline="#374151", width=2)
            text = self.canvas.create_text(x, y, text=str(num), font=("Arial", 18, "bold"))
            
            self.rects.append(rect)
            self.texts.append(text)

    def update_ui(self, index, current_sum, msg, color="#ffffff"):
        self.status_msg.config(text=msg)
        self.path_label.config(text=f"Path: {self.selected}")
        self.sum_label.config(text=f"Total Sum: {current_sum}")
        
        if index < len(nums):
            self.canvas.itemconfig(self.rects[index], fill=color)
        
        self.root.update()
        self.root.after(700) 

    def subset_sum(self, index, current_sum):
        # 1. Cek Solusi
        if current_sum == target:
            self.status_msg.config(text="🎯 SOLUSI DITEMUKAN!", fg="green")
            return True

        # 2. Base Case (Gagal)
        if index >= len(nums):
            return False
        
        if current_sum > target:
            self.update_ui(index-1, current_sum, "❌ Melebihi target! Backtracking...", "#f87171")
            return False

        # --- OPSI 1: AMBIL ANGKA ---
        num = nums[index]
        self.selected.append(num)
        self.update_ui(index, current_sum + num, f"Mencoba: Tambahkan {num}", "#86efac") 

        if self.subset_sum(index + 1, current_sum + num):
            return True

        # --- OPSI 2: BACKTRACK (TIDAK AMBIL) ---
        self.selected.pop()
        self.update_ui(index, current_sum, f"Backtrack: Lewati {num}", "#fbbf24") 
        
        self.canvas.itemconfig(self.rects[index], fill="#ffffff")
        
        if self.subset_sum(index + 1, current_sum):
            return True

        return False

    def start_process(self):
        self.start_btn.config(state="disabled")
        for r in self.rects: self.canvas.itemconfig(r, fill="white")
        
        found = self.subset_sum(0, 0)
        if not found:
            self.status_msg.config(text="Tidak ada solusi yang ditemukan.", fg="red")
            messagebox.showinfo("Selesai", "Pencarian selesai. Tidak ada subset yang cocok.")
        else:
            messagebox.showinfo("Sukses", f"Solusi ditemukan: {self.selected}")
        self.start_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = SubsetSumGUI(root)
    root.mainloop()