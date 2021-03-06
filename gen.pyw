from bs4 import BeautifulSoup
from PIL import Image, ImageFont, ImageDraw
from tkinter import Tk, Label, Button
import requests
import glob
import os
import socket


def create_img():
    def find_file(drive):
    # Checks for file in the drive list 
    #for i in drive_list:
        i = drive
        os.chdir(r'{}'.format(i))
        if glob.glob('counter.txt'):
            return True
        else:
            return False

    if find_file(os.getcwd()) == False:
        f =  open("counter.txt", "x")
        f.write("0")
        f.close()

    def giveText():
        page = requests.get("https://funnysentences.com/sentence-generator/")
        soup = BeautifulSoup(page.content, 'html.parser')
        data = soup.find("div", {"id": "sentencegen"})
        with open("last_sentence.txt", "a") as f:
            f.write("{}\n".format(data.get_text()))
        f.close()
        print(data.get_text())
        return data.get_text()

    def enterNewLine(text):
        if len(text) > 60:
            list1 = list(text)
            i = 60
            while list1[i]:
                #print(list1[i], end=" ")
                if i < len(text):
                    i += 1
                    if list1[i] == " ":
                        list1[i] = "\n"       
                        break 
                    else:
                        break
                else:
                    break
            str1 = ""
            for i in list1:
                str1 += i     
            return str1
        else:
            return text


    img = Image.new('RGBA',(1080,1080),'white')
    text = enterNewLine(giveText()) # calling function to get structered text

    #font = ImageFont.truetype("poppins.ttf",28)
    try : 
        font = ImageFont.truetype("C:\\Users\\SANFAL\\Downloads\\miri_font_files\\Roboto-Medium.ttf",28)
    except:
        font = ImageFont.truetype("arial.ttf",28)
        
    width, height = font.getsize(text)
    draw = ImageDraw.Draw(img)
    draw.text((((1080-width)/2)+32, (1080-height)/2), text, font=font, fill="black")

    with open("counter.txt", "r") as f:
        recent_counter = f.read()
        recent_counter = int(recent_counter)
        
    with open("counter.txt", "w") as f:
        update_counter = recent_counter + 1
        f.write("{}".format(update_counter))
        
    img.save("generated_{}.png".format(recent_counter))

    img.show()
    img.close()
    del img

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


from tkinter import Tk, Label, Button

t = Tk()
t.title("i m a g e   g e n e r a t o r")
t.iconbitmap("C:\\Users\\SANFAL\\Desktop\\text_gen\\icon.ico")
t.geometry('900x500')
t.resizable(width='FALSE', height='FALSE')

heading = Label(t,text="c r e a t i n g   i m a g e s   u s i n g   r a n d o m   t e x t", font=('arial', 15, 'italic','bold'),fg="#2B2B2B")
heading.place(x=185,y=100)

referrence = Label(t,text="text is generated by www.funnysentences.com/sentence-generator/", font=('arial', 10, 'bold'),fg="#2B2B2B")
referrence.place(x=225, y=150)

request = Label(t,text="do not edit the counter file ^_^ Thanks\nWait for couple of minutes before generating a new image be kind since too many request will lead to ban of your ip address", font=('arial', 10, 'bold'),fg="#2B2B2B")
request.place(x=40, y=400)

wifi = Label(t,text="i n t e r n e t   i s   n e e d e d", font=('arial', 10, 'bold'),fg="#2B2B2B")
wifi.place(x=345,y=290)

if is_connected() == False:
    wifi = Label(t,text="n o   i n t e r n e t   c o n n e c t i o n   f o u n d", font=('arial', 10, 'bold'),fg="red")
    wifi.place(x=285,y=310)


generate = Button(t, text="g e n e r a t e .", font=('arial', 14, 'bold'),fg="#2B2B2B", command=create_img)
generate.place(x=365,y=240)

t.mainloop()

