from django.shortcuts import render

from gtts import gTTS


def home(request):
    if request.method == 'POST':
        data = request.POST['data']
        lan = request.POST['lan']
        speed = request.POST['speed']

        mytext = data
        language = lan
        myobj = gTTS(text=mytext, lang=language, slow=speed, tld='co.in')
        myobj.save("media/music/result.mp3")



        return render(request, "voice.html")

    return render(request, "index.html")











