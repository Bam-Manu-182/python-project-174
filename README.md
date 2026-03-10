### Hexlet tests and linter status:
[![Actions Status](https://github.com/Bam-Manu-182/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Bam-Manu-182/python-project-174/actions)



Project. Difference Calc

Badge: GitHub CI
[![Python CI](https://github.com/Bam-Manu-182/python-project-174/actions/workflows/python-test.yml/badge.svg)](https://github.com/Bam-Manu-182/python-project-174/actions/workflows/python-test.yml)

Badge: Codeclimate - Maintainability
[![Maintainability](https://qlty.sh/gh/Bam-Manu-182/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/Bam-Manu-182/projects/python-project-174)


Descripción:
Difference Calc (Gendiff)
Difference Calc es una herramienta de línea de comandos (CLI) desarrollada en Python que permite comparar dos archivos de configuración y determinar sus diferencias. Es capaz de procesar formatos JSON y YAML, devolviendo el resultado en tres formatos distintos según la necesidad del usuario.


Características y Especificaciones
• Soporte de Formatos: Lectura de archivos `.json`, `.yml` y `.yaml`.

• Comparación Profunda: Capacidad recursiva para comparar objetos anidados.

• Arquitectura Modular: Separación clara entre el motor de comparación, los parsers y los formateadores.

• Formatos de Salida:

1. Stylish: Formato tipo árbol con sangría y signos `+` / `-` (estándar).

2. Plain: Formato de texto plano con frases descriptivas sobre los cambios.

3. JSON: Salida estructurada ideal para ser procesada por otras herramientas.


Requisitos del Sistema
• Sistemas Operativos: Windows (Powershell / CMD / WSL), macOS, Linux.

• Versiones de Python: Compatible con Python 3.10 o superior (Probado en 3.12).

• Gestor de Dependencias: Poetry.


Instalación:
```bash

make install

Uso en terminal:
Escribir comando en la terminal: poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

Uso como biblioteca:
Puedes importar la función `generate_diff` en tus propios scripts de Python:
from gendiff import generate_diff

Luego donde se requiera llamar la funcion se realiza asi:
diff = generate_diff('file1.json', 'file2.json')
print(diff)

Demostración inical:
https://drive.google.com/file/d/1wbQXbhQONUZuyY8WgVOaxV6F-PtVQ7_y/view?usp=drive_link


Para verificar el estilo puedes usar: make lint
Y para verificar pruebas unitarias: make test

Para que el proyecto funcione se deben automatizar las pruebas manualmente, para esto usaremos pytest.

Para que este comando funciones primero se debe instalar Pytest si aun no lo tienes instalado, para ello ejecuta este comando:
poetry add --group dev pytest

Luego y como paso A: Crear el archivo de los tests(pytest):
Primero creamos una carpeta llamada tests en la raiz del proyecto, luego de esto en esa carpeta creamos un archivo llamado test_generate_diff.py.

Siguiente y como paso B: Se crea el código de los test:
Este código comparará la salida de la funcón con un resultado esperado que se guardara en un archivo de texto.

Por último y como paso C: Ejecutar los tests:
Una vez que se crea el archivo, se ejecutara este comando en la terminal "poetry run pytest" si todo esta bien establecido y sin errores se vera un mensaje en color verde, el cual dira que los 3 test pasaron. ("3 Passed").

Demostración múltiformato:
https://drive.google.com/file/d/1C1z4Yq54USs8genzcpzaqhlbut2uD0DD/view?usp=drive_link


PLAIN:
Esta herramienta también es compatible con una salida de texto sin formato para facilitar la lectura de diferencias complejas. Utilicé la bandera "--format plain" para ver los cambios de propiedad como oraciones descriptivas.
ejm: poetry run --format plain tests/fixtures/file1.json tests/fixtures/file2.json

Demostración:
https://drive.google.com/file/d/183wpC8oiNkS8iPevMyLG08W4tAHpEanp/view?usp=drive_link


Formato JSON
Para casos en los que se necesite procesar los datos de las direnecias con otras aplicaciones o scripts, el proyecto permmite exportar el resultado directamente en formato **JSON**. Este formato devuelve una representación técnica y estructurada del árbol de diferencias.
Para su uso se puede escribir el siguiente comando en la termianl:
poetry run gendiff --format json tests/fixtures/file1.json tests/fixtures/file2.json

Demostarcion JSON:
https://drive.google.com/file/d/1Ol2_TKKeqG99dC4aRETQ10fJ_ruC3_j7/view?usp=drive_link

