# FaceCheckIn

## Pasos para trabajar en el repositorio:

## 1. Instalaciones necesarias

Antes de comenzar a trabajar en el proyecto, hay 2 instalaciones necesarias: Python para poder ejecutar la aplicación y Git para poder guardar cualquier cambio realizado en GitHub

Para verificar si ya los tienes instalados en tu equipo, desde la terminal ejecuta los siguientes comandos:

```
pip --version
git --version
```
Si te da una respuesta positiva, no necesitas instalar nada, caso contrario hay que descargarlos para poder trabajar en el proyecto.

Por último, debemos instalar una líbreria de Python que es virtualenv, esta nos ayudara a crear un entorno virtual para nuestro proyecto donde estarán todas nuestras dependencias. Para instalarlo ejecutamos:
```
pip install virtualenv
```
La ventaja de trabajar en entornos virtuales con Python es que las librerias o dependencias que instalemos para el proyecto, solo estaran disponibles en ese entorno y no de forma global en nuestra computadora, lo cual es muy bueno para que no tengamos conflictos con librerias de otros proyectos.

## 2. Clonar repositorio
Despues de verificar que tenemos las instalaciones requeridas, lo que haremos sera clonar el repositorio. Para esto abre la terminar y muevete hacia el escritorio:
```
cd .\Desktop\
```
Estando en el escritorio, clonaremos el repositorio:
```
https://github.com/RogelioCR311/facecheckin.git
```
Una vez termine de clonarse el repositorio nos moveremos hacia la carpeta que se nos creo, y la abriremos con Visual Studio Code:
```
cd .\facecheckin\
code .
```

## 3. Instalación de dependencias
En el proyecto podemos encontrar un archivo llamado "requirements.txt" este archivo contiene un listado de todas las dependencias que se necesitan para ejecutar el proyecto.

Para instalar las dependencias ejecuta el siguiente comando:
```
pip install -r requirements.txt
```

Si mientras trabajas en el proyecto instalaste una nueva dependencia, necesitas actualizar el archivo. Para esto ejecuta:
```
pip freeze > requirements.txt
```

## 4. Ejecución del proyecto
Para ejecutar el proyecto ejecutamos el comando:
```
python main.py
```

Después de ejecutar el comando, se abrirá la pantalla de nuestra app

## 5. Descargar los cambios más recientes en el proyecto
Antes de que vayas a realizar cualquier cambio en el proyecto, primero verifica que no haya cambios recientes. Para obtener los ultimos cambios en el repositorio de GitHub ejecuta el siguiente comando:
```
git pull
```

## 6. Subir cambios al repositorio de GitHub
Si quieres actualizar el repositorio de GitHub después de realizar cambios en el proyecto, ejecuta los siguientes comandos:
```
git add .
git commit -m "Descripcion de los cambios realizados"
git branch -M main
git push -u origin main
```
