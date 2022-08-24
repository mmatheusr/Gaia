import datetime
# 2022 8 24 11 54 30-> print(now.year, now.month, now.day, now.hour, now.minute, now.second)

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer