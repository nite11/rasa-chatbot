Movie Suggestion Chatbot

## Project Description
This simple terminal-based Rasa chatbot application fetches top 5 movie titles from IMDb based on user inputs. It asks the user 4 things (rasa slots): user's name, movie release year from, movie release year to and minimum movie rating. Based on these inputs it makes an HTTP request to IMDb.com to get a list of top 5 movies. The chatbot is not very intelligent and thus, cannot handle many logical and spelling errors. So the chatbot prompts have to be followed. However, a restart option has been provided to restart the conversation with the chatbot.

## Prerequisites
- Python 3.8.10
- Rasa 3.1

## Installation
1.  Clone the repository:
        git clone [Repository URL]
2.  Navigate to the project directory:
        cd [project-directory]
3.  Create a virtual environment:
        python -m venv venv
4.  Activate the virtual environment:
        source venv/bin/activate
5.  Install the required packages:
        pip install -r requirements.txt

## Basic Usage
1.  Create a new project:
       rasa init
2.  Make sure you still have the YAML and Python files from the MyGit repository. 
        If not pull them again.    
3.  Train a model using your NLU data and stories:
        rasa train
4.  Start an action server using the Rasa SDK:
        rasa run actions
5.  Load your trained model and talk to the chatbot on the command line:
        rasa shell
6.  Greet the chatbot (hi, hello, etc) to start the session and follow the prompts.

## Implementation of the Requests
### imdb.py
- fetch_movie_names
    Based on the arguments makes an HTTP request to imdb.com to get a list of movies

### actions.py
- action_session_start
    To start a new session with a custom message
- action_set_olduser
    To set the new_user flag and ask the user whether they want movie suggestions.
- action_check_ustatus
    To check whether it is a new user or the same user, and continue the conversation accordingly.
- action_set_fname
    To extract the name of the user from text (type: from_text, intent: name_entry). And ask the user to confirm the name.
- action_fetch_imdb
    Fetch the name of movies, and ask whether the user is happy with the result.

### domain.yml
Used 3 entities:
- user_rating
- year_to
- year_from
and 5 slots:
-    new_user
-    fname
-    year_from
-    year_to
-    user_rating
### rules.yml
used 2 rules:
- rule: extract name from name entry
- rule: reset conversation after restart
  