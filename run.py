from flask import *
from flask_socketio import *

# Init the server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'some super secret key!'
socketio = SocketIO(app, logger=True)


# Display the HTML Page & pass in a username parameter
@app.route('/')
def html():
    return render_template('index.html')

# Receive a message from the front end HTML
@socketio.on('send_message')   
def message_recieved(data):
    client_cmd = data['text']
    print(client_cmd)
    if client_cmd == "/login":
        for i in range(5):
            emit('message_from_server', {'text': f"Executing selenium Module with python run {i} " })
    elif client_cmd == "/help":
        emit('message_from_server', {'text': "This is just Beginning" })
    else:
        emit('message_from_server', {'text': "type /help to know More !" })

# Actually Start the App
if __name__ == '__main__':
    """ Run the app. """    
    socketio.run(app, host="0.0.0.0", port=5000)
