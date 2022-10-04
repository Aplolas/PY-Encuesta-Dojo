from dojo_encuesta import app
from dojo_encuesta.controllers import controlers
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

if __name__ == '__main__':
    app.run(debug= True)
