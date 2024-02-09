from flask.views import MethodView

class OlaController(MethodView):
    def get(self):
        return "Rota ok."