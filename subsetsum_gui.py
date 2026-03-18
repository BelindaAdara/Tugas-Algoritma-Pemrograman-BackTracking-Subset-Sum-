import tkinter as tk
from tkinter import messagebox

class SubsetSumGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualisasi Backtracking: Subset Sum (Dynamic Centered)")
        self.root.geometry("800x550")
        self.root.configure(bg="#f0f2f5")

        # Data Awal
        self.nums = [3, 7, 4, 2, 6, 8]
        self.target = 23
        self.selected = []
        self.rects = []
        self.texts = []

        self.setup_ui()
        self.draw_numbers()

    def setup_ui(self):
        # Bagian Input
        self.input_frame = tk.Frame(self.root, bg="#f0f2f5", pady=10)
        self.input_frame.pack()

        tk.Label(self.input_frame, text="Tambah Angka:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=0, padx=5)
        self.num_entry = tk.Entry(self.input_frame, width=10, font=("Arial", 12))
        self.num_entry.grid(row=0, column=1, padx=5)
        
        self.add_btn = tk.Button(self.input_frame, text="Tambah +", command=self.add_number, 
                                 bg="#10b981", fg="white", font=("Arial", 9, "bold"))
        self.add_btn.grid(row=0, column=2, padx=5)

        tk.Label(self.input_frame, text="Target:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=3, padx=(20, 5))
        self.target_entry = tk.Entry(self.input_frame, width=10, font=("Arial", 12))
        self.target_entry.insert(0, str(self.target))
        self.target_entry.grid(row=0, column=4, padx=5)

        # Header & Canvas
        self.title_label = tk.Label(self.root, text=f"Mencari Subset Berjumlah: {self.target}", 
                                    font=("Helvetica", 16, "bold"), bg="#f0f2f5", pady=10)
        self.title_label.pack()

        self.canvas = tk.Canvas(self.root, width=750, height=150, bg="white", 
                               highlightthickness=2, highlightbackground="#d1d5db")
        self.canvas.pack(pady=10)

        # Panel Informasi
        self.info_frame = tk.Frame(self.root, bg="#f0f2f5")
        self.info_frame.pack(pady=10)

        self.status_msg = tk.Label(self.info_frame, text="Siap memulai pencarian...", 
                                   font=("Courier", 11), fg="#4b5563", bg="#f0f2f5")
        self.status_msg.pack()

        self.path_label = tk.Label(self.info_frame, text="Current Path: []", font=("Arial", 12, "bold"), bg="#f0f2f5")
        self.path_label.pack()

        self.sum_label = tk.Label(self.info_frame, text="Current Sum: 0", font=("Arial", 12), bg="#f0f2f5")
        self.sum_label.pack()

        # Frame Tombol Kontrol
        self.button_frame = tk.Frame(self.root, bg="#f0f2f5")
        self.button_frame.pack(pady=10)

        self.start_btn = tk.Button(self.button_frame, text="Mulai Pencarian", command=self.start_process, 
                                   bg="#3b82f6", fg="white", font=("Arial", 12, "bold"), padx=30, pady=10)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = tk.Button(self.button_frame, text="Reset", command=self.reset_all, 
                                   bg="#ef4444", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
        self.reset_btn.grid(row=0, column=1, padx=10)

    def add_number(self):
        try:
            val = int(self.num_entry.get())
            if len(self.nums) >= 10:
                messagebox.showwarning("Penuh", "Maksimal 10 angka agar tampilan tetap rapi.")
                return
            self.nums.append(val)
            self.num_entry.delete(0, tk.END)
            self.draw_numbers()
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    def reset_all(self):
        """Menghapus angka, target, dan mereset UI"""
        self.nums = []
        self.selected = []
        self.num_entry.delete(0, tk.END)
        self.target_entry.delete(0, tk.END)
        self.draw_numbers()
        self.status_msg.config(text="Data dan Target direset. Silakan input baru.", fg="#4b5563")
        self.path_label.config(text="Current Path: []")
        self.sum_label.config(text="Current Sum: 0")
        self.title_label.config(text="Mencari Subset Berjumlah: -")

    def draw_numbers(self):
        self.canvas.delete("all")
        self.rects = []
        self.texts = []
        
        if not self.nums: return
        
        canvas_width = 750
        spacing = 80  
        total_content_width = (len(self.nums) - 1) * spacing
        start_x = (canvas_width / 2) - (total_content_width / 2)
        
        for i, num in enumerate(self.nums):
            x = start_x + (i * spacing)
            y = 75
            rect = self.canvas.create_rectangle(x-30, y-30, x+30, y+30, fill="#ffffff", outline="#374151", width=2)
            text = self.canvas.create_text(x, y, text=str(num), font=("Arial", 14, "bold"))
            self.rects.append(rect)
            self.texts.append(text)

    def update_ui(self, index, current_sum, msg, color="#ffffff"):
        self.status_msg.config(text=msg)
        self.path_label.config(text=f"Path: {self.selected}")
        self.sum_label.config(text=f"Total Sum: {current_sum}")
        
        if 0 <= index < len(self.nums):
            self.canvas.itemconfig(self.rects[index], fill=color)
        
        self.root.update()
        self.root.after(500) 

    def subset_sum(self, index, current_sum):
        if current_sum == self.target:
            self.status_msg.config(text="🎯 SOLUSI DITEMUKAN!", fg="green")
            return True

        if index >= len(self.nums):
            return False
        
        if current_sum > self.target:
            self.update_ui(index-1, current_sum, "❌ Melebihi target!", "#f87171")
            return False

        num = self.nums[index]
        self.selected.append(num)
        self.update_ui(index, current_sum + num, f"Coba ambil: {num}", "#86efac")

        if self.subset_sum(index + 1, current_sum + num):
            return True

        self.selected.pop()
        self.update_ui(index, current_sum, f"Lepas {num}, coba lainnya...", "#fbbf24")
        self.canvas.itemconfig(self.rects[index], fill="#ffffff")
        
        if self.subset_sum(index + 1, current_sum):
            return True

        return False

    def start_process(self):
        if not self.nums:
            messagebox.showwarning("Kosong", "Tambahkan angka dahulu!")
            return
            
        try:
            self.target = int(self.target_entry.get())
        except:
            messagebox.showerror("Error", "Target tidak valid!")
            return

        for rect in self.rects:
            self.canvas.itemconfig(rect, fill="#ffffff")

        self.title_label.config(text=f"Mencari Subset Berjumlah: {self.target}")
        self.start_btn.config(state="disabled")
        self.add_btn.config(state="disabled")
        self.reset_btn.config(state="disabled")
        
        self.selected = []
        found = self.subset_sum(0, 0)
        
        if not found:
            self.status_msg.config(text="Tidak ada kombinasi cocok.", fg="red")
            messagebox.showinfo("Selesai", "Pencarian selesai tanpa hasil.")
        else:
            messagebox.showinfo("Sukses", f"Solusi: {self.selected}")
        
        self.start_btn.config(state="normal")
        self.add_btn.config(state="normal")
        self.reset_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = SubsetSumGUI(root)
    root.mainloop()
