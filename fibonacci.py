def fibonacci(numero):
    a, b = 0, 1
    num_fibonacci = [a]
    
    while a <= numero:
        if a != 0:
            num_fibonacci.append(a)
        a, b = b, a + b
        
    pertence = numero in num_fibonacci
    return pertence, num_fibonacci
        
num = int(input("Digite um número: "))
pertence, sequencia = fibonacci(num)

if pertence:
    print (f"O número {num} pertence a sequência")
else:
    print(f"O numero {num} não pertence a sequencia")
    
print("Sequencia fibonnaci: ", sequencia)
