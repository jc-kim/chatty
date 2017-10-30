from app import create_app
from app.views.chat import socketio

app = create_app()

if __name__ == '__main__':
    socketio.run(app)
#    app.run(app.config.get('HOST', 'localhost'), app.config.get('PORT', 5000),
#            app.config.get('DEBUG', False))

