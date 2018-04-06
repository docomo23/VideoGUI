import time
import cv2
import tkinter as tk
import os

video_frame_size = (640, 480)
item_font_size = 25
description_font_size = 18
items_list = ["base", "distance-angle", "up-down-sideface", "left-right-sideface", "blocking", "with-glasses",
              "lighting", "multi-people"]
ID = "1"
root_path = "./data/ID_%d/" % int(ID)
max_image_amount = 5
interval_threshold = 20
path_list = "./path_list%d.txt" % int(ID)
video_length_short = 2
video_length_normal = 5
video_length_long = 12
video_length_extralong = 20


def record(item_text, scenario_texts, IDname, video_length, mode):
    path = root_path + item_text + "/" + mode + "/"
    if not os.path.exists(path):
        os.makedirs(path)
        
    file_name_pre = ""
    for scenario_text in scenario_texts:
        file_name_pre = file_name_pre + scenario_text + "_"
    file_name_pre = file_name_pre[:-1]
    file_name = path + file_name_pre + ".avi"
    print(file_name)
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    ################################################
    # might need to change here
    ################################################
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(file_name, fourcc, 20.0, video_frame_size)
    start = end = time.time()
    while (end - start < video_length):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Save the image
        out.write(frame)
        # Display the resulting frame
        cv2.namedWindow('recording....', cv2.WINDOW_NORMAL)
        cv2.imshow('recording....', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        end = time.time()
    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # video to images
    video2images(path, file_name_pre, IDname)


def video2images(path, video_name_pre, IDname):
    image_path = path + "imgs/"
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    video_name = path + video_name_pre + ".avi"
    #print(final_video_path)
    cap = cv2.VideoCapture(video_name)
    interval = 0
    counter = 0
    success, frame = cap.read()
    while success:
        print(interval)
        if counter > max_image_amount:
            #print("counter exit")
            break
        if interval > interval_threshold:
            cv2.imwrite(image_path + video_name_pre + "_img%d.jpg" % counter, frame)
            counter = counter + 1
        interval = interval + 1
        success, frame = cap.read()


def create_widget(page, item_text, scenario_texts, IDname, video_length):
    tk.Label(page, text=",".join(scenario_texts), font=("Helvetica", description_font_size)).pack()
    var = tk.IntVar()
    page.btn = tk.Checkbutton(master=page, variable=var)
    page.btn["text"] = "face record"
    page.btn["command"] = lambda: record(item_text, scenario_texts, IDname, video_length, "face")
    page.btn.pack(side="top")
    
    var = tk.IntVar()
    page.btn = tk.Checkbutton(master=page, variable=var)
    page.btn["text"] = "hand record"
    page.btn["command"] = lambda: record(item_text, scenario_texts, IDname, video_length * 2 + 1, "hand")
    page.btn.pack(side="top")


def init(toplevel):
    toplevel.title("Image Capture")
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = (1000, 600)
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    toplevel.attributes('-topmost', 'true')


def newSubPage(item_text, Page):
    if item_text == "base":
        return Page1(Page)
    if item_text == "distance-angle":
        return Page2(Page)
    if item_text == "up-down-sideface":
        return Page3(Page)
    if item_text == "left-right-sideface":
        return Page4(Page)
    if item_text == "blocking":
        return Page5(Page)
    if item_text == "with-glasses":
        return Page6(Page)
    if item_text == "lighting":
        return Page7(Page)
    if item_text == "multi-people":
        return Page8(Page)


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        
        item_text = "base"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="人脸录入： 人站在离摄像头0.5米处，分别录入正脸，左侧脸，右侧脸。强光状态下(开灯），弱光状态下（关上窗帘）。"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_short
        create_widget(self, item_text, ["strong-light", "front-side"], ID, video_length)
        create_widget(self, item_text, ["strong-light", "left-side"], ID, video_length)
        create_widget(self, item_text, ["strong-light", "right-side"], ID, video_length)
        create_widget(self, item_text, ["weak-light", "front-side"], ID, video_length)
        create_widget(self, item_text, ["weak-light", "left-side"], ID, video_length)
        create_widget(self, item_text, ["weak-light", "right-side"], ID, video_length)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "distance-angle"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="距离角度测试：在地上画一个扇形，分别标记在0-0.5米， 0.5米-1米，1米-2米， 左右角度（0-10°，10°-20°， 20°-30°）。"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_normal
        create_widget(self, item_text, ["0-0.5", "L", "0-20"], ID, video_length)
        create_widget(self, item_text, ["0-0.5", "L", "20-40"], ID, video_length)
        create_widget(self, item_text, ["0-0.5", "R", "0-20"], ID, video_length)
        create_widget(self, item_text, ["0-0.5", "R", "20-40"], ID, video_length)
        create_widget(self, item_text, ["0.5-1", "L", "0-20"], ID, video_length)
        create_widget(self, item_text, ["0.5-1", "L", "20-40"], ID, video_length)
        create_widget(self, item_text, ["0.5-1", "R", "0-20"], ID, video_length)
        create_widget(self, item_text, ["0.5-1", "R", "20-40"], ID, video_length)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "up-down-sideface"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="上下侧脸测试：测试人在0.5米处，目视前方，在摄像头的上下（0-10度，10-20度，20-30度，30-50度。"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_normal
        create_widget(self, item_text, ["up", "0-20"], ID, video_length)
        create_widget(self, item_text, ["up", "20-40"], ID, video_length)
        create_widget(self, item_text, ["down", "0-20"], ID, video_length)
        create_widget(self, item_text, ["down", "20-40"], ID, video_length)


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "left-right-sideface"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="左右测试：每人目视前方，站在镜头的0.5米处，向左右0.5米，每人拍十张，检查正确率和误判率。"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_normal
        create_widget(self, item_text, ["L", "0.5"], "3.avi", video_length)
        create_widget(self, item_text, ["R", "0.5"], "4.avi", video_length)


class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "blocking"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="遮挡测试：每人站在0.5米用纸片挡住脸的上下左右分别（1/10，1/8，1/4），每人每个方位遮挡拍十张"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_normal
        create_widget(self, item_text, ["up", "10th"], ID, video_length)
        create_widget(self, item_text, ["up", "8th"], ID, video_length)
        create_widget(self, item_text, ["up", "4th"], ID, video_length)
        create_widget(self, item_text, ["down", "10th"], ID, video_length)
        create_widget(self, item_text, ["down", "8th"], ID, video_length)
        create_widget(self, item_text, ["down", "4th"], ID, video_length)
        create_widget(self, item_text, ["right", "10th"], ID, video_length)
        create_widget(self, item_text, ["right", "8th"], ID, video_length)
        create_widget(self, item_text, ["right", "4th"], ID, video_length)
        create_widget(self, item_text, ["left", "10th"], ID, video_length)
        create_widget(self, item_text, ["left", "8th"], ID, video_length)
        create_widget(self, item_text, ["left", "4th"], ID, video_length)


class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "with-glasses"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="眼镜测试： 每人站在0.5米，戴眼镜，托眼镜分别拍五张"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_normal
        create_widget(self, item_text, ["with"], ID, video_length)
        create_widget(self, item_text, ["without"], ID, video_length)


class Page7(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "lighting"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="光照测试：人站在1米处，在强光的状态下（开灯）和弱光状态下（拉上窗帘）。"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_normal
        create_widget(self, item_text, ["strong-light"], ID, video_length)
        create_widget(self, item_text, ["weak-light"], ID, video_length)


class Page8(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        item_text = "multi-people"
        label = tk.Label(self, text=item_text, font=("Helvetica", item_font_size))
        label.pack()
        label = tk.Label(self, text="多人测试：在画面内同时出现多人，无误识别。建议用录像的形式进行测试。"
                         , font=("Helvetica", description_font_size))
        label.pack()
        video_length = video_length_extralong
        create_widget(self, item_text, ["multi-people"], ID, video_length)


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
    from sys import argv, exit
    if len(argv) != 2:
        print("please input ID")
        exit()
    ID = argv[1]
    root_path = "./data/ID_%d/" % int(ID)
    print("ID:%d" % int(ID))
    print(root_path)
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    init(root)
    root.mainloop()