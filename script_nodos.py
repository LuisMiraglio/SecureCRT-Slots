import time

def main():
    # Verifica si el objeto crt está disponible
    if "crt" not in globals():
        print("Este script debe ejecutarse dentro de SecureCRT.")
        return

    # Diccionario con los slots y datos de olt
    slots = {
        "1-1": ["1-1-1-{}".format(i) for i in range(1, 65)],
        "1-2": ["1-1-2-{}".format(i) for i in range(1, 65)],
        "1-3": ["1-1-3-{}".format(i) for i in range(1, 65)],
        "1-4": ["1-1-4-{}".format(i) for i in range(1, 65)],
        "1-5": ["1-1-5-{}".format(i) for i in range(1, 65)],
        "1-6": ["1-1-6-{}".format(i) for i in range(1, 65)],
        "1-7": ["1-1-7-{}".format(i) for i in range(1, 65)],
        "1-8": ["1-1-8-{}".format(i) for i in range(1, 65)],
        
        "2-1": ["1-2-1-{}".format(i) for i in range(1, 65)],
        "2-2": ["1-2-2-{}".format(i) for i in range(1, 65)],
        "2-3": ["1-2-3-{}".format(i) for i in range(1, 65)],
        "2-4": ["1-2-4-{}".format(i) for i in range(1, 65)],
        "2-5": ["1-2-5-{}".format(i) for i in range(1, 65)],
        "2-6": ["1-2-6-{}".format(i) for i in range(1, 65)],
        "2-7": ["1-2-7-{}".format(i) for i in range(1, 65)],
        "2-8": ["1-2-8-{}".format(i) for i in range(1, 65)],
        
        "3-1": ["1-3-1-{}".format(i) for i in range(1, 65)],
        "3-2": ["1-3-2-{}".format(i) for i in range(1, 65)],
        "3-3": ["1-3-3-{}".format(i) for i in range(1, 65)],
        "3-4": ["1-3-4-{}".format(i) for i in range(1, 65)],
        "3-5": ["1-3-5-{}".format(i) for i in range(1, 65)],
        "3-6": ["1-3-6-{}".format(i) for i in range(1, 65)],
        "3-7": ["1-3-7-{}".format(i) for i in range(1, 65)],
        "3-8": ["1-3-8-{}".format(i) for i in range(1, 65)],
        
        "4-1": ["1-4-1-{}".format(i) for i in range(1, 65)],
        "4-2": ["1-4-2-{}".format(i) for i in range(1, 65)],
        "4-3": ["1-4-3-{}".format(i) for i in range(1, 65)],
        "4-4": ["1-4-4-{}".format(i) for i in range(1, 65)],
        "4-5": ["1-4-5-{}".format(i) for i in range(1, 65)],
        "4-6": ["1-4-6-{}".format(i) for i in range(1, 65)],
        "4-7": ["1-4-7-{}".format(i) for i in range(1, 65)],
        "4-8": ["1-4-8-{}".format(i) for i in range(1, 65)],
        
        "5-1": ["1-5-1-{}".format(i) for i in range(1, 65)],
        "5-2": ["1-5-2-{}".format(i) for i in range(1, 65)],
        "5-3": ["1-5-3-{}".format(i) for i in range(1, 65)],
        "5-4": ["1-5-4-{}".format(i) for i in range(1, 65)],
        "5-5": ["1-5-5-{}".format(i) for i in range(1, 65)],
        "5-6": ["1-5-6-{}".format(i) for i in range(1, 65)],
        "5-7": ["1-5-7-{}".format(i) for i in range(1, 65)],
        "5-8": ["1-5-8-{}".format(i) for i in range(1, 65)],
        
        "6-1": ["1-6-1-{}".format(i) for i in range(1, 65)],
        "6-2": ["1-6-2-{}".format(i) for i in range(1, 65)],
        "6-3": ["1-6-3-{}".format(i) for i in range(1, 65)],
        "6-4": ["1-6-4-{}".format(i) for i in range(1, 65)],
        "6-5": ["1-6-5-{}".format(i) for i in range(1, 65)],
        "6-6": ["1-6-6-{}".format(i) for i in range(1, 65)],
        "6-7": ["1-6-7-{}".format(i) for i in range(1, 65)],
        "6-8": ["1-6-8-{}".format(i) for i in range(1, 65)],
        
        "7-1": ["1-7-1-{}".format(i) for i in range(1, 65)],
        "7-2": ["1-7-2-{}".format(i) for i in range(1, 65)],
        "7-3": ["1-7-3-{}".format(i) for i in range(1, 65)],
        "7-4": ["1-7-4-{}".format(i) for i in range(1, 65)],
        "7-5": ["1-7-5-{}".format(i) for i in range(1, 65)],
        "7-6": ["1-7-6-{}".format(i) for i in range(1, 65)],
        "7-7": ["1-7-7-{}".format(i) for i in range(1, 65)],
        "7-8": ["1-7-8-{}".format(i) for i in range(1, 65)],
    }

    # Pedir al usuario el número del slot
    slot = crt.Dialog.Prompt("Ingrese el Slot a escanear (por ejemplo, 1-1):", "Seleccionar Slot", "")

    # Validar si el slot existe
    if not slot or slot not in slots:
        crt.Dialog.MessageBox("Slot no encontrado o formato inválido. Verifique el número e intente de nuevo.")
        return

    # Obtener la sesión de SecureCRT
    crt.Screen.Synchronous = True  
    
    # Mostrar mensaje al usuario
    crt.Dialog.MessageBox("Iniciando escaneo de 64 OLTs. Esto puede tomar unos momentos...")

    # Ejecutar el comando "onu status" para las OLTs del slot seleccionado
    total_olts = len(slots[slot])
    for i, olt in enumerate(slots[slot]):
        comando = "onu status {}".format(olt)
        crt.Screen.Send(comando + "\r")
        # Reducir el tiempo de espera para mejorar la velocidad
        time.sleep(1)  

    crt.Screen.Synchronous = False
    crt.Dialog.MessageBox("Completado el escaneo del slot {}".format(slot))

main()
