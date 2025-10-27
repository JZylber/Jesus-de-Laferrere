# Jesús de Laferrere

## Introducción

Para entender el contexto del ejercicio, pueden mirar el siguiente video: [https://www.youtube.com/watch?v=05Iw0zqeSmM](https://www.youtube.com/watch?v=05Iw0zqeSmM)

## Consigna

### Rollinga

Crear una clase (en el archivo _rollinga.py_) que:

- Se inicialice con un nombre pasado por parámetro, 0 de felicidad, 0 de birras, 0 de panchos y tiene flequillo
- Tenga un método _tomar\_birras_ que toma un parámetro (cantidad de birras) y consuma esa cantidad de birras. Si el rollinga quiere consumir más birras de las que tiene, consume todas las que tenga. Aumenta en 1 su felicidad por birra consumida.
- Tenga un método _comer\_pancho_ que toma un parámetro (cantidad de panchos) y consuma esa cantidad de panchos. Si el rollinga quiere consumir más panchos de los que tiene, consume todos los que tenga. Aumenta en 2 su felicidad por pancho consumido.
- Tenga un método _corta\_flequillo_ (sin parámetros) que corte el flequillo
- Tenga un método _crece\_flequillo_ (sin parámetros) que reponga el flequillo del rollinga.
- Si el rollinga no tiene flequillo, no puede ni tomar birras ni comer panchos porque la vida dejó de tener sentido.

Verifiquar que la implementación funciona corriendo el archivo de tests

## Consigna Manija

### Jesús

Jesús provee a sus discípulos. Para eso, hacer una clase (en el archivo _jesus.py_) que:

- Se inicialice sin discípulos
- Tenga un método _adoptar\_rollinga_ que tome como parámetro un objeto de la clase y lo adopte como discípulo.
- Tenga un método _hacer\_birras_ que le de **una** birra a cada uno de sus discípulos.
- Tenga un método _hacer\_panchos_ que le de **un** pancho a cada uno de sus discípulos.
- Tenga un método _reestablecer\_flequillos_ que recupera los flequillos de todos sus discípulos.
- Tenga un método _milagro\_rollinga_ que hace que los rollingas discípulos tomen todas las birras y coman todos los panchos que tengan.
- Tenga un método _felicidad\_total_ que devuelve la felicidad total de todos sus discípulos.

Verifiquar que la implementación funciona corriendo el archivo de tests.
