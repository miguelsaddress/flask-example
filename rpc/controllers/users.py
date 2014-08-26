import rpc.flaskext as flaskext
import flask.ext.classy as classy
from domain.container import container


class Users(classy.FlaskView):
    def __init__(self):
        self.user_repository = container('models_user_repository')

    @flaskext.rpc_method('/', schema='foo')
    def index(self):
        query = self.user_repository.create_query().find_active()
        result = self.user_repository.find(query)

        output = {}
        for user in result.all():
            output[user.email] = {
                'email': user.email,
                'created_at': user.created_at,
                'last_name': user.last_name,
                'first_name': user.first_name
            }

        return output

    @classy.route('/get/<int:id>/')
    def get(self, id):
        return 'id %d' % id
