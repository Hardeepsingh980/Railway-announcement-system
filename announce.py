from gtts import gTTS
import os
from playsound import playsound




def main(tno, tname, from_, to, pno):

    language = 'hi'

    text = f'यात्री कृपया ध्यान दे |  गाड़ी नंबर  {tno} , {from_}  से  {to},  {tname},  प्लेटफार्म नंबर, {pno} पर खड़ी है |'

    myobj = gTTS(text=text, lang=language, slow=False)

    fileName = tname+'.mp3'

    myobj.save(f'resources/{fileName}')


    playsound('resources/starting.mp3')
    playsound(f'resources/{fileName}')
    playsound('resources/ending.mp3')

    os.remove(f'resources/{fileName}')

    

    


