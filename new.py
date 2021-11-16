import cv2
import dropbox
import random
import time

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("SNAPSHOT TAKEN")
    
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.A8ay6rR9NObRyaMpZ9frb8qPD0oBebgBYnsp58M2Jd7qFEQHlJyZevTkO4AqK4TeeelNwY2pn6atxOz7AybO1p2vbXum2LYoLYUMM1mDPfLp7gQnh-DBoMWdHhDMe5O37wHpF7E"
    file=img_name
    file_from=file
    file_to="/DROPBOX/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()
