# Jesús de Laferrere

## Introducción
Para entender el contexto del ejercicio, pueden mirar el siguiente video: [https://www.youtube.com/watch?v=05Iw0zqeSmM](https://www.youtube.com/watch?v=05Iw0zqeSmM)

## Consigna
Hacer una clase y un conjunto de tests de dicha clase.

### Rollinga
Crear una clase `Rollinga` (en el archivo `rollinga.py`) que:
- Se inicialice con un nombre pasado por parámetro, 0 de felicidad, 0 de birras, 0 de panchos, no tiene papas y tiene flequillo
- Tenga un método `tomar_birras` que toma un parámetro (cantidad de birras) y cosuma esa cantidad de birras. Si el rollinga quiere consumir más birras de las que tiene, consume todas las que tenga. Aumenta en 1 su felicidad por birra consumida.
- Tenga un método `comer_pancho` que no tome parámetros, y, si el rollinga tiene al menos un pancho, lo consuma y aumente en 1 su felicidad. Si además tenía papas, aumenta en 2 su felicidad, pero deja de tener papas.
- Si el rollinga no tiene flequillo, no puede ni tomar birras ni comer panchos porque la vida dejó de tener sentido

### Jesús

A Jesús le interesa evaluar que sus discípulos rollingas se comporten correctamente. Para eso, va a armar un **conjunto de tests usando `pytest`**. Tener en cuenta casos con y sin flequillo, con o sin papas, una o múltiples birras, que desee más birras de las que tiene, uno o múltiples panchos y las combinaciones de estos casos.

### Ejemplo

Si creo 4 rollingas:
1. Con 2 birras
2. Con 3 birras, dos panchos y sin flequillo
3. Con 2 panchos
4. Con 2 panchos y papas

Todos comen un pancho. Luego, reponerle el flequillo al rollinga 2. Hacer que todos tomen sus birras, y vuelvan a comer un pancho. La felicidad debería quedar:
1. 2
2. 4 (el primer pancho no lo come al no tener flequillo)
3. 2
4. 3 (el primer pancho lo come con papas, el segundo no)
