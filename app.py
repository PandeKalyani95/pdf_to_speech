from flask import Flask, render_template, request, redirect
#import speech_recognition as sr
import PyPDF2
import pyttsx3

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    text = ""
    # if request.method is "POST" so i know that my from
    # has been submitted with some data
    if request.method == "POST":
        print("from data received")

        # first thing i need to make sure that my file even exits
        # what is someone pings my website with a post request#
        # with no file information whatsoever
        if "file" not in request.files:
            return redirect(request.url)

        # what is someone submits a blank file
        file = request.files["file"]

        #print("File Name:- ",filename)
        #print("file type:- ",type(file))
        if file.filename == "":     # if file is empty then return to home page
            return redirect(request.url)

        if file:
               pdfReader = PyPDF2.PdfFileReader(file)
               print(" No. Of Pages :", pdfReader.numPages)
               for num in range(pdfReader.numPages):
                   pageObject = pdfReader.getPage(num)
                   text = pageObject.extractText()
                   # player = pyttsx3.init()
                   # play = player.say(text)
                   #palyer.runAndWait()
               #print(text)
               #pdfFileObject.close()
    return render_template('index.html', Totext = text )

if __name__ == "__main__":
    app.run(debug = True)