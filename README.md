# A Study Website created with Flask

Basic Programming Project <br />
Authors: @creoco & @thediligentcow <br />
Cognitive Science and Artificial Intelligence, Class of 2021, Tilburg University <br />
Instructors: Dr. F. Hermens and E. van Miltenburg <br />

Special thanks to our friend Geoffrey Westhoff for teaching us the ways of the jinja(2); Khoa Phan for his suggestion of using Flask in the first place; the team behind Quizlet for creating such an amazing website that has saved us in our final exams, which in turn inspired us to start this project; and @bev-a-tron for creating such a doable tutorial to begin with Flask - the style for this app is heavily adapted from her style_lulu.css. Thanks also to our classmates - Alexsandra, Codrin, Seda, Aidan and Sanna who volunteered to test our app and gave us helpful feedback, especially Codrin for letting us invade into his laptop in the middle of the night and almost destroy its operating system. <br />

## INTRODUCTION
This app creates a website that allows users to create basic study sets that are made up of terms and definitions (maximum 5 couples at a time), and stores them in the library root as separate .txt files. These files can be manipulated by using the search and study functions incorporated in the app. As for the study function, the app will load the study set of the user's choice, show them the definitions and ask them for their corresponding terms. This process will repeat until every question is correctly answered. The study results - the number of trials - will be shown in the result page. <br />

![Website_interface](images/interface.png)

## REQUIREMENTS
The app was programmed in Python version: 3.6.4 using PyCharm 3.4 as IDE <br />
Other required libraries are specified in requirements.txt, which can be installed by: <br />
```
pip install -r requirements.txt
```
An appropriate virtual environment needs to be configured depending on which IDE is in use. <br />
For some IDE, like PyCharm, a appropriate virtual environment(venv) needs to be installed in order to run the app. <br />
In python 3 the venv package is included, but in every release before Python 3.4 the user has to download the venv package first.<br />
The user can run venv in command prompt using this: <br />
```
python3 -m venv venv
```

## HOW TO USE
1. Make sure to download and upzip all of the files in your library root, ensure the directory of the Flask app look similar to this: <br />
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

2. Depending on which IDE you are using, you may need to configure your app intepreter, as well as a virtual environment as instructed above. Also make sure to install all of the required libraries. <br />

3. Open the application_flaskweb.py in your IDE to run the code as you normally would. The app will run from local host (http://127.0.0.1:5000/) without having to run a seperate server. <br />

Note for Spyder user: After testing our Flask app on several IDE, we have come to the conclusion that if you are using Spyder, the app needs to be run from command prompt. This can be done by: 
```
$ (source) {{ directory to your python.exe }} {{ directory to the application_flaskweb.py }}
```
For example:
```
$ C:\User\<name> C:\python\python.exe C:\Users\<name>\python\StudyingWeb-withFlask-master\application_flaskweb.py
```
Another solution for flask ver. 1.0.2:
"You need to edit the echo function definition at ../site-packages/click/utils.py. The default value for the file parameter must be sys.stdout instead of None. Do the same for the secho function definition at ../site-packages/click/termui.py" -josechval(https://github.com/plotly/dash/issues/257#issuecomment-391185831) <br />

If this still doesn't work, another solution is to downgrade flask to version 0.12.2
-Domanic(https://github.com/plotly/dash/issues/257#issuecomment-391187891) <br />

## REFERENCE
Flask documentations: http://flask.pocoo.org/docs/1.0/ <br />
Jinja documentations: http://jinja.pocoo.org/docs/2.10/ <br />
HTML guidelines: https://www.w3schools.com/html/default.asp <br />
MyFlaskTutorial: https://github.com/bev-a-tron/MyFlaskTutorial <br />
Project ideas: https://quizlet.com/ <br />
Other specific sources are included in the comment part of the app's script. <br />
