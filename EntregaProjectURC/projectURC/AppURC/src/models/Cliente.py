from django.db import models

from AppURC.models import poliza, Usuario

class Cliente(Usuario):
    poliza = poliza 