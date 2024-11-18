from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime, timedelta
import math

app = Flask(__name__)

DATABASE = 'database.db'
PER_PAGE = 10  # Rekordok száma oldalanként

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tools = conn.execute('SELECT * FROM tools').fetchall()
    conn.close()
    return render_template('index.html', tools=tools)

@app.route('/persons')
def persons():
    search_query = request.args.get('search', '')
    filter_by = request.args.get('filter', 'name')
    page = int(request.args.get('page', 1))
    per_page = PER_PAGE

    conn = get_db_connection()
    
    base_query = 'SELECT * FROM persons'
    params = []
    if search_query:
        if filter_by == 'name':
            base_query += ' WHERE name LIKE ?'
            params.append(f'%{search_query}%')
        elif filter_by == 'address':
            base_query += ' WHERE address LIKE ?'
            params.append(f'%{search_query}%')

    # Számoljuk ki az összes találatot
    count_query = f'SELECT COUNT(*) FROM ({base_query})'
    total = conn.execute(count_query, params).fetchone()[0]
    total_pages = math.ceil(total / per_page)

    # Alkalmazzuk a LIMIT és OFFSET klauzulákat a pagináláshoz
    paginated_query = base_query + ' ORDER BY name ASC LIMIT ? OFFSET ?'
    params.extend([per_page, (page - 1) * per_page])
    persons = conn.execute(paginated_query, params).fetchall()
    
    conn.close()
    return render_template('persons.html', 
                           persons=persons, 
                           search_query=search_query, 
                           filter_by=filter_by,
                           page=page,
                           total_pages=total_pages)

@app.route('/add_person', methods=('GET', 'POST'))
def add_person():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO persons (name, address) VALUES (?, ?)', (name, address))
        conn.commit()
        conn.close()
        return redirect(url_for('persons'))
    
    return render_template('add_person.html')

@app.route('/loan', methods=('GET', 'POST'))
def loan():
    if request.method == 'POST':
        person_id = request.form['person_id']
        tool_id = request.form['tool_id']
        loan_days = int(request.form['loan_days'])
        
        loan_date = datetime.today().strftime('%Y-%m-%d')  # Átalakítva stringgé
        return_date = (datetime.today() + timedelta(days=loan_days)).strftime('%Y-%m-%d')  # Átalakítva stringgé
        
        conn = get_db_connection()
        
        # Ellenőrizzük, hogy elérhető-e a szerszám
        tool = conn.execute('SELECT * FROM tools WHERE id = ?', (tool_id,)).fetchone()
        if tool['quantity'] < 1:
            conn.close()
            return "Nincs elegendő szerszám készleten."
        
        # Csökkentjük a készletet
        conn.execute('UPDATE tools SET quantity = quantity - 1 WHERE id = ?', (tool_id,))
        
        # Létrehozzuk a kölcsönzést
        conn.execute('INSERT INTO loans (person_id, tool_id, loan_date, return_date) VALUES (?, ?, ?, ?)',
                     (person_id, tool_id, loan_date, return_date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    persons = conn.execute('SELECT * FROM persons').fetchall()
    tools = conn.execute('SELECT * FROM tools').fetchall()
    conn.close()
    return render_template('loan.html', persons=persons, tools=tools)

@app.route('/loans')
def loans():
    sort = request.args.get('sort', 'loan_date')
    order = request.args.get('order', 'asc')
    page = int(request.args.get('page', 1))
    per_page = PER_PAGE

    valid_sort_columns = ['person_name', 'tool_name', 'loan_date', 'return_date']
    if sort not in valid_sort_columns:
        sort = 'loan_date'

    if order not in ['asc', 'desc']:
        order = 'asc'

    sort_column_mapping = {
        'person_name': 'persons.name',
        'tool_name': 'tools.name',
        'loan_date': 'loans.loan_date',
        'return_date': 'loans.return_date'
    }

    order_by = f"{sort_column_mapping[sort]} {order.upper()}"

    conn = get_db_connection()
    
    # Számoljuk ki az összes találatot
    count_query = '''
        SELECT COUNT(*) 
        FROM loans
        JOIN persons ON loans.person_id = persons.id
        JOIN tools ON loans.tool_id = tools.id
    '''
    total = conn.execute(count_query).fetchone()[0]
    total_pages = math.ceil(total / per_page)

    # Alkalmazzuk a LIMIT és OFFSET klauzulákat
    loans_query = f'''
        SELECT loans.id, persons.name AS person_name, tools.name AS tool_name, loans.loan_date, loans.return_date, tools.quantity AS tool_quantity
        FROM loans
        JOIN persons ON loans.person_id = persons.id
        JOIN tools ON loans.tool_id = tools.id
        ORDER BY {order_by}
        LIMIT ? OFFSET ?
    '''
    loans = conn.execute(loans_query, (per_page, (page - 1) * per_page)).fetchall()
    
    conn.close()
    return render_template('loans.html', 
                           loans=loans, 
                           current_sort=sort, 
                           current_order=order,
                           page=page,
                           total_pages=total_pages)

@app.route('/return/<int:loan_id>', methods=['POST'])
def return_tool(loan_id):
    conn = get_db_connection()
    loan = conn.execute('SELECT * FROM loans WHERE id = ?', (loan_id,)).fetchone()
    if loan:
        # Növeljük a szerszám készletét
        conn.execute('UPDATE tools SET quantity = quantity + 1 WHERE id = ?', (loan['tool_id'],))
        # Töröljük a kölcsönzést
        conn.execute('DELETE FROM loans WHERE id = ?', (loan_id,))
        conn.commit()
    conn.close()
    return redirect(url_for('loans'))

@app.route('/add_tool', methods=('GET', 'POST'))
def add_tool():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        
        conn = get_db_connection()
        conn.execute('INSERT INTO tools (name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('add_tool.html')

@app.route('/person_details/<int:loan_id>')
def person_details(loan_id):
    conn = get_db_connection()
    loan = conn.execute('SELECT * FROM loans WHERE id = ?', (loan_id,)).fetchone()
    if loan:
        person = conn.execute('SELECT * FROM persons WHERE id = ?', (loan['person_id'],)).fetchone()
        if person:
            # Lekérjük az összes aktív kölcsönzést a személyhez (függetlenül a return_date-től)
            active_loans = conn.execute('''
                SELECT tools.name, loans.loan_date, loans.return_date
                FROM loans
                JOIN tools ON loans.tool_id = tools.id
                WHERE loans.person_id = ?
            ''', (loan['person_id'],)).fetchall()
            
            conn.close()
            # Átalakítjuk az eredményt listává
            tools_borrowed = [{'name': loan['name'], 'loan_date': loan['loan_date'], 'return_date': loan['return_date']} for loan in active_loans]
            
            return jsonify({
                'name': person['name'],
                'address': person['address'],
                'tools_borrowed': tools_borrowed
            })
    conn.close()
    return jsonify({'error': 'Személy nem található'}), 404

if __name__ == '__main__':
    app.run(debug=True)
