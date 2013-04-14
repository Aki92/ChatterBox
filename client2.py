from socket import *
import pyaudio
from Tkinter import *
import thread

PORT = 5016

host = ("localhost", PORT)
sock = socket(AF_INET,SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

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

#common function
def mfetch():
    msg = ent.get( )
    ent.delete(0, len(msg)+1)
    sock.sendto('m'+gethostname(), host)
    sock.sendto(msg, host)
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
            sock.sendto(data,host)
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
            sock.sendto('v', host)
            sock.sendto(data,host)
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

    
sock.sendto("Start",host)
opt = sock.recv(1)

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

    im.title(string = gethostname())
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
            
