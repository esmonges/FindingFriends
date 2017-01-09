from flask import render_template
from pylib.ServerSetup.FlaskAppSetup import AppSetup


class SetupFlaskRoutes(object):
    routes_are_set_up = False

    @staticmethod
    def setup_flask_routes():
        if SetupFlaskRoutes.routes_are_set_up is not True:
            app = AppSetup.get_app()

            # Flask socketio test
            @app.route('/socketiotest')
            def socket_io_test():
                return render_template('SocketIOTest.html')

            @app.route('/socketiostresstest')
            def socket_io_stress_test():
                return render_template('StressTestSocketIO.html')

            # Autobahn socket test
            @app.route('/socket_test')
            def socket_test():
                return render_template('autobahnflasksockettest.html')

            SetupFlaskRoutes.routes_are_set_up = True
