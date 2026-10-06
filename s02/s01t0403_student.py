'''
NOTAS:
1. Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.
2. Es ver cuanto crece el numero de
operaciones en mi algoritmo conforme
crece el tamaño de la entrada
agrego las bigO identificadas
teniemdo en cuenta la Cota superior asintotica
O(n) + 4*0(1) = O(n+4) = O(n)
'''

# Creando una lista de estudiantes
student_list_01 =['Jonatan','Andrea','Joseline','Daniel']
student_list_01 =['Saul','Jatziri','Guadalupe','Axel']

# Verificando la presencia de un estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student: # 0(n)
            print("✅ Estudiante encontrado") # 0(1)
            return student
    # Si no encuentro al estudiante
    print("❌ Estudiante no encontrado")
    return None

# Probando algoritmo
check_student("Walter",student_list_01) # 0(1) 