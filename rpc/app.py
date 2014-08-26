import flask
import rpc.controllers as controllers
import rpc.fixtures as fixtures

fixtures.create_fixtures()

app = flask.Flask(__name__)
app.debug = True

controllers.Users.register(app)

if __name__ == "__main__":
    print 'Available routes: \n%s \n' % app.url_map
    app.run()
