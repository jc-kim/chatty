from app import create_app


app = create_app()


if __name__ == '__main__':
    app.run(app.config.get('HOST', 'localhost'), app.config.get('PORT', 5000),
            app.config.get('DEBUG', False))