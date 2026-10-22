from array import array as arr

# Parametros de mi cuadricula
rows = 3
columns = 2 * rows - 1

# Crando el grid 2D
matrix = []
# Construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la construccion del Grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas {len(matrix[0])}") 

for row in matrix:
    print(list(row))
