# Traductor
Este es un traductor del lenguaje de programación **Latino** a **JavaScript**. 
## Repositorio
[Link del repositorio en GitHub](https://github.com/nquirogac/Traductor)

## Requerimientos
Instalar  ANTlR4 para python

```
pip install -u antlr4-python3-runtime
```

Si se desea modificar el proyecto por favor diríjase al archivo en la raíz del proyecto titulado "SetUpGuide.pdf" para instalar la herramienta en su sistema.

Adicionalmente, si desea alterar la gramática del lenguaje Latino y generar los recognizers de ANTLR, deberá configurar la ubicación en donde estos se generan para que sea en la carpeta /grammar/gen.

## Uso
Para usar el traductor, se debe ejecutar el archivo `main.py` 

## Recursos
- Python 3.8
- ANTLR 4.13.1

## Estructura
En el archivo 'LatinoToJs.py' se encuentra la clase 'LatinoToJs' que contiene los métodos necesarios para traducir el código de Latino a JavaScript. Allí se sobreescriben los métodos de la clase 'LatinoGrammarListener' generada por ANTLR.

Adicionalmente el proyecto está dividido en dos carpetas: 'grammar' y 'translations'. En la carpeta 'grammar' se encuentra el archivo `LatinoGrammar.g4` que contiene la gramática del lenguaje Latino. En la carpeta 'translations' se encuentran los archivos específicos, divididos por tipos se bloque de código, que contienen las reglas de traducción.

## Alcance
En caso de que no exista una traducción directa para una regla de Latino, se especifica en un comentario el problema, esto con el fin de no detener la ejecución del programa.
