### Hexlet tests and linter status:
[![Actions Status](https://github.com/Bam-Manu-182/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Bam-Manu-182/python-project-174/actions)


Gendiff (Difference Calculator):
Herramienta para comprar dos archivos de configuración y mostrar sus diferencias.

Instalación:
'''bash
make install

Uso en terminal:
Escribir comando en la terminal: poetry run gendiff file1.json file2.json

Uso como biblioteca:
Escribir en archivo el comando de importe:
from gendiff import generate_diff
Luego donde se requiera llamar la funcion se realiza asi:
diff = generate_diff('file1.json', 'file2.json')
print(diff)

Demostracion:
https://drive.google.com/file/d/1wbQXbhQONUZuyY8WgVOaxV6F-PtVQ7_y/view?usp=drive_link

