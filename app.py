import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Définir le mot de passe ici
PASSWORD = "motdepasse"


@app.route('/')
def home():
    return render_template('login.html')
@app.route('/databases', methods=['POST'])
def databases():
    password = request.form['password']
    if password == PASSWORD:
        return render_template('databases.html')
    else:
        error_message = "Mot de passe incorrect, veuillez réessayer."
        return render_template('login.html', error=error_message)
@app.route('/todolist')
def todolist():
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, task FROM tasks WHERE parent_id IS NULL')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('todolist.html', tasks=tasks)
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('todolist'))
@app.route('/subtasks/<int:task_id>')
def subtasks(task_id):
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, task FROM tasks WHERE parent_id = ?', (task_id,))
    subtasks = cursor.fetchall()
    conn.close()
    return render_template('subtasks.html', subtasks=subtasks, task_id=task_id)
@app.route('/add_subtask/<int:task_id>', methods=['POST'])
def add_subtask(task_id):
    subtask = request.form['subtask']
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, parent_id) VALUES (?, ?)', (subtask, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('subtasks', task_id=task_id))
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()

    # Supprimer la tâche principale
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))

    # Supprimer toutes les sous-tâches associées
    cursor.execute('DELETE FROM tasks WHERE parent_id = ?', (task_id,))

    conn.commit()
    conn.close()
    return redirect(url_for('todolist'))

@app.route('/delete_subtask/<int:subtask_id>/<int:task_id>', methods=['POST'])
def delete_subtask(subtask_id, task_id):
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (subtask_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('subtasks', task_id=task_id))
@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    new_task_name = request.form['task_name']
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task_name, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('todolist'))


@app.route('/edit_subtask/<int:subtask_id>/<int:task_id>', methods=['POST'])
def edit_subtask(subtask_id, task_id):
    new_subtask_name = request.form['subtask_name']
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_subtask_name, subtask_id))
    conn.commit()
    conn.close()
    return redirect(url_for('subtasks', task_id=task_id))

if __name__ == '__main__':
    app.run(debug=True)

