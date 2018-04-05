import tkinter as tk
import os
video_frame_size = (640,480)
video_length = 5
item_font_size = 20
description_font_size = 13
items_list = ["人脸录入", "距离角度测试", "上下侧脸测试", "左右测试", "遮挡测试", "眼镜测试", "光照测试", "多人测试"]

def record(item_text, scenario_text, filename):
    path = "./" + item_text + "/" + scenario_text + "/"
    if not os.path.exists(path):
        os.makedirs(path)
    path = path + filename
    print(path)
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    ################################################
    # might need to change here
    ################################################
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path, fourcc, 20.0, video_frame_size)
    start = end = time.time()
    while(end - start < video_length):
        # Capture frame-by-frame
        ret, frame = cap.read()

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


def create_widget(page, item_text, scenario_text, description, filename):
        tk.Label(page, text=description, font=("Helvetica", description_font_size)).pack()
        var = tk.IntVar()
        page.btn = tk.Checkbutton(master=page, variable=var)
        page.btn["text"] = scenario_text
        page.btn["command"] = lambda: record(item_text, scenario_text, filename)
        page.btn.pack(side="top")

def init(toplevel):
    toplevel.title("Image Capture")
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = (1000, 600)
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    toplevel.attributes('-topmost', 'true')
    
    
def newSubPage(item_text, Page):
    if item_text == "人脸录入":
        return Page1(Page)
    if item_text == "距离角度测试":
        return Page2(Page)
    if item_text == "上下侧脸测试":
        return Page3(Page) 
    if item_text == "左右测试":
        return Page4(Page)     
    if item_text == "遮挡测试":
        return Page5(Page) 
    if item_text == "眼镜测试":
        return Page6(Page)
    if item_text == "光照测试":
        return Page7(Page) 
    if item_text == "多人测试":
        return Page8(Page)     

    
    
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "人脸录入"
        label = tk.Label(self, text=item_text, font = ("Helvetica", description_font_size))
        label.pack()
        create_widget(self, item_text, "强光", "正常光线，距离（1-2米）的识别率", "3.avi")
        create_widget(self, item_text, "弱光", "正常光线，距离（1-2米）的误识别率", "4.avi")

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "距离角度测试"
        label = tk.Label(self, text=item_text, font = ("Helvetica", description_font_size))
        label.pack()
        create_widget(self, item_text, "0-0.5", "正常光线，距离（0-0.5米）的识别率", "3.avi")
        create_widget(self, item_text, "0.5-1", "正常光线，距离（1-2米）的误识别率", "4.avi")

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)
        
class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)
        
class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)
        
class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

class Page7(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

class Page8(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        pages = []
        btns = []
        
        for item_text in items_list:
            p = newSubPage(item_text, self)
            p.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            pages.append(p)
            b = tk.Button(buttonframe, text=item_text, command=p.lift)
            b.pack(side="left")
            btns.append(b)

        pages[0].show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    init(root)
    root.mainloop()
