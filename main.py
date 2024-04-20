import time
import os

pizza = {
    "Splitza" : 103000,
    "Frankrurter BBQ" : 40000,
    "Cheeseburger" : 42000,
    "Meat Monsta" : 45000,
    "Super Supreme" : 53000,
    "Meat Lovers" : 43000,
    "Pepperoni" : 44000,
    "Splitza" : 49000,
}

add_ons = {
    "cheese" : 15000,
    "Chili" : 1000
}
tax_fee = 3900
def cls():
    os.system("cls")

def main():
    cls()
    while True:
        try:
            print("Aplikasi pemesanan Pizza Hut")
            print("1. Tampilkan Daftar Pizza")
            print("2. Pesan Pizza")
            print("3. Riwayat Pemesanan")
            print("0. Keluar")
            choice = int(input("Pilih :"))

            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 0:
                exit()
            else:
                print("Pilihan Salah!")
                time.sleep(1)
                cls()

        
        
        except Exception as e:
            print("Error " , e)
            time.sleep(1)
            cls()



if __name__ == "__main__":
    main()




    

    




