# A Study Website created with Flask

Basic Programming Project <br />
Authors: @creoco & @thediligentcow <br />
Cognitive Science and Artificial Intelligence, Class of 2021, Tilburg University <br />
Instructors: Dr. F. Hermens and E. van Miltenburg <br />

Special thanks to our friend Geoffrey Westhoff for his guidance in creating the study part for this website; Khoa Phan for his suggestion of using Flask in the first place; the team behind Quizlet: Learning tools & flashcards for creating such an amazing website that have saved us in our final exams, which in turn inspired us to start this project; and @bev-a-tron for creating such a doable tutorial to begin exploring Flask - the style for this app is mostly adapted from her style_lulu.css as our main purpose was to explore the module Flask and HTML. <br />

## INTRODUCTION
This app creates a website that allow users to creating study sets made up of terms and their definition (maximum 5 at a time), save these into a file with the file name is corresponding to the set's title. It keeps track of already-created study sets in the library root and allow users to load it back online to study them. For each study set, in the study process, the app shows the definitions and ask the users to give the matching terms until everything is correct - the number of trials will be shown in the result page. <br />

![Website_interface](images/interface.png)

Site-map: *in-progress* <br />

## REQUIREMENTS
Python version: 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) <br />
Other required libraries are specified in requirements.txt, which can be installed by: <br />
```
pip install -r requirements.txt
```
An appropriate virtual environment need configuaring depending on which IDE is in use. <br />

## HOW TO USE
After download and upzip the app in your library root, ensure the directory of the Flask app look similar to this: <br />
```bash
├── _images
|   ├── interface.png
├── _static
|   ├── style_flaskweb.css
├── _templates
|   ├── create_set_flaskweb.html
|   ├── flashing_layout_flaskweb.html
|   ├── results_flaskweb.htm
|   ├── sets_list_flaskweb.html
|   ├── study_set_flaskweb.html
|   ├── study_set_flaskweb_retry.html
|   ├── welcome_flaskweb.html
├── .gitignore
├── README.md
├── application_flaskweb.py
├── quotes_flaskweb.txt
├── requirements.txt
```

Depend on what IDE you use, you may need to configurate your app intepreter accordingly, as well as a virtual environment for the app to run on. In Python 3 version, virtual environment support is included, if needed, you can run a command similar to this to create one: <br />
```
python3 -m venv venv
```
Then make sure in install all of required library. <br />

Finally, application_flaskweb.py can be openned on your IDE to run as you would normally do with any program. The app will be run from local host (http://127.0.0.1:5000/) without the trouble of deploying it to any server. <br />

## REFERENCE
Flask documentations: http://flask.pocoo.org/docs/1.0/ <br />
Jinja documentations: http://jinja.pocoo.org/docs/2.10/ <br />
HTML guidelines: https://www.w3schools.com/html/default.asp <br />
MyFlaskTutorial: https://github.com/bev-a-tron/MyFlaskTutorial <br />
Project ideas: https://quizlet.com/ <br />
Other specific sources are included in the comment part of the app's script. <br />
