from Alumno import Alumno
from Nota import Nota

def main():
    alumnos = []
    
    while True:
        print("\n--- INGRESE DATOS DEL ALUMNO ---")
        
        while True:
            nombre_completo = input("Ingrese el nombre completo: ").strip().title()
            if nombre_completo == "":
                print("El nombre no puede estar vacío.")
            elif not nombre_completo.replace(" ", "").isalpha():
                print("El nombre debe contener solo letras.")
            else:
                break
        
        while True:
            legajo_str = input("Ingrese el legajo (entero): ")
            if legajo_str.isdigit():
                legajo = int(legajo_str)
                break
            print("El legajo debe ser un número entero.")
        
        lista_notas = []

        while True:
            print("\n-- Carga de Nota --")
            catedra = input("Ingrese el nombre de la cátedra: ").strip()
            if catedra == "":
                print("La cátedra no puede estar vacía.")
                continue
                
            while True:
                nota_str = input("Ingrese la nota del examen (0 a 10): ")
                try:
                    notaExamen = float(nota_str)
                    if 0 <= notaExamen <= 10:
                        break
                    print("La nota debe estar comprendida entre 0 y 10.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")
            
            nueva_nota = Nota(catedra, notaExamen)
            lista_notas.append(nueva_nota)
            
            # Consultar si desea salir de la carga de notas
            salirNotas = input("¿Desea salir de la carga de notas? (s/n): ").strip().lower()
            if salirNotas == 's':
                if len(lista_notas) == 0:
                    print("Debe ingresar al menos 1 nota.")
                    continue
                break

        nuevo_alumno = Alumno(nombre_completo, legajo, lista_notas)
        alumnos.append(nuevo_alumno)
        
        salirAlumno = input("\n¿Desea salir de la carga de alumnos? (s/n): ").strip().lower()
        if salirAlumno == 's':
            break


    print("       INFORMACIÓN DE ALUMNOS       ")
    print("="*40)
    
    for alumno in alumnos:
        print(f"Alumno: {alumno.nombre_completo} | Legajo: {alumno.legajo}")
        print("Calificaciones por Cátedra:")
        for nota in alumno.notas:
            print(f"  * {nota.catedra}: {nota.notaExamen}")
            
        promedio = alumno.calcular_promedio()
        print(f"El promedio del alumno es: {promedio:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()