libros = {
    'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
    'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
    'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
    'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
    'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
    'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
}

prestamos = {
    'L001': [500, 4],
    'L002': [700, 0],
    'L003': [300, 10],
    'L004': [400, 2],
    'L005': [600, 1],
    'L006': [350, 6]
}

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_autor(autor):
    return autor.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_anio(anio):
    return anio.isdigit() and int(anio) > 0

def validar_editorial(editorial):
    return editorial.strip() != ""

def validar_novedad(novedad):
    return novedad.strip().lower() in ("s", "n")

def validar_multa(multa):
    return multa.isdigit() and int(multa) > 0

def validar_copias(copias):
    return copias.isdigit() and int(copias) >= 0

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion = input("Ingrese opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            return int(opcion)
        print("Debe seleccionar una opción válida")

def copias_genero(genero):
    total = 0
    for codigo, datos in libros.items():
        if datos[2].lower() == genero.lower():
            total += prestamos[codigo][1]
    print(f"El total de copias disponibles es: {total}")

def busqueda_multa(multa_min, multa_max):
    encontrados = []
    for codigo, datos in prestamos.items():
        multa = datos[0]
        copias = datos[1]
        if multa_min <= multa <= multa_max and copias != 0:
            titulo = libros[codigo][0]
            encontrados.append(f"{titulo}--{codigo}")
    encontrados.sort()
    if encontrados:
        print(f"Los libros encontrados son: {encontrados}")
    else:
        print("No hay libros en ese rango de multa.")

def actualizar_multa(codigo, nueva_multa):
    codigo = codigo.strip().upper()
    if codigo not in prestamos:
        return False

    prestamos[codigo][0] = nueva_multa
    return True

def agregar_libro(codigo, titulo, autor, genero, anio, editorial, es_novedad, multa, copias):
    codigo = codigo.strip().upper()
    if codigo in libros:
        return False

    libros[codigo] = [
        titulo,
        autor,
        genero,
        anio,
        editorial,
        es_novedad
    ]
    prestamos[codigo] = [
        multa,
        copias
    ]
    return True

def eliminar_libro(codigo):
    codigo = codigo.strip().upper()
    if codigo not in libros:
        return False
    del libros[codigo]
    del prestamos[codigo]
    return True

while True:

    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        genero = input("Ingrese género a consultar: ")
        copias_genero(genero)

    elif opcion == 2:
        while True:
            try:
                multa_min = int(input("Ingrese multa mínima: "))
                multa_max = int(input("Ingrese multa máxima: "))
                if multa_min < 0 or multa_max < 0 or multa_min > multa_max:
                    print("Debe ingresar valores enteros")
                    continue
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_multa(multa_min, multa_max)

    elif opcion == 3:
        while True:
            codigo = input("Ingrese código del libro: ")
            nueva_multa = input("Ingrese nueva multa: ")
            if not validar_multa(nueva_multa):
                print("La multa debe ser un número entero positivo")
            else:
                actualizado = actualizar_multa(
                    codigo,
                    int(nueva_multa)
                )
                if actualizado:
                    print("Multa actualizada")
                else:
                    print("El código no existe")
            respuesta = input("¿Desea actualizar otra multa (s/n)?: ")
            if respuesta.lower() != "s":
                break

    elif opcion == 4:
        codigo = input("Ingrese código del libro: ")
        if not validar_codigo(codigo):
            print("Código inválido")
            continue

        titulo = input("Ingrese título: ")
        if not validar_titulo(titulo):
            print("Título inválido")
            continue

        autor = input("Ingrese autor: ")
        if not validar_autor(autor):
            print("Autor inválido")
            continue

        genero = input("Ingrese género: ")
        if not validar_genero(genero):
            print("Género inválido")
            continue

        anio = input("Ingrese año de publicación: ")
        if not validar_anio(anio):
            print("Año inválido")
            continue

        editorial = input("Ingrese editorial: ")
        if not validar_editorial(editorial):
            print("Editorial inválida")
            continue

        novedad = input("¿Es novedad? (s/n): ")
        if not validar_novedad(novedad):
            print("Debe ingresar s o n")
            continue

        multa = input("Ingrese precio de multa: ")
        if not validar_multa(multa):
            print("Multa inválida")
            continue

        copias = input("Ingrese copias disponibles: ")
        if not validar_copias(copias):
            print("Copias inválidas")
            continue

        agregado = agregar_libro(
            codigo,
            titulo,
            autor,
            genero,
            int(anio),
            editorial,
            novedad.lower() == "s",
            int(multa),
            int(copias)
        )
        if agregado:
            print("Libro agregado")
        else:
            print("El código ya existe")
    elif opcion == 5:
        codigo = input("Ingrese código del libro: ")
        eliminado = eliminar_libro(codigo)
        if eliminado:
            print("Libro eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
