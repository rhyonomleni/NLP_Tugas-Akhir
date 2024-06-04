from flask import Flask, request, jsonify, render_template
import aiml
from tabulate import tabulate
import os
import re

app = Flask(__name__)

# Membuat kernel AIML dan mempelajari berkas AIML
kernel = aiml.Kernel()

# Pastikan direktori kerja adalah direktori proyek
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Memuat file AIML utama
kernel.learn("aiml/resto.xml")
kernel.respond("RESTO")

# Data menu
data = {
    "Nasi Ayam Kremes": 14000,
    "Nasi Ayam Kuah Kecap": 14000,
    "Nasi Telur Kuah Kecap": 9000,
    "Nasi Telur Dadar": 7000,
    "Nasi Koloke": 12000,
    "Nasi Fuyunghai": 12000,
    "Nasi Telur Tempe Terong": 10000,
    "Nasi Tahu Terong": 18000,
    "Nasi Tahu Tempe Terong": 19000,
    "Nasi Tempe Terong": 8000,
    "Nasi Telur Terong": 9000,
    "Nasi Orak Arik": 8000,
    "Nasi Gila": 13000,
    "Nasi Goreng Gila": 14000,
    "Nasi Goreng": 10000,
    "Bakmi Goreng/Kuah": 10000,
    "Bihun Goreng/Kuah": 10000,
    "Cap Cai": 10000,
    "Nasi Godog": 10000,
    "Mie Dok-dok": 10000,
    "Indomie": 6000,
    "Indomie Telur": 9000,
    "Es Teh": 3000,
    "Jeruk Es/Panas": 3000,
    "Milo Es/Panas": 4000,
    "Hilo Es/Panas": 4000,
    "Coffeemix Es/Panas": 4000,
    "GoodDay": 3000,
    "Nutrisari Es/Panas": 4000,
    "GoodDay": 4000,
    "Air Es": 1000,
    "Teh Tawar": 1000,
    "Kopi Hitam": 3000
}
col_names = ["Menu", "Harga"]

minuman = {
    "Es Teh": 3000,
    "Jeruk Es/Panas": 3000,
    "Milo Es/Panas": 4000,
    "Hilo Es/Panas": 4000,
    "Coffeemix Es/Panas": 4000,
    "GoodDay Capucino": 3000,
    "Nutrisari Es/Panas": 4000,
    "GoodDay": 4000,
    "Air Es": 1000,
    "Teh Tawar": 1000,
    "Kopi Hitam": 3000
}
col_minuman = ["Minuman", "Harga"]

makanan = {
    "Nasi Ayam Kremes": 14000,
    "Nasi Ayam Kuah Kecap": 14000,
    "Nasi Telur Kuah Kecap": 9000,
    "Nasi Telur Dadar": 7000,
    "Nasi Koloke": 12000,
    "Nasi Fuyunghai": 12000,
    "Nasi Telur Tempe Terong": 10000,
    "Nasi Tahu Terong": 18000,
    "Nasi Tahu Tempe Terong": 19000,
    "Nasi Tempe Terong": 8000,
    "Nasi Telur Terong": 9000,
    "Nasi Orak-Arik": 8000,
    "Nasi Gila": 13000,
    "Nasi Goreng Gila": 14000,
    "Nasi Goreng": 10000,
    "Bakmi Goreng/Kuah": 10000,
    "Bihun Goreng/Kuah": 10000,
    "Cap Cai": 10000,
    "Nasi Godog": 10000,
    "Mie Dok-dok": 10000,
    "Indomie": 6000,
    "Indomie Telur": 9000,
}
col_makanan = ["Makanan", "Harga"]

# Tambahkan variabel global untuk total harga
kunci = "esan" # Kunci pertama
harga = r'\d+' # Kunci kedua
total = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global total  # Gunakan variabel global total
    user_input = request.json.get("message")
    user_input_split = user_input.split()
    
    # Menyimpan pasangan dua kata berurutan
    pasangan_dua_kata = []
    
    # Mengambil dua kata berurutan
    for i in range(len(user_input_split) - 1):
        pasangan_dua_kata.append(f"{user_input_split[i]} {user_input_split[i + 1]}")
        
    if ('menu minuman' in pasangan_dua_kata or 'daftar minuman' in pasangan_dua_kata):
        table = [[key, value] for key, value in minuman.items()]
        menu_table = tabulate(table, headers=col_minuman, tablefmt="html")
        return jsonify({"response": menu_table})
    elif ('menu makanan' in pasangan_dua_kata or 'daftar makanan' in pasangan_dua_kata):
        table = [[key, value] for key, value in makanan.items()]
        menu_table = tabulate(table, headers=col_makanan, tablefmt="html")
        return jsonify({"response": menu_table})
    elif 'menu' in user_input_split:
        table = [[key, value] for key, value in data.items()]
        menu_table = tabulate(table, headers=col_names, tablefmt="html")
        return jsonify({"response": menu_table})
    
    response = kernel.respond(user_input)
    
    # Menambahkan logika pencarian kunci dan harga serta perhitungan total
    cariKunci = re.search(kunci, response)
    cariHarga = re.findall(harga, response)
    if cariKunci and cariHarga:
        total += int(cariHarga[0])
        response += f" Untuk sekarang total harga adalah: {total}"
    elif cariKunci:
        return jsonify({"response": "Maaf menu tersebut tidak ada disini."})
    
    if response:
        return jsonify({"response": response})
    else:
        return jsonify({"response": "Maaf Kak, saya kurang mengerti. Bisakah diulangi lagi?"})

if __name__ == '__main__':
    app.run(debug=True)
