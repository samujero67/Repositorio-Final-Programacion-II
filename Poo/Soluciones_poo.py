#Ejercicios de Herencia:
#1.Vehículos
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        if self.velocidad > 200:
            self.velocidad = 200

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.placa = self._generar_placa()

    def _generar_placa(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        numeros = ''.join(random.choices(string.digits, k=3))
        return letras + numeros

    def __str__(self):
        return f"{self.marca} {self.modelo} - Placa: {self.placa} - Puertas: {self.numero_puertas}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo  # deportiva, crucero, etc.

    def hacer_caballito(self):
        if self.velocidad > 30:
            return "¡Caballito!"
        else:
            return "Necesitas más velocidad"

    def __str__(self):
        return f"{self.marca} {self.modelo} - Tipo: {self.tipo}"
    
#2.Figuras Geométricas


class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError('Implementar en subclase')

    def perimetro(self):
        raise NotImplementedError('Implementar en subclase')

    def __str__(self):
        return f"Figura de color {self.color}"

    def descripcion(self):
        return (f"Soy una {type(self).__name__} de color {self.color} "
                f"con área {self.area():.2f} y perímetro {self.perimetro():.2f}")


class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo de radio {self.radio} y color {self.color}"


class Triangulo(Figura):
    def __init__(self, color, base, altura, lado1, lado2, lado3):
        super().__init__(color)
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def __str__(self):
        return f"Triángulo de base {self.base} y color {self.color}"

#3.Sistema de Empleados:

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.id_empleado = self._generar_id()

    def _generar_id(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=4))
        return letras + numeros

    def calcular_salario(self):
        raise NotImplementedError('Implementar en subclase')

    def __str__(self):
        return f"Empleado: {self.nombre} | ID: {self.id_empleado}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def __str__(self):
        return (f"{super().__str__()} | "
                f"{self.horas_trabajadas}h × ${self.tarifa_por_hora}/h")


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono_porcentaje):
        super().__init__(nombre)
        self.salario_base = salario_base
        self.bono_porcentaje = bono_porcentaje

    def calcular_salario(self):
        return self.salario_base * (1 + self.bono_porcentaje / 100)

    def ascender(self, empleado, nuevo_salario_base):
        if isinstance(empleado, Gerente):
            empleado.salario_base = nuevo_salario_base
            return (f"Ascenso exitoso: nuevo salario base de "
                    f"{empleado.nombre} es ${nuevo_salario_base}")
        else:
            return "Error: solo se pueden ascender empleados que sean Gerente"

    def __str__(self):
        return f"{super().__str__()} | Salario base: ${self.salario_base}"

#4.Pila con Historial:

class Pila:
    def __init__(self):
        self._elementos = []

    def apilar(self, elemento):
        self._elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._elementos.pop()

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self._elementos[-1]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def __len__(self):
        return len(self._elementos)

    def __str__(self):
        elementos = list(reversed(self._elementos))
        return f"Pila (tope → base): {elementos}"


class PilaConHistorial(Pila):
    def __init__(self):
        super().__init__()
        self._historial = []

    def apilar(self, elemento):
        super().apilar(elemento)
        self._historial.append(f"APILAR: {elemento}")

    def desapilar(self):
        elemento = super().desapilar()
        self._historial.append(f"DESAPILAR: {elemento}")
        return elemento

    def ver_historial(self):
        for i, operacion in enumerate(self._historial, start=1):
            print(f"{i}. {operacion}")

#5.Herencia Múltiple:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años"

    def informacion(self):
        return f"Persona: {self.nombre}"


class Trabajador:
    def __init__(self, empresa, salario):
        self.empresa = empresa
        self.salario = salario

    def presentarse(self):
        return f"Trabajo en {self.empresa} con salario de ${self.salario}"

    def informacion(self):
        return f"Trabajador en: {self.empresa}"


class EstudianteTrabajador(Persona, Trabajador):
    def __init__(self, nombre, edad, empresa, salario, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, empresa, salario)
        self.universidad = universidad

    def presentarse(self):
        return (f"{Persona.presentarse(self)}. "
                f"{Trabajador.presentarse(self)}. "
                f"Estudio en {self.universidad}")

    def informacion(self):
        return (f"{Persona.informacion(self)} | "
                f"{Trabajador.informacion(self)} | "
                f"Universidad: {self.universidad}")
    
#Ejercicios: Uso básico de métodos de instancia
#1.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

#2.
class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida")

    def consultar_saldo(self):
        return self.saldo

#3.class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        return self.base == self.altura

#4.
class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def __str__(self):
        terminos = []
        for i, coef in enumerate(self.coeficientes):
            if coef == 0:
                continue
            if i == 0:
                terminos.append(f"{coef}")
            elif i == 1:
                terminos.append(f"{coef}x")
            else:
                terminos.append(f"{coef}x^{i}")
        return " + ".join(terminos) if terminos else "0"

    def __add__(self, other):
        max_len = max(len(self.coeficientes), len(other.coeficientes))
        resultado = []

        for i in range(max_len):
            a = self.coeficientes[i] if i < len(self.coeficientes) else 0
            b = other.coeficientes[i] if i < len(other.coeficientes) else 0
            resultado.append(a + b)

        return Polinomio(resultado)

    def __sub__(self, other):
        max_len = max(len(self.coeficientes), len(other.coeficientes))
        resultado = []

        for i in range(max_len):
            a = self.coeficientes[i] if i < len(self.coeficientes) else 0
            b = other.coeficientes[i] if i < len(other.coeficientes) else 0
            resultado.append(a - b)

        return Polinomio(resultado)

    def __mul__(self, other):
        resultado = [0] * (len(self.coeficientes) + len(other.coeficientes) - 1)

        for i in range(len(self.coeficientes)):
            for j in range(len(other.coeficientes)):
                resultado[i + j] += self.coeficientes[i] * other.coeficientes[j]

        return Polinomio(resultado)

    def evaluar(self, x):
        resultado = 0
        for i, coef in enumerate(self.coeficientes):
            resultado += coef * (x ** i)
        return resultado

#5.
class Cajero:
    def __init__(self, n1, n2, n3):
        self.b10 = n1
        self.b20 = n2
        self.b50 = n3

    def retirar(self, cantidad):
        restante = cantidad

        # Copias temporales para intentar la operación
        usar50 = min(restante // 50000, self.b50)
        restante -= usar50 * 50000

        usar20 = min(restante // 20000, self.b20)
        restante -= usar20 * 20000

        usar10 = min(restante // 10000, self.b10)
        restante -= usar10 * 10000

        # Verificar si se pudo completar el monto exacto
        if restante != 0:
            return "No es posible entregar la cantidad solicitada"

        # Actualizar el estado del cajero
        self.b50 -= usar50
        self.b20 -= usar20
        self.b10 -= usar10

        return {
            "50000": usar50,
            "20000": usar20,
            "10000": usar10
        }
