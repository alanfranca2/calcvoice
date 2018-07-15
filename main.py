#author: "Alan França"
#author: "Paulo Henrique"

#modules
import speech_recognition as sr
from gtts import gTTS
import os.path
import playsound
import os,shutil

#vars
scene = "home"
scene_ = 0
type_ = ""
memory = []
audio_pos = 0

folder = 'sfx/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

def falar(text):
    global audio_pos
    audio_pos = audio_pos + 1
    voz = gTTS(text, lang="pt-BR")
    voz.save(f"sfx/voz{audio_pos}.mp3")
    playsound.playsound(f'sfx/voz{audio_pos}.mp3')

r = sr.Recognizer()
with sr.Microphone() as source:
    while scene == "home":
        try:
            falar("Esperando Comando")
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            result = r.recognize_google(audio,language="pt-BR")
            print(result)
            if "somar" in result:
                scene = "somar"
                falar("Comando de Soma Selecionado")
            elif "multiplicar" in result:
                scene = "multiplicar"
            elif "dividir" in result:
                scene = "dividir"
            elif "subtrair" in result:
                scene = "subtrair"
        except:
            falar("Comando de voz não reconhecido.")
    while scene == "somar":
        try:
            if scene_ == 0:
                falar("Fale o primeiro valor para somar")
            #    r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                result = r.recognize_google(audio,language="pt-BR")
                memory.append(int(result))
                scene_ = 1
            if scene_ == 1:
                falar("Fale o segundo valor para somar")
            #    r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                result = r.recognize_google(audio,language="pt-BR")
                memory.append(int(result))
                scene = "result"
                type_ = "somar"
        except:
            falar("Comando de voz não reconhecido")
    while scene == "dividir":
        try:
            if scene_ == 0:
                falar("Fale o primeiro valor para dividir")
                #r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                result = r.recognize_google(audio,language="pt-BR")
                memory.append(int(result))
                scene_ = 1
            if scene_ == 1:
                falar("Fale o segundo valor para dividir")
                #r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                result = r.recognize_google(audio,language="pt-BR")
                memory.append(int(result))
                scene = "result"
                type_ = "dividir"
        except:
            falar("Comando de voz não reconhecido")
    while scene == "multiplicar":
        try:
            if scene_ == 0:
                falar("Fale o primeiro valor para multiplicar")
                #r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                result = r.recognize_google(audio,language="pt-BR")
                memory.append(int(result))
                scene_ = 1
            if scene_ == 1:
                falar("Fale o segundo valor para multiplicar")
        #        r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                result = r.recognize_google(audio,language="pt-BR")
                falar(f"Valor Reconhecido: {int(result)}")
                memory.append(int(result))
                scene = "result"
                type_ = "multiplicar"
        except:
            falar("Comando de voz não reconhecido")
    while scene == "subtrair":
        try:
            if scene_ == 0:
                falar("Fale o primeiro valor para subtrair")
            #    r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                memory.append(int(result))
                scene_ = 1
            if scene_ == 1:
                print("Fale o segundo valor para subtrair")
            #    r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                result = r.recognize_google(audio,language="pt-BR")
                memory.append(int(result))
                scene = "result"
                type_ = "subtrair"
        except:
            falar("Comando de voz não reconhecido")
if scene == "result":
    scene_ = 0
    if type_ == "somar":
        falar(f"O Resultado é {int(memory[0]+memory[1])}")
    elif type_ == "dividir":
        falar(f"O Resultado é {int(memory[0]/memory[1])}")
    elif type_ == "multiplicar":
        falar(f"O Resultado é {int(memory[0]*memory[1])}")
    elif type_ == "subtrair":
        falar(f"O Resultado é {int(memory[0]-memory[1])}")
