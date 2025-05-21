# This is a simple Flask application

from flask import Flask
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)


class MyApp:
    def __init__(self, name = None, info= None):
        self.name = name if name else "Demo App"
        self.info = info if info else "This is a simple Flask application."
        self.setup_routes()

    def setup_routes(self):
        @app.get('/')
        def get_name():
            logger.info("{self.name} is running")
            return f"Welcome to Flask World App!<br>This is {self.name}"

        @app.get('/about')    
        def about():
            return f"About this app:<br>{self.info}"
    
    def run(self):
        try:
            app.run(debug=True)
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise
            

if __name__ == "__main__":
    my_app = MyApp()
    my_app.run()
