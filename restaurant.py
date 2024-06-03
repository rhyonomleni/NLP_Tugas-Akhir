import aiml
from tabulate import tabulate


# membuat kernel dan mempelajari berkas AIML
kernel = aiml.Kernel()
kernel.learn("resto.xml")
kernel.respond("resto")

# menu = [
#     {"item": "Nasi Ayam Kremes", "price": 14000},
#     {"item": "Nasi Ayam Kuah Kecap", "price": 14000},
#     {"item": "Ayam Bakar", "price": 25.000},
#     {"item": "Sate Ayam", "price": 30.000},
#     {"item": "Es Teh", "price": 5.000}
# ]

# def generate_menu_table(menu):
#     html = "<table border='1'><tr><th>Makanan</th><th>Harga</th></tr>"
#     for item in menu:
#         html += f"<tr><td>{item['item']}</td><td>{item['price']}</td></tr>"
#     html += "</table>"
#     return html

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
    #define header names

    #display table
table = [[key, value] for key, value in data.items()]
print(tabulate(table, headers=["Menu", "Harga"], tablefmt="grid"))

while True:
    user_input = kernel.respond(input("USER > "))
    if user_input:
        # print("Coba dulu")
        print("Bot > ", user_input)
    else:
        print("Bot > Maaf Ka, saya kurang mengerti. Bisakah diulangi lagi?" )

    # print(kernel.respond(input("Tuliskan pesan di sini: >> ")))