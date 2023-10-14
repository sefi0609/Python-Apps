import streamlit as st
import app1


def add_todo():
    new_line = st.session_state['new_todo'].title() + '\n'
    if new_line not in todos:
        todos.append(new_line)
        app1.write_to_file(todos)
    else:
        st.error('This todo is already in your list')
    st.session_state['new_todo'] = ''


st.title('My Todo App')
st.subheader(time.strftime('%B %d %Y'))
todos = app1.read_from_file()

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        app1.write_to_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=' ', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
