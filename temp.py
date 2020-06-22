import socket
html_str = """
<!DOCTYPE HTML><html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 3.5rem; }
    p { font-size: 3.0rem; }
    .units { font-size: 15rem; }
    .sensor-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 2px;
    }
    .button {
        font-size: 4.0rem; display: inline-block; background-color: #ddaa00; border: none; 
        border-radius: 10px; color: white; padding: 30px 32px; text-decoration: none;
        font-size: 30px; margin-bottom: 0px; cursor: pointer; margin-left: 18px; margin-right: 18px
    }
    .button2 {
        background-color: #000000; padding: 30px 35px; 
    }
    .button3 {
        background-color: #00aa44; padding: 32px 64px; margin-top: 50px; border-radius: 10px; font-size: 30px;
    }
    .button4 {
        background-color: #1111ff; padding: 32px 46px; border-radius: 10px; font-size: 30px;
    }
    </style>
    </head>
    <body>
    <h2>ECE 40862 Final Project Controls</h2>
    <p>
    Directional Inputs
    </p>
    <p>
    <a><button class="button">▲</button></a>
    <p>
    <a><button class="button">◄</button></a>
    <a><button class="button button2">◆</button></a>
    <a><button class="button">►</button></a>
    </p>
    <p><a><button class="button">▼</button></a>
    </p>  
    <p>
    <a><button class="button button3">Manual</button></a>
    <a><button class="button button4">Automatic</button></a>
    </p>
    </body>
    </html>"""


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #station = network.WLAN(network.STA_IF)le
    print("good")
    #address = socket.getaddrinfo('192.168.137.65', 1025)[0][-1]
    sock.bind(('0.0.0.0',1111))
    #print(address)
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        receive = connection.recv(1024)
        connection.send('HTTP/1.1 200 OK\nContent-type: text/html\nConnection: close\n\n')
        connection.sendall(html_str)
        connection.close()
        