from tkinter import *
from tkinter.ttk import *
from gpiozero import LED
import sys
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

led = LED(21)
led1 = LED(22)
led3 = LED(23)
motor1CurrentRpm = 0
motor2CurrentRpm = 0
defaultRpmIncrementAndDecrementSpeed = 2

# create the main window of the application
# main window object named root
root = Tk()
# giving title to the main window
root.title("First Gui")


# function to validate mark entry
def only_numbers(char):
    return char.isdigit()


validation = root.register(only_numbers)

# giving title to the main window
root.title("First_Program")
root.geometry('700x450')



def change_label_text(obj, message):
    obj.config(text=message)


def set_text_input(obj, text):
    obj.delete(0, "end")
    obj.insert(0, text)


def motor_1_increase_speed(target, no):
    global motor1CurrentRpm
    motor1CurrentRpm = motor1CurrentRpm + int(no.get())
    change_label_text(target, motor1CurrentRpm)


def motor_2_increase_speed(target, no):
    global motor2CurrentRpm
    motor2CurrentRpm = motor2CurrentRpm + int(no.get())
    change_label_text(target, motor2CurrentRpm)


def motor_1_decrease_speed(target, no):
    global motor1CurrentRpm
    motor1CurrentRpm = motor1CurrentRpm - int(no.get())
    change_label_text(target, motor1CurrentRpm)


def motor_2_decrease_speed(target, no):
    global motor2CurrentRpm
    motor2CurrentRpm = motor2CurrentRpm - int(no.get())
    change_label_text(target, motor2CurrentRpm)


def toggleLED():
    led.toggle()
    if led.is_lit:
        change_label_text(motorBtn_1, "MOTOR1 OFF")
        welcome_message.value = "MOTOR1_OFF";
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor1_onoff', '0')
    else:
        change_label_text(motorBtn_1, "MOTOR1 ON")
        welcome_message.value = "MOTOR1_OFF";
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor1_onoff', '1')


def toggleLED1():
    led1.toggle()
    if led1.is_lit:
        change_label_text(motorBtn_2, "MOTOR2 OFF")
        welcome_message.value = "MOTOR2_oFF";
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor2_onoff', '0')
    else:
        change_label_text(motorBtn_2, "MOTOR2 ON")
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor2_onoff', '1')


def toggleLED2():
    led1.toggle()
    if led1.is_lit:
        change_label_text(motorBtn_3, "MOTOR1 DIR_R")
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor1_dir', '0')
    else:
        change_label_text(motorBtn_3, "MOTOR1 DIR_L")
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor1_dir', '1')


def toggleLED3():
    led1.toggle()
    if led1.is_lit:
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor_speed', '0')
    else:
        change_label_text(motor2DirectionControlButton, "MOTOR2 DIR_L")
        welcome_message.value = "MOTOR2 DIR_L";
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motor2_dir', '1')


def toggleLED4():
    led3.toggle()
    if led3.is_lit:
        change_label_text(motorSpeedControlButton, "MOTOR_SPEED_H")
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motorspeed', '0')
    else:
        change_label_text(motorSpeedControlButton, "MOTOR_SPEED_L")
        client = mqtt.Client()
        client.connect('localhost', 1883, 60)
        client.loop_start()
        print('Script is running, press Ctrl-C to quit...')
        if True:
            client.publish('motorspeed', '1')


welcome_message = Label(root, text="Welcome to my app")

motorBtn_1 = Button(root, command=toggleLED, text="MOTOR1 ON")
motorBtn_2 = Button(root, command=toggleLED1, text="MOTOR2 ON")
motorBtn_3 = Button(root, command=toggleLED2, text="MOTOR1 DIR_R")
motor2DirectionControlButton = Button(root, command=toggleLED3, text="MOTOR2 DIR_R")
motorSpeedControlButton = Button(root, command=toggleLED4, text="MOTOR_SPEED_H")
exitButton = Button(root, command=root.destroy, text="Exit")

# new
currentRpmLabel = Label(root, text="current rpm")
motor1CurrentRpmLabel = Label(root, text=motor1CurrentRpm)
motor2CurrentRpmLabel = Label(root, text=motor2CurrentRpm)
speedIncrementLabel = Label(root, text="Speed increment (rmp)")
motor1SpeedInput = Entry(root, validate="key", validatecommand=(validation, '%S'))
motor2SpeedInput = Entry(root, validate="key", validatecommand=(validation, '%S'))
motor1IncreaseSpeedBtn = Button(root, text="Increase Speed",
                                command=lambda: motor_1_increase_speed(motor1CurrentRpmLabel, motor1SpeedInput))
motor1DecreaseSpeedBtn = Button(root, text="Decrease Speed",
                                command=lambda: motor_1_decrease_speed(motor1CurrentRpmLabel, motor1SpeedInput))
motor2IncreaseSpeedBtn = Button(root, text="Increase Speed",
                                command=lambda: motor_2_increase_speed(motor2CurrentRpmLabel, motor2SpeedInput))
motor2DecreaseSpeedBtn = Button(root, text="Decrease Speed",
                                command=lambda: motor_2_decrease_speed(motor2CurrentRpmLabel, motor2SpeedInput))
# end

# setting default rpm
set_text_input(motor1SpeedInput, defaultRpmIncrementAndDecrementSpeed)
set_text_input(motor2SpeedInput, defaultRpmIncrementAndDecrementSpeed)

welcome_message.place(relx=0.35)
speedIncrementLabel.place(x=300, y=30)
currentRpmLabel.place(x=480, y=30)

# motor 1 set alignment
motor1DecreaseSpeedBtn.place(x=30, y=50)
motorBtn_1.place(x=170, y=50)
motor1SpeedInput.place(x=300, y=50)
motor1CurrentRpmLabel.place(x=480, y=50)
motor1IncreaseSpeedBtn.place(x=550, y=50)
# motor 2 set alignment
motor2DecreaseSpeedBtn.place(x=30, y=110)
motorBtn_2.place(x=170, y=110)
motor2SpeedInput.place(x=300, y=110)
motor2CurrentRpmLabel.place(x=480, y=110)
motor2IncreaseSpeedBtn.place(x=550, y=110)

motorBtn_3.place(x=170, y=170)
motor2DirectionControlButton.place(x=170, y=230)
motorSpeedControlButton.place(x=170, y=290)
exitButton.place(relx=0.45, rely=0.8)

# it tells the code to keep displaying
root.mainloop()
