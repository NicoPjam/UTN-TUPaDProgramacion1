from Funct import Elementos as f

class GestionNotas:

    @staticmethod
    def ejecutar():
        Alumnos = {
            60902: "Rodolfo Fernandez",
            61654: "Luis Gomez",
            61852: "Andrea Pereira",
            61754: "Juan Cruz Gonzales"
        }

        notasFinales = [
            ["Rodolfo Fernandez", 0.0],
            ["Luis Gomez", 0.0],
            ["Andrea Pereira", 0.0],
            ["Juan Cruz Gonzales", 0.0]
        ]

        indice_alumno = 0

        for legajo in Alumnos:
            nombre = Alumnos[legajo]
            
            print("\n" + "=" * 50)
            print(f"Alumno: {nombre} (Legajo: {legajo})")
            print("=" * 50)
            
            notas_alumno = [
                ["Ciencias", 0.0, 0.0, 0.0],
                ["Historia", 0.0, 0.0, 0.0],
                ["Geografia", 0.0, 0.0, 0.0],
                ["Matematicas", 0.0, 0.0, 0.0],
                ["Fisica", 0.0, 0.0, 0.0]
            ]
            
            for materia in notas_alumno:
                print(f"\nIngrese las notas para {materia[0]}:")
                materia[1] = f.solicitar_nota("  Nota 1: ")
                materia[2] = f.solicitar_nota("  Nota 2: ")
                
                materia[3] = (materia[1] + materia[2]) / 2
                print(f"  Nota Final ({materia[0]}): {materia[3]:.2f}")
            
            print(f"\n--- Resumen de materias: {nombre} ---")
            print(f"{'Materia'} | {'Nota 1'} | {'Nota 2'} | {'Nota Final'}")
            print("-" * 50)
            for fila in notas_alumno:
                print(f"{fila[0]} | {fila[1]:.2f} | {fila[2]:.2f} | {fila[3]:.2f}")
            
            materia_max = notas_alumno[0]
            for fila in notas_alumno[1:]:
                if fila[3] > materia_max[3]:
                    materia_max = fila
            print(f"\n-> Materia con mejor nota: '{materia_max[0]}' con {materia_max[3]:.2f}")
            
            acumulado_promedios = 0.0
            cantidad_materias = 0
            for fila in notas_alumno:
                acumulado_promedios += fila[3]
                cantidad_materias += 1
                
            promedio_general = acumulado_promedios / cantidad_materias

            notasFinales[indice_alumno][1] = promedio_general
            print(f"-> Promedio general de {nombre}: {promedio_general:.2f}")
            
            indice_alumno += 1

        print("RESUMEN GENERAL DE PROMEDIOS")
        for reg in notasFinales:
            print(f"{reg[0]} | Promedio General: {reg[1]:.2f}")

        
        max_promedio = notasFinales[0][1]
        for reg in notasFinales[1:]:
            if reg[1] > max_promedio:
                max_promedio = reg[1]

        mejores_alumnos = []
        for reg in notasFinales:
            if reg[1] == max_promedio:
                mejores_alumnos.append(reg[0])

        cantidad_mejores = 0
        for _ in mejores_alumnos:
            cantidad_mejores += 1

        if cantidad_mejores == 1:
            print(f"EL MEJOR PROMEDIO FUE DE: {mejores_alumnos[0]} CON {max_promedio:.2f}")
        else:
            print(f"HUBO EMPATE EN EL MEJOR PROMEDIO CON {max_promedio:.2f}:")
            for alumno in mejores_alumnos:
                print(f" - {alumno}")
                
        print("*" * 50)

GestionNotas.ejecutar()