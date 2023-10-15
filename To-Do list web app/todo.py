import streamlit as st
import app1
import time

""" main site page """

def add_todo():
    """ Add a new todo itme to the list """
    new_line = st.session_state['new_todo'].title() + '\n'
    st.session_state['new_todo'] = ''
    
    if new_line not in todos:
        todos.append(new_line)
        app1.write_to_file(todos)
    else:
        app1.INDICATOR = True


st.title('My Todo App')
st.subheader(time.strftime('%B %d %Y'))
# get the todos
todos = app1.read_from_file()

# create a checkbox for each todo
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    # delete finished todos
    if checkbox:
        todos.remove(todo)
        app1.write_to_file(todos)
        del st.session_state[todo]
        st.rerun()

# input a new todo
st.text_input(label=' ', placeholder='Add new todo...', on_change=add_todo, key='new_todo')

# print an error message when the user tries to add the same task
if app1.INDICATOR:
    st.error('This todo is already in your list')
    app1.INDICATOR = False
