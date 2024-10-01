def fibonacci_sequence(n):
    primario = 0
    segundario = 1
    fibonacci = primario + segundario
    while True:
        primario = fibonacci
        segundario += fibonacci
        fibonacci = primario + segundario
        print(primario, segundario, fibonacci)
        if fibonacci == n:
            return print("Pertence a sequencia!")
        elif fibonacci > n:
            return print("Nao pertence a sequencia!")

n = int(input("Qual numero deseja verificar na sequencia de Fibonacci?: "))
fibonacci_sequence(n)