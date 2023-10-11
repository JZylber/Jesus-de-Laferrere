# Jesús de Laferrere

## Introducción
Para entender el contexto del ejercicio, pueden ver el siguiente video: https://www.youtube.com/watch?v=05Iw0zqeSmM

## Consigna
Juntarse de a **DOS**. Uno de los integrantes va a ser el que haga al rollinga, y otro a Jesús de Laferrere.

### Rollinga
Crear una clase `Rollinga` (en el archivo `rollinga.py`) que:
- Se inicialice con un nombre pasado por parámetro, 0 de felicidad, 0 de birras, 0 de panchos, no tiene papas y tiene flequillo
- Tenga un método `tomar_birras` que toma un parámetro (cantidad de birras), y, si el rollinga tiene esa cantidad de birras, las consume. Aumenta en 1 su felicidad por birra consumida.
- Tenga un método `comer_pancho` que no tome parámetros, y, si el rollinga tiene al menos un pancho, lo consuma y aumente en 1 su felicidad. Si además tenía papas, aumenta en 2 su felicidad, pero deja de tener papas.
- Si el rollinga no tiene flequillo, no puede ni tomar birras ni comer panchos porque la vida dejó de tener sentido

### Jesús
Crear 4 rollingas usando la clase creada por su compañero:
1. Con 2 birras
2. Con 3 birras, dos panchos y sin flequillo
3. Con 2 panchos
4. Con 2 panchos y papas

Hacer que todos coman un pancho. Luego, reponerle el flequillo al rollinga 2. Hacer que todos tomen sus birras, y vuelvan a comer un pancho. La felicidad debería quedar:
1. 2
2. 4 (el primer pancho no lo come al no tener flequillo)
3. 2
4. 3 (el primer pancho lo come con papas, el segundo no)

Crear un programa (en el archivo `jesus.py`) que haga estas acciones y verifiquen que la felicidad es la correcta. Van a tener que coordinar con quien se encargue de hacer el rollinga para que les diga como modificar la cantidad de birras, panchos y la presencia de flequillo y papas.

Cuando cada uno termina su parte, pushear al repo y verificar que anda corriendo el archivo `jesus.py`. Si hay errores, revisen su trabajo mutuamente.
