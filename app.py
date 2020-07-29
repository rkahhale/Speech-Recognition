from flask import Flask, render_template, request, redirect
import speech_recognition as sr
 
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECIEVED!")
 
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        # handeling uploading a blank file
        if file.filename == "":
            return redirect(request.url)
        
        # take the file that the user uploaded and create and audioFile object 
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)

            # Read the file through the recognizer 
            with audioFile as source:
                audio = recognizer.record(source, duration=120) 

            transcript = recognizer.recognize_google(audio, key=None)
        
    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)