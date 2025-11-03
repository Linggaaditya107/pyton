import tkinter as tk

def prediksi_prodi():
    # Fungsi ini selalu mengembalikan "Prodi Teknologi Informasi" terlepas dari input
    hasil_label.config(text="Prodi Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")


# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.pack(pady=10)

# Daftar nama mata pelajaran (10 buah)
mata_pelajaran = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Sejarah", "Geografi", "Ekonomi", "Sosiologi"
]

# Frame untuk input nilai
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Membuat 10 entry fields dengan label
entries = []
for i, pelajaran in enumerate(mata_pelajaran):
    label = tk.Label(input_frame, text=f"{pelajaran}:")
    label.grid(row=i, column=0, sticky="w", padx=5, pady=2)
    entry = tk.Entry(input_frame, width=20)
    entry.grid(row=i, column=1, padx=5, pady=2)
    entries.append(entry)

# Button Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi, font=("Arial", 12))
prediksi_button.pack(pady=10)

# Label untuk hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
hasil_label.pack(pady=10)

# Menjalankan loop utama
root.mainloop()






   
