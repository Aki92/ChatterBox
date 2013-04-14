<<<<<<< HEAD
import socket
=======
from socket import *
>>>>>>> parent of b5f1978... Project Files.
import pyaudio
from Tkinter import *
import thread

<<<<<<< HEAD
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("", 5015))
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
=======
PORT = 5016

#port for msg.
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
sock.bind(("", PORT))
>>>>>>> parent of b5f1978... Project Files.

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100

def streamopen():
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK)
    return stream

<<<<<<< HEAD
def fetch( ):
    msg = ent.get( )
    ent.delete(0, len(msg)+1)
    sock.sendto(msg, addr)
    sock.sendto(socket.gethostname(), addr)
    Label(root,text=socket.gethostname()+":    "+msg).pack(side=TOP)
    
def recieve():
    while True:
        try:
            msg = sock.recv(262144)
            rec = sock.recv(1024)
            Label(root,text = rec+":    "+msg).pack(side=TOP)
        except:
            return

menu = '''
Press 1 for TEXT MESSAGING
Press 2 for VOICE CHAT\n
'''

msg,addr = sock.recvfrom(1024)
print menu
opt = raw_input()
sock.sendto(opt,addr)
if opt == '1':
    if msg=="Start":
        root = Tk()
        root.title(string = socket.gethostname())
        root.geometry("200x200")
        ent = Entry(root)
        ent.pack(side=BOTTOM, fill=X)
        ent.focus()                # save a click
        ent.bind('<Return>', (lambda event: fetch())) 
        btn = Button(root,text='SEND MESSAGE',command = fetch)
        btn.pack(side=BOTTOM,after=ent)
        thread.start_new_thread(recieve,())
        root.mainloop()
elif opt == '2':
    stream = streamopen()
    sock.setblocking(0)
    while True:
        try:
            data = stream.read(CHUNK)
            sock.sendto(data,addr)
        except:
            continue

        try:
            data = sock.recv(262144)
            stream.write(data, CHUNK)
        except:
            continue
    stream.stop_stream()
    stream.close()
    p.terminate()
                    
print("done")
=======
#common function
def mfetch():
    msg = ent.get()
    ent.delete(0, len(msg)+1)
    sock.sendto('m'+gethostname(), addr)
    sock.sendto(msg, addr)
    Label(im,text=gethostname()+":    "+msg).pack(side=TOP)

#function for opt == 1
def recieve():
    while True:
        rec = sock.recv(1024)
        msg = sock.recv(262144)
        Label(im,text = rec[1:]+":    "+msg).pack(side=TOP)

#function for opt == 2
def play():
    while chatflag != 1:
        try:
            data = stream.read(CHUNK)
            sock.sendto(data,addr)
        except:
            pass

        try:
            data = sock.recv(262144)
            stream.write(data, CHUNK)
        except:
            pass
        
def stop():
    global chatflag
    stream.stop_stream()
    stream.close()
    chat.destroy()
    chatflag = 1
    
#function for opt == 3
def vmsendrecieve():
    while imflag != 1 or chatflag != 1:
        try:
            data = stream.read(CHUNK)
            sock.sendto('v', addr)
            sock.sendto(data,addr)
        except:
            pass
        try:
            rec = sock.recv(1024)
            data = sock.recv(262144)
            if rec[0] == 'm':
                Label(im,text = rec[1:] + ":    "+data).pack(side=TOP)
            else:
                stream.write(data, CHUNK)
        except:
            pass

    
menu = '''
Press 1: TEXT MESSAGING
Press 2: VOICE CHAT
Press 3: TEXT MESSAGING & VOICE CHAT\n
'''

msg,addr = sock.recvfrom(5)
print menu
opt = raw_input()
sock.sendto(opt,addr)

if opt == '1':
    im = Tk()
    im.title(string = gethostname())
    im.geometry("200x500")
    ent = Entry(im)
    ent.pack(side=BOTTOM, fill=X)
    ent.focus()                # save a click
    ent.bind('<Return>', (lambda event: mfetch())) 
    btn = Button(im,text='SEND MESSAGE',command = mfetch)
    btn.pack(side=BOTTOM,after=ent)
    thread.start_new_thread(recieve,())
    im.mainloop()

elif opt == '2':
    chatflag = 0
    stream = streamopen()
    sock.setblocking(0)
    chat = Tk()
    chat.title(string = "Chatter Box")
    chat.geometry("200x50")
    Label(chat,text="CHATTER BOX").pack(side=TOP)
    Button(chat,text='STOP CHATTING',command = stop).pack(side=BOTTOM)
    thread.start_new_thread(play,())
    chat.mainloop()
    
elif opt == '3':
    chatflag = 0
    imflag = 0
    stream = streamopen()
    sock.setblocking(0)
    im = Tk()               #instant messaging window
    chat = Tk()             #chat window

    im.title(string = gethostname()+'1')
    im.geometry("200x500")
    ent = Entry(im)
    ent.pack(side=BOTTOM, fill=X)
    ent.focus()
    ent.bind('<Return>', (lambda event: mfetch())) 
    Button(im,text='SEND MESSAGE',command = mfetch).pack(side=BOTTOM,after=ent)
    
    chat.title(string = "Chatter Box")
    chat.geometry("200x50")
    Label(chat,text="CHATTER BOX").pack(side=TOP)
    Button(chat,text='STOP CHATTING',command = stop).pack(side=BOTTOM)
    thread.start_new_thread(vmsendrecieve,())
    def im_on():
        im.mainloop()    
    chat.after(100,im_on)
    chat.mainloop()
    
print("done")
imflag = 1
>>>>>>> parent of b5f1978... Project Files.

            
    
