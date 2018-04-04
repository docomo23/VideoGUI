import tkinter as tk
import time
import cv2
video_frame_size = (640,480)
video_length = 5
def init(toplevel):
    toplevel.title("Image Capture")
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_)*3 for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    toplevel.attributes('-topmost', 'true')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.record_btn = tk.Button(self)
        self.record_btn["text"] = "start record"
        self.record_btn["command"] = self.record
        self.record_btn.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        
        
    def record(self):
        cap = cv2.VideoCapture(0)
        # Define the codec and create VideoWriter object
        ################################################
        # might need to change here
        ################################################
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, video_frame_size)
        start = end = time.time()
        while(end - start < video_length):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Save the image
            out.write(frame)
            # Display the resulting frame
            cv2.namedWindow('recording....', cv2.WINDOW_NORMAL)
            cv2.imshow('recording....',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            end = time.time()

        # When everything done, release the capture
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        
root = tk.Tk()
init(root)
app = Application(master=root)
root.mainloop()



