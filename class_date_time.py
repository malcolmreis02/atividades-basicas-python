from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)

    data_atual_br_1 = data_atual.strftime('%d/%m/%y')
    print(data_atual_br_1)

    data_atual_br_2 = data_atual.strftime('%A, %d/%m/%Y')
    print(data_atual_br_2)

def trabalhando_com_time():
    horario = time(hour=12, minute=10, second=30)
    print(horario)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    data_atualizada = data_atual.strftime('%A, %d/%m/%Y, %H:%M')
    print(data_atualizada)
    print(data_atual.year)

if __name__ == '__main__':
    trabalhando_com_datetime()