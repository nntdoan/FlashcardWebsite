"""
Created on Fri Jan 11 18:13:50 2019
@author: @Creoco & @thediligentcow
"""
from flask import Flask, render_template, request, redirect, flash, url_for, session
from random import choice
import json
import os


# SUPPORT PART
###################################################################
def filter_file(files_list, key_words='studyset_', extension='.txt', erase_key_word=True):
    """ :param files_list: a list of file names
    :param key_words: exact keyword to match for
    :param extension: filename extension, default set to be .txt
    :param erase_key_word: delete key_word in results showed if True
    :return the filtered list, empty list if there is no file satisfies key_words and extension"""

    # Copy file_name into list files_list_updated if both key words and extension appear in file name
    files_list_updated = [file_name for file_name in files_list if (key_words in file_name) and (extension in file_name)]

    # Erase the .extension in file name for better visually-display
    result_x0 = [file_name.replace(extension, '') for file_name in files_list_updated]

    if erase_key_word:
        # Erase the suffix_ in file name for better visually-display
        result_x1 = [file_name.replace(key_words, '') for file_name in result_x0]
    else:
        result_x1 = result_x0[:]
    # Reference: https://stackoverflow.com/questions/3136689/find-and-replace-string-values-in-python-list
    # https://stackoverflow.com/questions/13779526/finding-a-substring-within-a-list-in-python

    return result_x1


def has_illegal_char(t):
    """:param t: title name
    :return Illegal characters in directory name"""
    illegal_char = '<>:"/\|?*'
    for char in illegal_char:
        if char in t:
            return True
    return False
###################################################################

# MAIN APP
###################################################################


app_flaskweb = Flask(__name__)
app_flaskweb.secret_key = b'D;d>SWA>f)V?4$;$'


@app_flaskweb.route('/', methods=['GET', 'POST'])
def to_welcome_page():
    """:return welcome page as default when no specific suffix stated"""
    return redirect(url_for('welcome_flaskweb'))


@app_flaskweb.route('/welcome_flaskweb', methods=['GET', 'POST'])
def welcome_flaskweb():
    # Create a randomly-chosen quote will appear on the welcome page
    list_quotes = []
    with open('quotes_flaskweb.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            list_quotes.append(line)
        quote_of_the_day = choice(list_quotes)

    return render_template('welcome_flaskweb.html', quote_of_the_day=quote_of_the_day)


@app_flaskweb.route('/create_set_flaskweb', methods=['GET', 'POST'])
def create_set_flaskweb():
    app_flaskweb_dict = {}
    defit_list = []
    term_list = []
    error = None
    files_list = os.listdir(os.getcwd())
    set_list = filter_file(files_list, key_words='studyset_', extension='.txt')

    if request.method == 'GET':
        return render_template('create_set_flaskweb.html')
    else:
        for i in range(1, 6):
            term = request.form['term%d'%i]
            defit = request.form['def%d'%i]
            if term and defit is not '':  # Ignore empty string for further usage of this dict in further process
                app_flaskweb_dict[defit] = term  # Study later: show definition, ask for term since term is shorter
            if term is not '':
                defit_list.append(term)
            if defit is not '':
                term_list.append(defit)

        # Ensure that users have filled in Title
        if (request.form['title'] == '') or (request.form['title'] == '.'):
            error = 'Fill in Title'

        # Ensure that (title) does not contain illegal character for directory name in Window/Linux
        elif has_illegal_char(request.form['title']):
            error = 'These character: <>:"/\|?* are not allowed in Title'

        # Ensure users choose title has not existed to prevent overwrite file in the rooting library
        elif request.form['title'] in set_list:
            error = 'Title already exist. Choose another title.'

        # Ensure that users have filled in at least one couple of term and definition
        elif not app_flaskweb_dict:  # empty dictionary return False Boolean value
            error = 'Each couple of Term and Definition must be complete. There must be at least one couple'

        # Terms and Definitions are unique, avoid overwriting when using key-value in dict
        elif (len(defit_list) != len(set(defit_list))) or (len(term_list) != len(set(term_list))):
            error = 'Repeated definitions or terms detected'

        else:
            # Save the study set in a .txt file for further process
            with open(f'studyset_{request.form["title"]}.txt', 'w') as study_set:
                json.dump(app_flaskweb_dict, study_set)

            # Inform user that the study set has been created, then redirect to welcome page
            flash('Study set %s was successfully created!' % request.form['title'])
            return redirect(url_for('welcome_flaskweb'))
    return render_template('create_set_flaskweb.html', error=error)


@app_flaskweb.route('/sets_list_flaskweb', methods=['GET', 'POST'])
def sets_list_flaskweb():
    files_list = os.listdir(os.getcwd())
    if request.method == 'GET':
        set_list = filter_file(files_list, key_words='studyset_', extension='.txt')
        return render_template('sets_list_flaskweb.html', set_list=set_list)
    else:
        set_list = filter_file(files_list, key_words='studyset_', extension='.txt')
        search_result = filter_file(set_list, key_words=str(request.form['key_word']), extension='', erase_key_word=False)
        flash('Search result: %d' % len(search_result))
        return render_template('sets_list_flaskweb.html', search_result=search_result, set_list=set_list)


@app_flaskweb.route('/study_set_flaskweb/<title>', methods=['GET', 'POST'])
def study_set_flaskweb(title=None):
    count = session.get('count', 0)
    with open(f'studyset_{title}.txt') as f:
        definitions = json.load(f)
        definition_flaskweb = definitions.items()
    if request.method == 'GET':
        return render_template('study_set_flaskweb.html', definition_flaskweb=definition_flaskweb, num=count + 1)
    elif request.method == 'POST':
        correct = []
        incorrect = []
        for a, b in definitions.items():
            if request.form.get(f'{a}_answer', '') == b:
                correct.append(f'{a}')
            else:
                incorrect.append(f'{a}')
        correct_format = ', '.join(correct)
        incorrect_format = ', '.join(incorrect)
        already_correct = dict()
        retry = dict()
        for a, b in definitions.items():
            if a in incorrect:
                retry[a] = b
            if a in correct:
                already_correct[a] = b
        flash(f'The following questions were incorrect: {incorrect_format}')
        if len(incorrect) == 0:
            # session reset if and only if user complete studying a set; not reset even with interruption
            # in the middle of studying - not allow cheating!!
            session.clear()
            return render_template('results_flaskweb.htm', correct=already_correct.items(), incorrect=retry.items(), num=count + 1)
        session['count'] = count + 1
        return render_template('study_set_flaskweb_retry.html', correct=already_correct.items(), incorrect=retry.items(), num=count + 2)


if __name__ == "__main__":
    app_flaskweb.run(debug=True)
