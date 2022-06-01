def area_quadrado(lado: float) -> float:
    return lado * lado

def area_circulo(raio: float) -> float:
    return 3.14 * raio ** 2

def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def opcoes(opcao: int) -> float:
    if opcao == 1:
        print('Cálculo Area do quadrado\n')
        lado = float(input('Insira o tamanho do lado: '))
        result = area_quadrado(lado)
        return print(f'Área: {round(result, 2)}')
    elif opcao == 2:
        print('Cálculo área do círculo\n')
        raio = float(input('Insira o ráio do círculo: '))
        result = area_circulo(raio)
        return print(f'Área: {round(result, 2)}')
    elif opcao == 3:
        print('Cálculo área do Triangulo\n')
        base = float(input('Insira o tamanho da base: '))
        altura = float(input('Insira a altura do triangulo: '))
        result = area_triangulo(base, altura)
        return print(f'Área: {round(result, 2)}')


def valida_opcoes(opcao: int):
    if opcao > 3:
        return print('Opção inválida!')

def apresentar_opcoes():
    print('1 - Quadrado\n'
          '2 - Círculo\n'
          '3 - Triângulo')
