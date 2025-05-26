from collections import deque

# Ejemplo de cola de notificaciones
notificaciones = deque([
    {'hora': '10:00', 'aplicacion': 'WhatsApp', 'mensaje': 'Hola!'},
    {'hora': '12:00', 'aplicacion': 'Facebook', 'mensaje': 'Nuevo mensaje'},
    {'hora': '12:30', 'aplicacion': 'Twitter', 'mensaje': 'Python rocks!'},
    {'hora': '14:00', 'aplicacion': 'Twitter', 'mensaje': 'Aprendiendo Java'},
    {'hora': '16:00', 'aplicacion': 'Facebook', 'mensaje': 'Revisa tus recuerdos'},
    {'hora': '13:00', 'aplicacion': 'Twitter', 'mensaje': 'Python para todos'},
])

# a. Eliminar todas las notificaciones de Facebook
def eliminar_facebook(cola):
    nueva_cola = deque()
    while cola:
        notif = cola.popleft()
        if notif['aplicacion'] != 'Facebook':
            nueva_cola.append(notif)
    return nueva_cola

# b. Mostrar notificaciones de Twitter cuyo mensaje incluye 'Python', sin perder datos
def mostrar_twitter_python(cola):
    print("Notificaciones de Twitter con 'Python':")
    for notif in cola:
        if notif['aplicacion'] == 'Twitter' and 'Python' in notif['mensaje']:
            print(notif)

# c. Usar una pila para las notificaciones en el rango de hora
def notificaciones_en_intervalo(cola, hora_inicio='11:43', hora_fin='15:57'):
    pila = []
    for notif in cola:
        if hora_inicio <= notif['hora'] <= hora_fin:
            pila.append(notif)
    print(f"Cantidad de notificaciones entre {hora_inicio} y {hora_fin}: {len(pila)}")
    return pila

# Proceso completo
print("Cola original:")
for n in notificaciones:
    print(n)

# a)
notificaciones = eliminar_facebook(notificaciones)

print("\nCola después de eliminar Facebook:")
for n in notificaciones:
    print(n)

# b)
mostrar_twitter_python(notificaciones)

# c)
pila = notificaciones_en_intervalo(notificaciones)
