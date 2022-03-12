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
        print("[i] Coming soon...")
        aaa = input("...")
    elif inpu == "4":
        gate_main.go_git()
    else:
        print("[e] Retry")
    cls()