### Hexlet tests and linter status:
[![Actions Status](https://github.com/Bam-Manu-182/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Bam-Manu-182/python-project-174/actions)



Project. Difference Calc

Badge: GitHub CI
[![Python CI](https://github.com/Bam-Manu-182/python-project-174/actions/workflows/python-test.yml/badge.svg)](https://github.com/Bam-Manu-182/python-project-174/actions/workflows/python-test.yml)

Badge: Codeclimate - Maintainability
[![Maintainability](https://qlty.sh/gh/Bam-Manu-182/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/Bam-Manu-182/projects/python-project-174)


Descripción:
Este proyecto esta pensado como una herramienta para facilitar la comoparación entre dos archivos, tipo: JSON y YAML, el cual devolvera sus diferencias.

Gendiff (Difference Calculator):
Herramienta para comprar dos archivos de configuración y mostrar sus diferencias.


Instalación:
```bash
make install

Uso en terminal:
Escribir comando en la terminal: poetry run gendiff file1.json file2.json

Uso como biblioteca:
Puedes importar la función `generate_diff` en tus propios scripts de Python:
from gendiff import generate_diff

Luego donde se requiera llamar la funcion se realiza asi:
diff = generate_diff('file1.json', 'file2.json')
print(diff)

Demostración inical:
https://drive.google.com/file/d/1wbQXbhQONUZuyY8WgVOaxV6F-PtVQ7_y/view?usp=drive_link


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


Esta herramienta también es compatible con una salida de texto sin formato para facilitar la lectura de diferencias complejas. Utilicé la bandera "--format plain" para ver los cambios de propiedad como oraciones descriptivas.

Demostración:
