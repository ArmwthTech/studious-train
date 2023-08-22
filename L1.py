#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

def format_duration(duration):
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    if duration < 60:  # до минуты
        return f"{duration} сек"
    elif duration < 3600:  # до часа
        return f"{minutes} мин {seconds} сек"
    elif duration < 86400:  # до суток
        return f"{hours} час {minutes} мин {seconds} сек"
    else:  # в остальных случаях
        return f"{days} дн {hours} час {minutes} мин {seconds} сек"
# Список продолжительностей в секундах
durations = [53, 153, 4153, 400153]

# Проверка для каждой продолжительности
for duration in durations:
    formatted_duration = format_duration(duration)
    print(f"duration = {duration}: {formatted_duration}")
