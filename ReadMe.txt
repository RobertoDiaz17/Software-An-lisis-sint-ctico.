**Objetivo del Software**

El objetivo principal de este software es realizar un análisis léxico y sintáctico básico de expresiones en un lenguaje simplificado. Específicamente, busca:

Análisis Léxico: Dividir el texto de entrada en una secuencia de tokens significativos (números, operadores, paréntesis, y opcionalmente palabras clave).
Análisis Sintáctico: Verificar si la secuencia de tokens generada por el analizador léxico se ajusta a las reglas gramaticales definidas para el lenguaje. En caso de ser válida, construye una representación estructurada (en este caso, una tupla anidada) del árbol de sintaxis abstracta (AST) de la expresión. Si la entrada no cumple con las reglas gramaticales, reporta un error de sintaxis.

Instrucciones para Ejecutar el Programa

**Para ejecutar este programa, sigue estos pasos:**

Guarda los archivos:

Guarda el código del analizador léxico en un archivo llamado lexer.py.
Guarda el código del analizador sintáctico en un archivo llamado parser.py en el mismo directorio.
Abre tu terminal o símbolo del sistema: Navega hasta el directorio donde guardaste los archivos lexer.py y parser.py.

Ejecuta el analizador sintáctico: Utiliza el siguiente comando para ejecutar el script del parser:

Bash

python parser.py
El script parser.py importará y utilizará el lexer definido en lexer.py para analizar las expresiones de ejemplo que están dentro de su bloque if __name__ == '__main__':.

Observa la salida: El programa imprimirá en la consola el resultado del análisis sintáctico para las expresiones de ejemplo. Si la sintaxis es correcta, mostrará la representación del AST. Si hay errores, mostrará un mensaje de error de sintaxis.

**Ejemplos de Entrada y Salida**

A continuación, se presentan algunos ejemplos de cómo el software procesaría diferentes entradas y cuál sería la salida esperada:

Ejemplo 1: Expresión Aritmética Simple

Entrada: 3 + 4
Salida: ('+', ('NUMBER', 3), ('NUMBER', 4))
El parser reconoce la suma de dos números y genera una tupla donde el primer elemento es el operador y los siguientes son los operandos.
Ejemplo 2: Expresión con Paréntesis y Multiplicación

Entrada: (10 - 2) * 5
Salida: ('*', ('-', ('NUMBER', 10), ('NUMBER', 2)), ('NUMBER', 5))
El parser respeta la precedencia dada por los paréntesis y la multiplicación.