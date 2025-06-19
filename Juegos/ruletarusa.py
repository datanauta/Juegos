import os
import shutil
import random

def eliminar_carpeta(ruta):
    if os.path.exists(ruta):
        shutil.rmtree(ruta)
        print('⚠️ La carpeta ha sido eliminada')
        return True
    else:
        print('❌ La carpeta no existe')
        return False

def ruleta_rusa():
    if random.randint(0, 1) == 1:
        return eliminar_carpeta('cosasImportantes')
    else:
        print('💥 Click... La carpeta permanece intacta')
        return False

while True:
    confirmacion = input('¿Estás seguro de que quieres jugar a la ruleta rusa? (si/no): ')
    if confirmacion.lower() == 'si':
        if ruleta_rusa():
            print('☠️ El juego ha terminado porque la carpeta ha sido eliminada')
            break
    elif confirmacion.lower() == 'no':
        print('✅ Operación cancelada')
        break
    else:
        print('⚠️ Responde solo con "si" o "no"')
