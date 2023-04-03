import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from random import randint

root = ttk.Window(themename="cyborg")
root.title("Voice Bot")

lbl_heading = ttk.Label(root, text="Voice Changer", font=('Lato',15), bootstyle="info")
lbl_heading.grid(row=0, column=0, padx=50, columnspan=2, pady=(80,50))

voices_list = ["Justin", "Jarvis", "Friday"]
current_voice = ttk.StringVar(value="Justin")
cbo_voice = ttk.Combobox(root, textvariable=current_voice, values=voices_list, width=20, bootstyle="info")
cbo_voice.grid(row=1, column=0, columnspan=2, padx=(25,60), pady=(10,30))

mtr_speed = ttk.Meter(metersize=230, padding=5, amountused=50, metertype="semi", subtext="Speed", interactive=True, bootstyle="primary")
mtr_pitch = ttk.Meter(metersize=230, padding=5, amountused=75, metertype="semi", subtext="Pitch", interactive=True, bootstyle="warning")

mtr_speed.grid(row=2, column=0, padx=(60,25))
mtr_pitch.grid(row=2, column=1, padx=(25,60))

lbl_volume = ttk.Label(root, text="Volume", font=('Lato',10), bootstyle="info")
lbl_volume.grid(row=3, column=0, padx=50, columnspan=2)

volume = ttk.IntVar(value=50)
scl_volume = ttk.Scale(root, orient=HORIZONTAL, variable=volume, length=800, from_=0, to=100, bootstyle="info")
scl_volume.grid(row=4, column=0, columnspan=2, pady=(10,50))

mtr_voice = ttk.Meter(metersize=150, padding=5, amountused=0, metertype="semi", subtext="Voice", interactive=True, bootstyle="success")
mtr_voice.grid(row=5, column=0, padx=(25,60))

ent_text = ttk.Text(root, width=35, height=6)
ent_text.grid(row=5, column=1, padx=(0,100), pady=(0,0))


def speakBtnCommand():
    pass

def startBtnCommand():
    pass

BTN_WIDTH = 30
btn_listen = ttk.Button(root, text="Start", command=startBtnCommand, width=BTN_WIDTH, bootstyle="primary")
btn_listen.grid(row=6, column=0, pady=(0,100), ipady=10)

btn_speak = ttk.Button(root, text="Read", command=speakBtnCommand, width=BTN_WIDTH, bootstyle="warning")
btn_speak.grid(row=6, column=1, padx=(0,100), pady=(0,100), ipady=10)


def getSpeedLevel():
    return mtr_speed.amountusedvar.get()

def getPitchLevel():
    return mtr_pitch.amountusedvar.get()

def getVoiceLevel():
    return mtr_voice.amountusedvar.get()

def setVoiceLevel(speed):
    mtr_voice.configure(amountused = speed)

def getVoiceName():
    return current_voice.get()

def getVolumeLevel():
    return volume.get()

def getText():
    return ent_text.get('1.0', END)

def clearText():
    ent_text.delete('1.0', END)

def setRandomVoiceLevel():
    voice_level = getVoiceLevel() + randint(-5,5)
    if voice_level < 0:
        voice_level = 0
    elif voice_level > 100:
        voice_level = 100
    setVoiceLevel(voice_level)

def task():
    # print(getSpeedLevel())
    # print(getPitchLevel())
    # print(getVolumeLevel())
    # print(getText())
    # print(getVoiceName())
    setRandomVoiceLevel()

    root.after(200, task)  # run task function every 200 miliscecs
root.after(200, task)
root.mainloop()