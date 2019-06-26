import os
import cherrypy

class HelloWorld:

    @cherrypy.expose
    def index(self):
        return 'We have a <a href="hello_message">message</a> for you!'

    @cherrypy.expose
    def hello_message(self):
        return 'Hi buddy! Say your name <a href="./say_your_full_name">here</a>'

    @cherrypy.expose
    def say_your_full_name(self):
        return '''
            <form action="get_xml" method="GET">
            What's your name?
            <input type="text" name="first_name" />
            <input type="text" name="last_name" />
            <input type="submit" />
            </form>'''

    # @cherrypy.expose
    # def greetUser(self, first_name=None, last_name=None):
    #     if (first_name and last_name):
    #         return 'Hi {} {}!'.format(first_name, last_name)
    #     else:
    #         if first_name is None: return 'Please enter your first name <a href="./say_your_full_name">here</a>.'
    #         if last_name is None: return 'Please enter your last name <a href="./say_your_full_name">here</a>.'

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def get_xml(self):
        fn = cherrypy.request.json['first_name']
        ln = cherrypy.request.json['last_name']
        if (fn and ln):
            from jinja2 import Template
            template = Template('''
            <?xml version="1.0"?>
            <person iri="https://ruben.verborgh.org/profile/#me"><first_name>{{ first_name }}</first>
            <last_name>{{ last_name }}</last_name>
            </person></xml>
            ''')
            return template.render(first_name=fn, last_name=ln)
        else:
            if fn is None: return 'Please enter your first name <a href="./say_your_full_name">here</a>.'
            if ln is None: return 'Please enter your last name <a href="./say_your_full_name">here</a>.'


#server_conf = os.path.join(os.path.dirname(__file__), 'cherry-ws.conf')


if __name__ == '__main__':
    #cherrypy.quickstart(HelloWorld(), server_conf)
    cherrypy.quickstart(HelloWorld())
