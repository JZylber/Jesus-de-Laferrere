from jesus import Jesus
from rollinga import Rollinga

def test_nacimiento_jesus():
    jesus = Jesus()
    assert jesus.felicidad_total() == 0

def test_milagro_rollinga_sin_rollingas():
    jesus = Jesus()
    jesus.hacer_birras()
    jesus.milagro_rollinga()
    assert jesus.felicidad_total() == 0

def test_milagro_rollinga_con_un_rollinga():
    jesus = Jesus()
    rollinga = Rollinga("Juan")
    jesus.adoptar_rollinga(rollinga)
    jesus.hacer_birras()
    jesus.milagro_rollinga()
    assert jesus.felicidad_total() == 1

def test_milagro_rollinga_con_muchos_rollingas():
    jesus = Jesus()
    for i in range(5):
        rollinga = Rollinga(f"Juan_{i}")
        jesus.adoptar_rollinga(rollinga)
    jesus.hacer_birras()
    jesus.milagro_rollinga()
    assert jesus.felicidad_total() == 5

def test_milagro_rollinga_birras_y_panchos():
    jesus = Jesus()
    rollinga = Rollinga("Pedro")
    jesus.adoptar_rollinga(rollinga)
    jesus.hacer_birras()
    jesus.hacer_panchos()
    jesus.milagro_rollinga()
    assert jesus.felicidad_total() == 3  # 1 birra + 2 panchos

def test_reestablecer_flequillos():
    jesus = Jesus()
    rollinga = Rollinga("Pedro")
    jesus.adoptar_rollinga(rollinga)
    rollinga.corta_flequillo()
    jesus.reestablecer_flequillos()
    assert rollinga.flequillo == True