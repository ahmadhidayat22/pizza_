import time
import os
from prettytable import PrettyTable
import locale
locale.setlocale( locale.LC_ALL, '' )

table = PrettyTable()


pizza = [
    ["splitza",103000],
    ["Frankrurter BBQ",40000],
    ["Cheeseburger",42000],
    ["Meat Monsta",45000],
    ["Super Supreme",53000],
    ["Meat Lovers",43000],
    ["Pepperoni",44000]       
    ]



tax_fee = 3900
chilli = 5500
order_history = []

def cls():
    os.system("cls")


# memformat harga dari integer biasa menjadi rupiah 
def rupiah_format(angka, with_prefix=False, desimal=0):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format_string("%.*f", (desimal, angka), True)
    if with_prefix:
        return "Rp {}".format(rupiah)
    return rupiah

# menambahkan data pizza ke dalam prettytable 
def add_to_table():
    table.field_names = ["No" , "Nama pizza" , "Harga"]
    for i in range(len(pizza)):
        
        harga  = rupiah_format(pizza[i][1] , True)
        table.add_row([i+1,pizza[i][0], harga])
      

def order():
    time.sleep(1)
    cls()
    print("======= Pesan Pizza =======")
    while True:
        print(table)

        try:
            orderNum = int(input("Pilih pizza no (kembali = 0):"))
            if orderNum == 0 :
                return
            elif orderNum < 0:
                print("pilihan salah......")
                time.sleep(1)
                cls()
                order()
        
            if (orderNum - 1) < len(pizza):
                pizza_name = pizza[orderNum - 1][0] 
                pizza_price = pizza[orderNum - 1][1]
                total = pizza_price + tax_fee

                
                extra_chili =  input("apakah anda ingin menambahkan chili (y/n) ?")
                if extra_chili == "y":
                    print("pizza = " , pizza_price)
                    print("chili = 5.000")
                    print("tax fee = ", tax_fee)
                    total += chilli
                    total = rupiah_format(total, True , 0)
                    pizza_name += " + chili"
                    print("total = ",total )
                elif extra_chili == "n":
                    total = rupiah_format(total, True , 0)
                    print("tax fee = ", tax_fee)
                    print("total = ",total )
                else :
                    print("pilihan tidak ada")
                    order()



                order_history.append([pizza_name, total])
                print("pizza berhasil dipesan")
                input("\ntekan enter untuk melanjutkan....")
                cls()
                return
                
            else :  
                print("menu tidak ada")


        except Exception as e:
            print(e)
            time.sleep(1)
            cls()
            order()



def orderHistory():
    if not order_history:
        print("data kosong")
        time.sleep(1)
        cls()
        return
   
    print(">>>>> Riwayat Pemesanan <<<<<")
    
   
    for i in order_history:
        nama, total = i
        print(f"{nama:4} = {total}")
    print("\n-------------------------------")

def add_pizza():
    while True:
        try:
            print(">>>>> Tambah Menu Pizza <<<<<")
            nama_pizza = input("Nama pizza :").lower()
            harga = int(input("Harga : "))

            for i in range(len(pizza)):
                if nama_pizza in pizza[i][0]:
                    print("nama pizza sudah ada")
                    add_pizza()

            pizza.append([nama_pizza , harga])
            print("menu berhasil ditambah")
            time.sleep(1)
            cls()
            break
        except Exception as e:
            print(e)
    
def update_pizza():
    while True:
        try :
            print(">>>>> Update Menu Pizza <<<<<")

            print(table)
            number = int(input("ubah nomor (kembali = 0):"))

            if number < 0 or number > len(pizza):
                print("pilihan salah") 
                update_pizza()
            elif number == 0 :
                return
            
            
            new_name = input("Nama pizza baru :")
            new_price = int(input("harga baru :"))

            pizza[number-1][0] =new_name
            pizza[number-1][1] =new_price
            print("pizza berhasil diubah")

            input("tekan untuk melanjutkan.....")
            break

        
        except Exception as e:
            print(e)
    
def del_pizza():
     while True:
        try :
            print(">>>>> hapus Menu Pizza <<<<<")

            print(table)
            number = int(input("Hapus nomor (kembali = 0):"))

            if number < 0 or number > len(pizza):
                print("pilihan salah") 
                del_pizza()
            elif number == 0 :
                break
            
            pizza.pop(number-1)
            table.clear()
            add_to_table()
            print("pizza berhasil di hapus")

            input("tekan untuk melanjutkan.....")
            break

        
        except Exception as e:
            print(e)

def main():
    cls()
    add_to_table()
   
    while True:
        try:
            print("Aplikasi pemesanan Pizza Hut")
            print("1. Tampilkan Daftar Pizza")
            print("2. Pesan Pizza")
            print("3. Riwayat Pemesanan")
            print("4. Tambah menu Pizza")
            print("5. Ubah menu Pizza")
            print("6. Hapus menu Pizza")
            print("0. Keluar")
            choice = int(input("Pilih :"))

            match choice:
                case 1:
                    cls()
                    print(table)
                
                case 2:
                    order()
                
                case 3 :
                    orderHistory()
                
                case 4 :
                    add_pizza()

                case 5 :
                    update_pizza()

                case 6 :
                    del_pizza()

                case 0 :
                    print("thank you :)")
                    exit()

                case _ :
                    print("Pilihan Salah!")
                    time.sleep(1)
                    cls()


        
        except Exception as e:
            print("Error " , e)
            time.sleep(1)
            cls()



if __name__ == "__main__":
    main()




    

    




