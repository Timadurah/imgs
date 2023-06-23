import customtkinter
import http.client
import urllib.parse
from tkinter import *

customtkinter.set_appearance_mode("dark")
# give it theam color dark blue
customtkinter.set_default_color_theme("dark-blue")
# set ctk
root = customtkinter.CTk()
# set the window size
root.geometry("500x800")
# give it title
root.title("SMS BOOMBER")
# Set the window icon
# root.iconbitmap("smsy.ico")
 
 # set k for loop count
k = 0
# textvar for result
labelText = StringVar()
# function to run forms and api


def sms_send_tim():
    passwordy = password_entry.get()
    namey = username_entry.get()
    urlly = Base_url_entry.get()
    iddy = Sender_id_entry.get()
    Textty = urllib.parse.quote(Text_box_entry.get())
    Phoney = Phones_entry.get()
    listy = [Phoney]
    clist = len(listy)

    conn = http.client.HTTPSConnection(urlly)
    payload = ''

    for phone in listy:
        global my_text
        my_text = k+1
        headers = {
            'Accept': 'application/json'
        }
        conn.request("GET", "/sms/1/text/query?username="+namey+"&password="+passwordy+"&from="+iddy+"&to="+phone+"&text="+Textty +
                     "&flash=false&transliteration=TURKISH&languageCode=TR&intermediateReport=true&notifyUrl=https://www.example.com&notifyContentType=application/json&callbackData=callbackData&validityPeriod=720&track=URL&trackingType=Custom%20tracking%20type", payload, headers)
        res = conn.getresponse()
        data = res.read()

        f = open("./Infobip.txt", "w")
        f.write(data.decode("utf-8"))
        f.close()
        print(data.decode("utf-8"))
        ltv = "", my_text, 'Message sent out of', clist, ""
        labelText.set(ltv)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="INFOIP SMS BOOMBER")
label.pack(pady=12, padx=10)
resulty = customtkinter.CTkLabel(master=frame, textvariable=labelText)
resulty.pack(pady=12, padx=10)

username_entry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Username")
username_entry.pack(pady=12, padx=10)

password_entry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Account password")
password_entry.pack(pady=12, padx=10)

Base_url_entry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Base url")
Base_url_entry.pack(pady=12, padx=10)

Sender_id_entry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Sender ID")
Sender_id_entry.pack(pady=12, padx=10)

Text_box_entry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Text Box")
Text_box_entry.pack(pady=12, padx=10)

Phones_entry = customtkinter.CTkEntry(
    master=frame, height=200, width=200, placeholder_text="Phones seperate with comma")
Phones_entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(
    master=frame, text="Broadcast", command=sms_send_tim)
button.pack(pady=12, padx=10)

# upl = customtkinter.CTkButton(
#     master=frame, text='Open', command=UploadAction)
# upl.pack()

# checkbox = customtkinter.CTkCheckBox(master=frame, text="remember me")
# checkbox.pack(pady=12, padx=10)

root.mainloop()


# thanks
