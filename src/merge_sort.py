from src.my_array import MyArray


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2

    esquerda = MyArray()
    direita = MyArray()

    # copiar manualmente (não pode usar slicing)
    for i in range(meio):
        esquerda.append(arr[i])

    for i in range(meio, len(arr)):
        direita.append(arr[i])

    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)

    return merge(esquerda_ordenada, direita_ordenada)


def merge(left, right):
    resultado = MyArray()

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    # resto da esquerda
    while i < len(left):
        resultado.append(left[i])
        i += 1

    # resto da direita
    while j < len(right):
        resultado.append(right[j])
        j += 1

    return resultado