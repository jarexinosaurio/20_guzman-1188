
print(" ")#imprime en la pantalla un espacio en blanco
print("guzman 1188")#imprime en la pantallada mi nombre
print(" ")#imprime en la pantalla un espacio en blanco
def tri_recursion(k):
    """Función recursiva que calcula la suma de números """
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
