from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

#total size coontainer
file_size=0

#progress check
def progress(stream,chunk,file_handle,remaining=None):
    # gets percentage of file that has been downloaded...
    
    file_downloaded=(file_size-file_handle)
    per=float(file_downloaded/file_size)*100
    dBtn.config(text="{:00.0f} % Downloaded".format(per))


def startDownload():
    global file_size
    try:
        url=urlField.get()
        # changing button text
        dBtn.config(text='Please wait...')
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if(path_to_save_video is None):
            return
        #creating youtbe object with url
        ob = YouTube(url,on_progress_callback=progress)

        # fetch all streams
        # strms = ob.streams.all()

        # for s in strms:
        # print(s)

        strm = ob.streams.get_by_itag(22)
        file_size=strm.filesize
        vTittle.config(text=strm.title)
        vTittle.pack(side=TOP)
        # print(strm)
        # print(strm.filesize)
        # print(strm.title)
        # print(ob.title)

        #downloading the video
        strm.download(path_to_save_video)
        print('done')
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded Successfully")
        urlField.delete(0,END)
        vTittle.pack_forget()

    except Exception as e:
        print(e)
        print("error!!")

def startDownloadThread():
    thread =Thread(target=startDownload)
    thread.start()

# starting gui building
main= Tk()
main.title("My YouTube Downloader")
img = PhotoImage(file='icon.gif')
main.tk.call('wm', 'iconphoto', main._w, img)
main.geometry("500x600")
# heading icon
file= PhotoImage(file='icon.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP,pady=20)

# url textfield
urlField= Entry(main,font=("verdana",20),justify=CENTER)
urlField.pack(side=TOP, fill=X,padx=10,pady=20)

#download button
dBtn= Button(main,text="Start Download",font=("verdana",20),relief='ridge',command=startDownloadThread)
dBtn.pack(side=TOP,pady=10)

#video title
vTittle = Label(main,text='Video Title')

main.mainloop()

