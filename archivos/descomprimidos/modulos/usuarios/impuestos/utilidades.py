if __name__ != "__main__":
    from ..gestion.crud import guardar

    print(__name__)

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()

    print("tarea de mantenimineto")


if __name__ == "__main__":
    print("tarea de mantenimiento")
