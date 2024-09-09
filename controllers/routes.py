from flask import redirect, render_template, url_for, request, flash
from models.database import db, Suplementos

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/supplements', methods=['GET', 'POST'])
    def supplements():
        per_page = 4
        page = request.args.get('page', 1, type=int)
        paginated_suplementos = Suplementos.query.paginate(page=page, per_page=per_page, error_out=False)
        return render_template('supplements.html', supplements=paginated_suplementos)

    @app.route('/supplements/delete/<int:id>', methods=['GET', 'POST'])
    def delete_supplement(id):
        suplemento = Suplementos.query.get(id)
        if suplemento:
            db.session.delete(suplemento)
            db.session.commit()
        return redirect(url_for('supplements'))

    @app.route('/add_supplement', methods=['GET', 'POST'])
    def add_supplement():
        if request.method == 'POST':
            novoSuplemento = Suplementos(
                titulo=request.form['titulo'],
                categoria=request.form['categoria'],
                ano=request.form['ano'],
                descricao=request.form['descricao']
            )
            db.session.add(novoSuplemento)
            db.session.commit()
            return redirect(url_for('supplements'))
        return render_template('add_supplement.html')

    @app.route('/edit_supplement/<int:id>', methods=['GET', 'POST'])
    def edit_supplement(id):
        suplemento = Suplementos.query.get(id)
        if suplemento is None:
            flash('Suplemento não encontrado.')
            return redirect(url_for('supplements'))
        if request.method == 'POST':
            suplemento.titulo = request.form['titulo']
            suplemento.ano = request.form['ano']
            suplemento.categoria = request.form['categoria']
            suplemento.descricao = request.form['descricao']
            db.session.commit()
            return redirect(url_for('supplements'))
        return render_template('edit_supplement.html', suplemento=suplemento)
