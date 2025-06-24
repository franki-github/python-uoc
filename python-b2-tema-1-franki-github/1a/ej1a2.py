"""
Enunciado:
Desarrolla un conjunto de funciones para gestionar eventos en diferentes zonas horarias, facilitando la creación,
manipulación y consulta de eventos programados utilizando Python, con especial énfasis en el manejo de fechas, horas y
zonas horarias mediante datetime y pytz.

Funciones a desarrollar:
- `create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Crea un diccionario representando un evento, incluyendo su nombre, fecha y hora de inicio, y zona horaria.
    Parámetros:
        - `name` (str): Nombre del evento.
        - `datetime_start` (datetime): Fecha y hora de inicio del evento.
        - `timezone_str` (str): Identificador de la zona horaria del evento.

- `time_until_event(event: Dict[str, str]) -> timedelta`:
    Descripción:
    Calcula el tiempo restante hasta el inicio de un evento dado.
    Parámetros:
        - `event` (Dict[str, str]): Evento para calcular el tiempo restante.

- `change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Cambia la zona horaria de un evento existente a una nueva especificada.
    Parámetros:
        - `event` (Dict[str, str]): Evento a modificar.
        - `new_timezone_str` (str): Nueva zona horaria.

- `find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]`:
    Descripción:
    Identifica el próximo evento entre una lista de eventos, considerando la fecha y hora actual.
    Parámetros:
        - `events` (List[Dict[str, str]]): Lista de eventos entre los cuales buscar el próximo evento.

Ejemplo:

    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    
    time_to_event = time_until_event(event)
    print(f"Time until '{event['name']}':", time_to_event)

    changed_event1 = change_event_timezone(event1, "America/New_York")
    print(f"Event after timezone change: {changed_event1}")

    next_event = find_next_event(events)
    print("\nThe next event is:", next_event["name"])

Salida esperada:
- Crear eventos con sus respectivas zonas horarias.
     {'name': 'Global Meeting', 'datetime_start': datetime.datetime(2024, 9, 10, 10, 0), 'timezone': 'UTC'}

- Mostrar el tiempo restante hasta el inicio de cada uno de los eventos.
    "Time until 'Global Meeting': 1 day, 20:00:00"

- Cambiar dinámicamente la zona horaria de un evento.
    "Event after timezone change: {'name': 'Global Meeting', 'datetime_start': datetime.datetime(2024, 9, 10, 6, 0,
        tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>), 'timezone': 'America/New_York'}"

- Calcular cuál será el siguiente evento.
    "The next event is: Global Meeting"
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pytz


def create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]:
    # Write here your code

    # Aseguramos que datetime_start sea un objeto datetime con la zona horaria correcta
    tz = pytz.timezone(timezone_str)
    
    # creamos un objeto datetime con la zona horaria especificada
    dt_with_tz = tz.localize(datetime_start)

    event = {
        'name': name,
        'datetime_start': dt_with_tz.isoformat(),  # ejemplo: '2024-09-10T10:00:00+02:00'
        'timezone': timezone_str
    }
    return event

    pass


def time_until_event(event: Dict[str, str]) -> timedelta:
    # Write here your code
    event_time = datetime.fromisoformat(event['datetime_start'])
    current_time = datetime.now(pytz.timezone(event['timezone']))
    time_difference = event_time - current_time
    if time_difference < timedelta(0):
        return timedelta(0)  # Si el evento ya ha pasado, devolvemos 0
    return time_difference
    pass


def change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]:
    # Write here your code
    old_tz = pytz.timezone(event['timezone'])
    new_tz = pytz.timezone(new_timezone_str)
    event_time = datetime.fromisoformat(event['datetime_start']).astimezone(old_tz)
    new_event_time = event_time.astimezone(new_tz)
    event['datetime_start'] = new_event_time.isoformat()
    event['timezone'] = new_timezone_str
    return event
    pass


def find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    # Write here your code
    current_time = datetime.now(pytz.utc)
    future_events = [event for event in events if datetime.fromisoformat(event['datetime_start']) > current_time]
    if not future_events:
        return None
    next_event = min(future_events, key=lambda e: datetime.fromisoformat(e['datetime_start']))
    return next_event

    pass


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    event2 = create_event("Python Talk", datetime(2024, 9, 10, 18, 30), "America/New_York")
    event3 = create_event("Data Science Workshop", datetime(2029, 9, 10, 12, 0), "Europe/London")

    for event in [event1, event2, event3]:
        time_to_event = time_until_event(event)
        print(f"Time until '{event['name']}':", time_to_event)

    changed_event1 = change_event_timezone(event1, "America/New_York")
    print(f"Event after timezone change: {changed_event1}")

    events = [event1, event2, event3]
    next_event = find_next_event(events)
    if next_event:
        print("\nThe next event is:", next_event["name"])
    else:
        print("There are no future events.")
