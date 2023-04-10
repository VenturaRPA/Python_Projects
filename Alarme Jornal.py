import datetime
import pygame
import pywhatkit

c = 10
def display_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    print("Hora Atual: ", formatted_time)


def set_alarm():
    alarm_hour = int(input("Qual a hora do alarme: "))
    alarm_minute = int(input("Qual o minuto: "))
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
            print("ALARME! - {}".format(current_time))
            pesquisa = "icl ao vivo agora"
            pywhatkit.playonyt(pesquisa)
            while c > 0:
                pygame.mixer.init()
                pygame.mixer.music.load('C:\Windows\Media\Alarm01.wav')
                pygame.mixer.music.play()
                pygame.time.delay(5000)
            while pygame.mixer.music.get_busy():
                pass
            break
            #MUDANÇAS FUTURAS : MOSTRAR O HORARIO ATUAL DINAMICO#
while True:
    display_time()
    set_alarm()