from pathlib import Path
import shutil

from sedes import obtener_sede


RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
BANDEJA_ENTRADA = RAIZ_PROYECTO / "bandeja_entrada"
PEDIDOS_ORDENADOS = RAIZ_PROYECTO / "pedidos_ordenados"
PARA_REVISAR = RAIZ_PROYECTO / "revisar"

SEDES = ("Itagüí", "Envigado", "Sabaneta")


def organizar_pedidos():
    if not BANDEJA_ENTRADA.is_dir():
        print("No existe bandeja_entrada/. Ejecuta primero generar_pedidos.py.")
        return

    conteo_por_sede = {sede: 0 for sede in SEDES}
    conteo_revision = 0

    for sede in SEDES:
        (PEDIDOS_ORDENADOS / sede).mkdir(parents=True, exist_ok=True)

    for archivo in sorted(BANDEJA_ENTRADA.iterdir()):
        if not archivo.is_file():
            continue

        sede = obtener_sede(archivo)

        if sede in conteo_por_sede:
            carpeta_destino = PEDIDOS_ORDENADOS / sede
            conteo_por_sede[sede] += 1
        else:
            carpeta_destino = PARA_REVISAR
            conteo_revision += 1

        carpeta_destino.mkdir(parents=True, exist_ok=True)
        shutil.copy(archivo, carpeta_destino / archivo.name)

    print("Pedidos copiados por sede:")
    for sede, cantidad in conteo_por_sede.items():
        print(f"- {sede}: {cantidad}")

    print(f"- Para revisar: {conteo_revision}")
    print("La bandeja original no se modificó.")


if __name__ == "__main__":
    organizar_pedidos()
