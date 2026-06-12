# ==============================================================================
# TRABAJO PRÁCTICO N°2: TEORIA DE CONJUNTOS APLICADA A REDES DE FIBRA OPTICA
# ==============================================================================

print("=========================================================")
print("  SISTEMA DE GESTION Y AUDITORIA DE REDES DE FIBRA OPTICA  ")
print("=========================================================\n")

# ------------------------------------------------------------------------------
# LECTURA DE DATOS 
# ------------------------------------------------------------------------------
# Se ingresan las descripciones del universo y de cada conjunto para que el sistema sea dinamico y adaptable a cualquier problematica.

universo_desc = input("Descripcion del Universo (Ej: Tecnicos de planta externa): ")
total_u = int(input(f"Cantidad total de elementos en el Universo (|U|): "))

print("\n--- Nombres de los Conjuntos ---")
conj_a_nom = input("Nombre del Conjunto A : ")
conj_b_nom = input("Nombre del Conjunto B : ")
conj_c_nom = input("Nombre del Conjunto C : ")

print("\n--- Totales por Conjunto ---")
total_a = int(input(f"Total generales con {conj_a_nom} (|A|): "))
total_b = int(input(f"Total generales con {conj_b_nom} (|B|): "))
total_c = int(input(f"Total generales con {conj_c_nom} (|C|): "))

print("\n--- Intersecciones Dobles ---")
int_ab = int(input(f"Cantidad que comparte {conj_a_nom} y {conj_b_nom} (|A n B|): "))
int_ac = int(input(f"Cantidad que comparte {conj_a_nom} y {conj_c_nom} (|A n C|): "))
int_bc = int(input(f"Cantidad que comparte {conj_b_nom} y {conj_c_nom} (|B n C|): "))

print("\n--- Intersección Triple ---")
int_abc = int(input(f"Cantidad que posee los tres elementos simultaneamente (|A n B n C|): "))

# ------------------------------------------------------------------------------
# PROCESAMIENTO
# ------------------------------------------------------------------------------
# Logica "De adentro hacia afuera": se limpia el centro para aislar las regiones puras.

#Calcular las intersecciones exclusivas (solo dos conjuntos)
solo_int_ab = int_ab - int_abc
solo_int_ac = int_ac - int_abc
solo_int_bc = int_bc - int_abc

#Calcular los elementos exclusivos de cada conjunto (solo una herramienta)
solo_a = total_a - (solo_int_ab + solo_int_ac + int_abc)
solo_b = total_b - (solo_int_ab + solo_int_bc + int_abc)
solo_c = total_c - (solo_int_ac + solo_int_bc + int_abc)

#Calcular el complemento (elementos fuera de los conjuntos)
total_en_conjuntos = solo_a + solo_b + solo_c + solo_int_ab + solo_int_ac + solo_int_bc + int_abc
ninguno = total_u - total_en_conjuntos

# ------------------------------------------------------------------------------
#RESULTADOS 
# ------------------------------------------------------------------------------
print("\n" + "="*57)
print("             REPORTES Y RESULTADOS FINALES")
print("="*57)
print(f"Universo analizado: {universo_desc} (Total: {total_u})")
print("-"*57)
print(f"Equipamiento completo (Los 3 conjuntos): {int_abc}")
print("-"*57)
print(f"Tecnicos con ÚNICAMENTE DOS herramientas:")
print(f"    - Solo {conj_a_nom} y {conj_b_nom}: {solo_int_ab}")
print(f"    - Solo {conj_a_nom} y {conj_c_nom}: {solo_int_ac}")
print(f"    - Solo {conj_b_nom} y {conj_c_nom}: {solo_int_bc}")
print("-"*57)
print(f" Tecnicos con UNICAMENTE UNA herramienta:")
print(f"    - Exclusivo {conj_a_nom}: {solo_a}")
print(f"    - Exclusivo {conj_b_nom}: {solo_b}")
print(f"    - Exclusivo {conj_c_nom}: {solo_c}")
print("-"*57)
print(f" Sin equipamiento asignado en estas areas (Afuera): {ninguno}")
print("=========================================================")