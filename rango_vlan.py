# rango_vlan.py

def main():
    vlan = int(input("Ingrese el número de VLAN: "))

    if 1 <= vlan <= 1000:
        print(f"La VLAN {vlan} pertenece al rango normal.")
    elif 1002 <= vlan <= 4094:
        print(f"La VLAN {vlan} pertenece al rango extendido.")
    else:
        print(f"La VLAN {vlan} no pertenece a ninguno de los rangos normales o extendidos.")

if __name__ == "__main__":
    main()
