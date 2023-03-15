def what_time(sec):
    import datetime
    hours = sec // 3600
    minutes = (sec - hours*3600) // 60
    seconds = sec - hours*3600 - minutes*60
    if sec < 3600:
        hours = 0
    if sec < 60:
        minutes = 0
    result_time = datetime.time(hours, minutes, seconds)
    return f"Введенное время: {result_time}"


user_seconds = int(input("Введите время в секундах: "))
print(what_time(user_seconds))
