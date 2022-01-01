# Run with https://codewith.mu

import speech
import microbit as ubit

number_phonemes = [
'Z IH1 R OW0'
'W AH N',
'T UW',
'TH R IY',
'F AO R',
'F AY V',
'S IH K S',
'S EH V AH N',
'EY T',
'N AY N',
'T EH N',
'IH L EH V AH N',
'T W EH L V',
'TH ER T IY N',
'F AO R T IY N',
'F IH F T IY N',
'S IH K S T IY N',
'S EH V AH N T IY N',
'EY T IY N',
'N AY N T IY N',
'T W EH N T IY',
'T W EH N T IY W AH N',
'T W EH N T IY T UW',
'T W EH N T IY TH R IY',
'T W EH N T IY F AO R',
'T W EH N T IY F AY V',
'T W EH N T IY S IH K S',
'T W EH N T IY S EH V AH N',
'T W EH N T IY EY T',
'T W EH N T IY N AY N',
'TH ER D IY',
'TH ER D IY W AH N',
'TH ER D IY T UW',
'TH ER D IY TH R IY',
'TH ER D IY F AO R',
'TH ER D IY F AY V',
'TH ER D IY S IH K S',
'TH ER D IY S EH V AH N',
'TH ER D IY EY T',
'TH ER D IY N AY N',
'F AO R T IY',
'F AO R T IY W AH N',
'F AO R T IY T UW',
'F AO R T IY TH R IY',
'F AO R T IY F AO R',
'F AO R T IY F AY V',
'F AO R T IY S IH K S',
'F AO R T IY S EH V AH N',
'F AO R T IY EY T',
'F IH F T IY'
]

def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

def num_to_phonemes(num):
    return number_phonemes[clamp(0, num - 1, len(number_phonemes))]

def show_temperature():
    temp = ubit.temperature()
    ubit.display.scroll(temp, delay=250, wait=False, monospace=True)
    try:
        speech.pronounce(num_to_phonemes(temp), pitch=150, speed=100)
    except:
        pass

if __name__ == "__main__":
    ubit.set_volume(255)
    show_temperature()
    last_run = ubit.running_time()

    while True:
        if ubit.button_a.is_pressed():
            show_temperature()
        if ubit.running_time() - last_run >= 5 * 60 * 1000:
            show_temperature()
            last_run = ubit.running_time()

        ubit.sleep(100)
