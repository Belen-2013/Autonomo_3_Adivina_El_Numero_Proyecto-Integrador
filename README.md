# 🎮 ADIVINA EL NÚMERO

![Juego Adivina el Número](https://img.icons8.com/color/96/000000/question-mark.png)

## 👩‍💻 Datos del Proyecto

**Nombre del proyecto:** Adivina el Número  
**Nombre de la estudiante:** María Belén Beltrán Beltrán  
**Carrera:** Inteligencia Artificial  
**Nivel:** Primer semestre  
**Fecha de elaboración:** 27/06/2026  

---

# 📌 Descripción del Proyecto

**Adivina el Número** es un juego desarrollado en Python utilizando la librería **Pygame**, que permite crear una interfaz gráfica interactiva para que el usuario pueda participar en el juego.

El sistema genera un número secreto de manera aleatoria y el jugador debe intentar descubrirlo ingresando diferentes valores mediante el teclado. Durante el proceso, el programa proporciona pistas indicando si el número ingresado es mayor o menor que el número oculto, ayudando al usuario a encontrar la respuesta en el menor número de intentos posible.

---

# 🎯 Objetivo del Sistema

El objetivo de este sistema es permitir que el usuario adivine un número secreto generado aleatoriamente mediante intentos interactivos, utilizando pistas que faciliten la búsqueda y logrando encontrar la respuesta en el menor tiempo posible.

Además, busca aplicar conceptos fundamentales de programación como:
- Variables.
- Condicionales.
- Ciclos repetitivos.
- Entrada de datos.
- Generación de números aleatorios.
- Desarrollo de interfaces gráficas.

---

# ⚙️ Funcionalidades del Sistema

El programa cuenta con las siguientes funcionalidades:

✅ **Generación de números aleatorios**  
- El sistema crea un número secreto utilizando la librería `random`.
- El número generado se encuentra dentro de un rango establecido.

✅ **Ingreso de números mediante teclado**  
- El usuario puede escribir sus intentos directamente en la interfaz gráfica.

✅ **Comparación lógica del intento**  
- El sistema compara el número ingresado por el usuario con el número secreto.
- Determina si la respuesta es correcta o necesita otro intento.

✅ **Sistema de pistas**  
- Si el número ingresado es mayor, el programa indica que debe buscar un número menor.
- Si el número ingresado es menor, indica que debe buscar un número mayor.

✅ **Mensajes de respuesta**
- Muestra información al usuario durante el juego.
- Indica cuando el jugador gana.

✅ **Contador de intentos**
- Registra la cantidad de veces que el usuario intenta adivinar el número.

✅ **Interfaz gráfica con Pygame**
- Cuenta con una ventana interactiva.
- Presenta títulos, mensajes, número ingresado e intentos.
- Incluye diseño visual mediante colores y textos.

---

# 🛠️ Tecnologías Utilizadas

- **Lenguaje de programación:** Python 🐍
- **Librería gráfica:** Pygame
- **Generación aleatoria:** Random

---

# 🧠 Funcionamiento del Programa

1. El sistema inicia creando la interfaz gráfica.
2. Se genera un número secreto aleatorio.
3. El usuario ingresa un número mediante el teclado.
4. El programa compara el intento con el número oculto.
5. Se muestra una pista:
   - Número ingresado demasiado alto.
   - Número ingresado demasiado bajo.
   - Número correcto.
6. Se incrementa el contador de intentos.
7. El juego continúa hasta que el usuario encuentre el número correcto.

---

# 📂 Estructura del Proyecto
