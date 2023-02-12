import speech_recognition as sr

#Criar um reconhecedor
r = sr.Recognizer()


#Abrir o microfone para captura
with sr.Microphone() as source:
    r.listen(source) # Define microfone como fonte de áudio
    audio = r.listen(source)

    print(r.recognize_google(audio))