#simpel script uden jupyer notebook
#man kan køre filer i vs code med trekantpil symbolet i øvre højre side
#køre automatisk bash kommando til at køre det
#fra kommandline køres det manuelt med python3 script.py
#er det samme der sker i jupyter notebook i en kodecelle 
#print('Hello from script')

#.venv mappem i roden siger version af python envirponment

#han skrev deactivate i terminalen for at fjerne .venv i 
#python version: python3 --version
#pip list    -ser på moduler der er installeret

#installer requests modul
#pip install requests
#pip list viser nye mapper, viser også version. versioner ændre sig og request version brugbarhed
#afhænger af andre mappers versioner, så vi bruger virtuelt miljø så alt passer sammen
#så er det .venv virtuelt miljø der aktiveres når vi køre python, når vi har virtuelt miljø


#claus sletter .venv mappe
# python3 -m venv .venv   hender venv mappe og navngiver .venv, standard. 
# skjulte filer skal med igitignore
#når vi så bruger ovenstående kommando laves virtuelt miljø, .venv mappe i ses5 mappen kun
#det skal dog ikke ske, det skal laves i roden

#jeg skulle installere apt install python3.10-venv før den kunne gøre det og bruge sudo på alt
# så: sudo python3 -m venv .venv   -nogle skal skrive python3 andre bare python
#så blev der lavet en .venv mappe i roden af python mappen 
#godt med virtuelt miljø, fucker man noget op kan man nemt reinaallere

#source .venv/bin/activate  aktivere det
#skriv bare deactivate i terinal for at fjerne virtuelt miljø?

#når vi henter claus kode ned har vi ikke request instalerert så skal selv gøre det, men man
#laver requirements.txt fil hvor der står hvad man skal installere
#den skal hedde requirements.txt det er en standard
#copy paster hans og laver egen i ses5
#det skal vi ikke gøre hver gang det er bare for at vise hvad der sker. 

#pip install -r requirements.txt   - installere alt fra requirements, så behøver man ikke .venv?

#pip freeze > requirements.txt    -laver requirements.txt om og hvis man installerede et nyt modul
#så kommer det nye i requirements.txt. Er for den der laver programmet
# dem der har hentet programmet og skal have opdateringen bruger pip install > requirements.txt

#man kan have .venv i hvilke som helst mapper og man skal specificere hvilken man aktivere
# source .venv/bin/activate  bruger venv i mappe i den mappe man skriver denne kommando

#en gang skulle jeg rm -r .venv med sudo!

#rækkefølge efter klone nyt projekt:
# laver virtuelt miljø:
# python3 -m venv .venv   -i projekt folderen, her ses5. i ses6 og 7  får vi andre requirements
# source .venv/bin/activate    i hver .venv mappe er der en mappe bin med et activate script som
#køres her fra den projektmappe man vil køre 
# pip install -r requirements.txt
# pip install -r requirements.txt køres hver gang man skal opdatere eller hvis noget ikke virker
# altså hvis claus har opdateret/tilføjges/slettes i sin requirements.txt pga ændringer i
# sit projekt så pusher han dette og når jeg så kloner skal jeg køre requirements.txt igen
# så at jeg opdatere til hans nye moduler

# gav fejl med at den ikke hentede moduler ved pip install -r requirements.txt
# siger desuden ved mange fejlbeskeder at man skal bruge root, men det er ikke det det handler om:
# kommentar her: https://stackoverflow.com/questions/39539110/pyvenv-not-working-because-ensurepip-is-not-available
# siger at pip ofte siger brug root ved fejl som slet ikke har noget med det at gøre
# fejlen var at jeg kørte activate før requirements så at requirements blev kørt mens det
# virtuelle miljø kørte - må ikke ske åbenbart.
# pip list viser nu at requests er installeret. Giver dog stadig compilerfejl herinde

# dog på realpython how to make a webscraper guide installere de requests inde i det virtuelle
# miljø. så pip install requests. men requirements.txt SKAL køres uden for åbenbart
# nu virker kommandoerne, dog er det virtuelle miljø som køres det i roden. Den defaulter
# til dette fordi den åbenbart ikke kan køre det i undermappen. Navnet på mappen ville stå
# på linjen i terminalen før navn og $HOME mappe

#claus siger desuden at man bør køre requirements inde i det virtuelle miljø og ikke uden for
# så det virker nok kun nu fordi den bruger venv i roden 
# at ændre permission til chmod 777 til .venv1 og .venv1/bin/activate ændrede intet

# man kan gøre det samme i GUI, når man vælger kernel og python environment kan man også vælge
# hvilken requirements.txt man skal køre

import requests
import os

# fetch the html from a url
req = requests.get('https://clbokea.github.io/exam/assignment_2.html')
text = req.text

img_url_list = [] 

text_list = text.split('img')

def locate_image(e):
    i = e.find('"')

    # cut after  'src="' to end of the img_url  
    img_url = e.split('"')
    img_url = img_url[1]
    img_url_list.append(img_url)


for e in text_list:
    if 'src' in e:
        locate_image(e)

# print(img_url_list)

# Create a src directory for the images
os.mkdir('src')
os.chdir('src')

for i in img_url_list:
    # get the image
    req = requests.get(f'https://clbokea.github.io/exam/{i}', stream=True)

    # write image to file
    with open(i[4:], 'wb') as f:
        for chunk in req:
            f.write(chunk)

os.chdir('..')

with open('index.html', 'w') as f:
    f.write(text)