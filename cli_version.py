import gate_main
import os
gate_main.update()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

print(">>> WELLKOME <<<")
while True:
    print("[0] - Exit")
    print("[1] - Search")
    print("[2] - Parser list")
    print("[3] - Go Book")
    print("[4] - Go GitHub")
    inpu = input(": ")
    cls()
    if inpu == "0":
        exit()
    elif inpu == "1":
        print("[i] Coming soon...")
        aaa = input("...")
    elif inpu == "2":
        pars_list = gate_main.list()
        for ii in pars_list:
            print("[*]", ii)
        aaa = input("...")
    elif inpu == "3":
        url = input("url: ")
        datas = gate_main.get_info_book(url)
        cls()
        if datas["code"] == 1:
            print(">>>",datas["name"],"<<<\n->",datas["status"], "-",str(datas["chapters"]),"\n",datas["desc"])
            cyclic_i = 1
            print("[0] - Exit\n[1] - Download")
            while cyclic_i == 1:
                inpu = input(": ")
                if inpu == "0":
                    cyclic_i = 0
                if inpu == "1":
                    cyclic_i = 0
                    down_data = gate_main.down(datas["url"])
            aaa = input("...")
        else:
            print("[e]", datas["desce"])
            aaa = input("...")
    elif inpu == "4":
        gate_main.go_git()
    else:
        print("[e] Retry")
    cls()