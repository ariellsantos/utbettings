from .models import Equipo, Liga, Evento, Torneo

def generar_juegos_temporada(liga):
    equipos = Equipo.objects.filter(liga=liga)

    equipos_id = []
    for equipo in equipos:
        equipos_id.append(equipo.id)
    

    s = []

    if len(equipos_id) % 2 == 1: 
        equipos_id = equipos_id + ["LIBRE"]
    
    for i in range(len(equipos_id)-1):
        mid = int(len(equipos_id) / 2)
        l1 = equipos_id[:mid]
        l2 = equipos_id[mid:]
        l2.reverse()

        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]

        equipos_id.insert(1, equipos_id.pop())
    return s

def crear_rol(liga, torneo):
    semana = 0
    liga = Liga.objects.get(pk=liga)
    torneo = Torneo.objects.get(pk=torneo)
    for jornada in generar_juegos_temporada(liga):
        semana = semana + 1

        for juego in jornada:
            evento = Evento()
            evento.torneo = torneo
            evento.jornada = semana
            evento.equipo_local_id = juego[0]
            evento.equipo_visitante_id = juego[1]
            evento.save()
    
    torneo.rol = True


