import time
import os
from prettytable import PrettyTable
import locale
locale.setlocale( locale.LC_ALL, '' )

table = PrettyTable()
table_addon = PrettyTable()

pizza = [
    ["splitza",103000],
    ["Frankrurter BBQ",40000],
    ["Cheeseburger",42000],
    ["Meat Monsta",45000],
    ["Super Supreme",53000],
    ["Meat Lovers",43000],
    ["Pepperoni",44000]       
    ]

table.field_names = ["No" , "Nama pizza" , "Harga"]
table_addon.field_names = ["No" , "Nama" , "Harga"]



add_ons = [
    ["cheese" , 4500],
    ["Chili" , 1000]
]

tax_fee = 3900

order_history = []

def cls():
    os.system("cls")


def rupiah_format(angka, with_prefix=False, desimal=0):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format_string("%.*f", (desimal, angka), True)
    if with_prefix:
        return "Rp {}".format(rupiah)
    return rupiah

def add_to_table():
    # print("Menu : \n")
    for i in range(len(pizza)):
        # print(f"Nama : {pizza[i][0]}")

        harga  = rupiah_format(pizza[i][1] , True)
      
        table.add_row([i+1,pizza[i][0], harga])
        # print(f"harga : {pizza[i][1]}")

def add_to_table_addon():
    for i in range(len(add_ons)):
        harga  = rupiah_format(add_ons[i][1] , True)
        table_addon.add_row([i+1,add_ons[i][0], harga])

        


def order():
    print("======= Pesan Pizza =======")
    print(table)

    try:
        orderNum = int(input("Pilih pizza no (kembali = 0):"))
        if orderNum == 0:
            return
       
        if (orderNum - 1) < len(pizza):
            pizza_name = pizza[orderNum - 1][0] 
            pizza_price = pizza[orderNum - 1][1]
            # print(f"anda memesan {pizza_name} dengan harga {pizza_price}")
            print(table_addon)

            isWantExtra = input("ingin pesan tambahan (y/n) ? ")
            if isWantExtra == "y":
                choiceExtra = int(input("pilih : "))
                if (choiceExtra - 1) < len(add_ons):
                    extra_name = add_ons[choiceExtra - 1][0] 
                    extra_price = add_ons[choiceExtra - 1][1]

                    total = pizza_price + extra_price + tax_fee 
                    # menambahkan pesanan ke list jika membeli extra menu
                    order_history.append([pizza_name, pizza_price, extra_name, extra_price , total])


                    # print(f"{extra_name} {extra_price} {total}")



                else :  
                    print("menu tidak ada")
            elif isWantExtra == "n":
                # menambahkan pesanan ke list jika tidak membeli extra menu

                pass
            else : 
                print("input salah")

            # order_history.append([pizza_name, pizza_price])
            # print(order_history)

            
        else :  
            print("menu tidak ada")


    except Exception as e:
        print(e)


def orderHistory():
    pass

def main():
    cls()
    add_to_table()
    add_to_table_addon()

    while True:
        try:
            print("Aplikasi pemesanan Pizza Hut")
            print("1. Tampilkan Daftar Pizza")
            print("2. Pesan Pizza")
            print("3. Riwayat Pemesanan")
            print("0. Keluar")
            choice = int(input("Pilih :"))

            if choice == 1:
                print(table)
            elif choice == 2:
                order()
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




    

    




