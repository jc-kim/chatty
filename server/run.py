from app import app

if __name__ == '__main__':
    app.run(app.config.get('HOST', 'localhost'), app.config.get('PORT', 5000), app.config.get('DEBUG', False))