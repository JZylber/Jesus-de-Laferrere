from rollinga import Rollinga

def test_creación_rollinga():
    r = Rollinga("Juan")
    assert r.nombre == "Juan"
    assert r.flequillo == True
    assert r.birras == 0
    assert r.panchos == 0
    assert r.felicidad == 0

def test_tomar_birra_menor():
    r = Rollinga("Pedro")
    r.birras = 3
    r.tomar_birra(2)
    assert r.birras == 1
    assert r.felicidad == 2

def test_tomar_birra_igual():
    r = Rollinga("Luis")
    r.birras = 2
    r.tomar_birra(2)
    assert r.birras == 0
    assert r.felicidad == 2

def test_tomar_birra_mayor():
    r = Rollinga("Carlos")
    r.birras = 2
    r.tomar_birra(3)
    assert r.birras == 0
    assert r.felicidad == 2

def test_tomar_birra_sin_flequillo():
    r = Rollinga("Ana")
    r.birras = 5
    r.corta_flequillo()
    r.tomar_birra(3)
    assert r.birras == 5
    assert r.felicidad == 0

def test_comer_pancho_menor():
    r = Rollinga("Pedro")
    r.panchos = 3
    r.comer_pancho(2)
    assert r.panchos == 1
    assert r.felicidad == 4

def test_comer_pancho_igual():
    r = Rollinga("Luis")
    r.panchos = 2
    r.comer_pancho(2)
    assert r.panchos == 0
    assert r.felicidad == 4

def test_comer_pancho_mayor():
    r = Rollinga("Carlos")
    r.panchos = 2
    r.comer_pancho(3)
    assert r.panchos == 0
    assert r.felicidad == 4

def test_comer_pancho_sin_flequillo():
    r = Rollinga("Ana")
    r.panchos = 5
    r.corta_flequillo()
    r.comer_pancho(3)
    assert r.panchos == 5
    assert r.felicidad == 0

def test_cortar_flequillo():
    r = Rollinga("Marta")
    r.corta_flequillo()
    assert not r.flequillo

def test_crecer_flequillo():
    r = Rollinga("Sofia")
    r.corta_flequillo()
    r.crece_flequillo()
    assert r.flequillo

