def reverse_array(arr):
    inicio = 0
    fim = len(arr) - 1

    while inicio < fim:
        temp = arr[inicio]
        arr[inicio] = arr[fim]
        arr[fim] = temp

        inicio += 1
        fim -= 1