def askurl(urlbase):
    import urllib.request
    #模擬瀏覽器頭部訊息，向網站發送信息
    header={
        'User-Agent': 'Mozilla/5.0'
            }
    #模擬用户代理
    request = urllib.request.Request(urlbase,headers=header)
    #異常超時處理
    try:
        # html=""
        response = urllib.request.urlopen(request,timeout=5)
        html = response.read().decode("utf-8")
        # print(html)
    except Exception as a:
        print(a)
    return html

def road(url):
    link = f"{url}"
    # 獲得html文檔信息
    html = askurl(link)
    #解析數據
    soup = BeautifulSoup(html,"html.parser")
    name = []       #建立空列表用於儲存數據
    winRate = []
    pickRate = []
    banRate = []
    for tr in soup.find(name = "tbody").children:
    # 判斷tr是否為標籤類型，去除空行
        if isinstance(tr,bs4.element.Tag):
            # 查找tr標籤下的td標籤
            tds = tr('td')
            # 英雄名
            name.append(tds[1].find("strong").text)
            # 勝率 %百分號對後續有影響，去除
            winRate.append(tds[3].text.replace('%',''))
            # 選取率
            pickRate.append(tds[4].text.replace('%',''))

            banRate.append(tds[5].text.replace('%',''))
    return name,winRate,pickRate,banRate

from sklearn.linear_model import LinearRegression
import requests
from bs4 import BeautifulSoup
import bs4
import tkinter as tk
from PIL import ImageTk, Image
from io import BytesIO
import os
import numpy as np

#獲取index
def search_text_in_list(text, lst):
    try:
        index = lst.index(text)
        return index
    except ValueError:
        return -1

#取得英雄名稱
def get_hero_name():
    url = 'https://u.gg/lol/champions'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    champion_data = []

    champion_tags = soup.find_all(class_='champion-name')
    for tag in champion_tags:
        champion_name = tag.text.strip()
        champion_data.append(champion_name)
    return champion_data

#創建資料夾
def make_a_folder():
    path = "./hero"
    os.makedirs(path)

#爬取英雄照片
def get_hero_img():
    url = 'https://u.gg/lol/champions'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ls = soup.select('div.image-wrapper')

    for k in range(len(text_list)):
        imgs = ls[k].select('img')
        for i in imgs:
            imgurl = '{}'.format(i['src'])
            path = 'hero/{}.jpg'.format(i['alt'])
            content = requests.get(imgurl).content
            with open(path, 'wb') as file:
                file.write(content)

#按下按鈕後的動作(創建新的視窗)
def create_new_page(hero_name):
    new_window = tk.Toplevel(window)
    new_window.title(f'{hero_name}')
    new_window.geometry('1200x700')
    new_window.resizable(False, False)
    label = tk.Label(new_window, text=f"Hero Name: {hero_name}")
    label.pack()

    count = 0
    road = []
    win = []                       # 對應的目標值

    patch1 = tk.Label(new_window, text="(Patch 13.11)")
    patch1.pack()

    index = search_text_in_list(hero_name, name1)
    if index != -1:
        lane = 'Top'
        win_rate = winRate1[index]
        pick_rate = pickRate1[index]
        ban_rate = banRate1[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name2)
    if index != -1:
        lane = 'Jungle'
        win_rate = winRate2[index]
        pick_rate = pickRate2[index]
        ban_rate = banRate2[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name3)
    if index != -1:
        lane = 'Mid'
        win_rate = winRate3[index]
        pick_rate = pickRate3[index]
        ban_rate = banRate3[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name4)
    if index != -1:
        lane = 'ADC'
        win_rate = winRate4[index]
        pick_rate = pickRate4[index]
        ban_rate = banRate4[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name5)
    if index != -1:
        lane = 'Support'
        win_rate = winRate5[index]
        pick_rate = pickRate5[index]
        ban_rate = banRate5[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    patch2 = tk.Label(new_window, text="(Patch 13.10)")
    patch2.pack()

    index = search_text_in_list(hero_name, name_1)
    if index != -1:
        lane = 'Top'
        win_rate = winRate_1[index]
        pick_rate = pickRate_1[index]
        ban_rate = banRate_1[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name_2)
    if index != -1:
        lane = 'Jungle'
        win_rate = winRate_2[index]
        pick_rate = pickRate_2[index]
        ban_rate = banRate_2[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name_3)
    if index != -1:
        lane = 'Mid'
        win_rate = winRate_3[index]
        pick_rate = pickRate_3[index]
        ban_rate = banRate_3[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name_4)
    if index != -1:
        lane = 'ADC'
        win_rate = winRate_4[index]
        pick_rate = pickRate_4[index]
        ban_rate = banRate_4[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name_5)
    if index != -1:
        lane = 'Support'
        win_rate = winRate_5[index]
        pick_rate = pickRate_5[index]
        ban_rate = banRate_5[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    patch3 = tk.Label(new_window, text="(Patch 13.09)")
    patch3.pack()

    index = search_text_in_list(hero_name, name__1)
    if index != -1:
        lane = 'Top'
        win_rate = winRate__1[index]
        pick_rate = pickRate__1[index]
        ban_rate = banRate__1[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name__2)
    if index != -1:
        lane = 'Jungle'
        win_rate = winRate__2[index]
        pick_rate = pickRate__2[index]
        ban_rate = banRate__2[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name__3)
    if index != -1:
        lane = 'Mid'
        win_rate = winRate__3[index]
        pick_rate = pickRate__3[index]
        ban_rate = banRate__3[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name__4)
    if index != -1:
        lane = 'ADC'
        win_rate = winRate__4[index]
        pick_rate = pickRate__4[index]
        ban_rate = banRate__4[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)

    index = search_text_in_list(hero_name, name__5)
    if index != -1:
        lane = 'Support'
        win_rate = winRate__5[index]
        pick_rate = pickRate__5[index]
        ban_rate = banRate__5[index]
        infor_label = tk.Label(new_window, text=f"Lane: {lane}\nWin Rate: {win_rate}%\nPick Rate: {pick_rate}%\nBan Rate: {ban_rate}%")
        infor_label.pack()
        win.append(win_rate)
        count = count + 1
        road.append(lane)
    #線性回歸部分處理
    if(count == 3):
        X = np.array([[1], [2], [3]])  # 輸入的數據點
        y = np.array(win, dtype=np.float64)

        model = LinearRegression()
        # 擬合模型
        model.fit(X, y)
        next_number = model.predict([[4]])
        infor_label = tk.Label(new_window,text = f"{road[0]}下版本勝率預測值為:{next_number}%")
        infor_label.pack()
        
    elif(count == 6):
        X = np.array([[1], [2], [3]])  # 輸入的數據點
        y1 = []
        y2 = []
        for i in range(3):
            y1.append(win[i])
            y2.append(win[i+3])
        y1 = np.array(y1, dtype=np.float64)
        y2 = np.array(y2, dtype=np.float64)
        model1 = LinearRegression()
        model2 = LinearRegression()
        # 擬合模型
        a = model1.fit(X, y1)
        b = model2.fit(X, y2)
        next_number1 = a.predict([[4]])
        next_number2 = b.predict([[4]])
        infor_label1 = tk.Label(new_window,text = f"{road[0]}下版本勝率預測值為:{next_number1}%")
        infor_label2 = tk.Label(new_window,text = f"{road[1]}下版本勝率預測值為:{next_number2}%")
        infor_label1.pack()
        infor_label2.pack()

# hero列表
text_list = get_hero_name()
k = len(text_list)
# make_a_folder() 目前已創建所以就不執行了
# get_hero_img()

#用網址去爬取資料
name1, winRate1, pickRate1,banRate1 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&position=top')
name2, winRate2, pickRate2,banRate2 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&position=jungle')
name3, winRate3, pickRate3,banRate3 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&position=mid')
name4, winRate4, pickRate4,banRate4 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&position=adc')
name5, winRate5, pickRate5,banRate5 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&position=support')
#以下這兩個要隨著版本的不同去更改其網址，不然不能執行
name_1, winRate_1, pickRate_1,banRate_1 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.10&position=top')
name_2, winRate_2, pickRate_2,banRate_2 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.10&position=jungle')
name_3, winRate_3, pickRate_3,banRate_3 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.10&position=mid')
name_4, winRate_4, pickRate_4,banRate_4 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.10&position=adc')
name_5, winRate_5, pickRate_5,banRate_5 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.10&position=support')

name__1, winRate__1, pickRate__1,banRate__1 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.09&position=top')
name__2, winRate__2, pickRate__2,banRate__2 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.09&position=jungle')
name__3, winRate__3, pickRate__3,banRate__3 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.09&position=mid')
name__4, winRate__4, pickRate__4,banRate__4 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.09&position=adc')
name__5, winRate__5, pickRate__5,banRate__5 = road('https://www.op.gg/champions?region=global&tier=platinum_plus&patch=13.09&position=support')

# 創建主窗口
window = tk.Tk()
window.title('GUI')
window.geometry('1200x700')
window.resizable(False, False)
window.iconbitmap('lol.ico')

# 圖像所在的文件夾路徑
image_folder = './hero/'

# 讀取所有圖像文件
image_files = os.listdir(image_folder)

# 創建滾動條
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 創建Canvas
canvas = tk.Canvas(window, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 設置Canvas的滾動條連接
scrollbar.config(command=canvas.yview)

# 創建框架，用於放置按鈕和文字
frame = tk.Frame(canvas)
canvas.create_window(0, 0, anchor=tk.NW, window=frame)

# 遍歷圖像文件，創建按鈕和文字並排版
buttons = []
for i, image_file in enumerate(image_files):
    image_path = os.path.join(image_folder, image_file)

    # 載入圖像並調整大小
    img = Image.open(image_path)
    img = img.resize((100, 100))
    photo = ImageTk.PhotoImage(img)

    # 創建按鈕
    button = tk.Button(frame, image=photo, text=text_list[i], compound=tk.TOP, command=lambda name=text_list[i]: create_new_page(name))
    button.image = photo  # 保持圖像引用，否則圖像無法正常顯示
    button.grid(row=i // 10, column=i % 10, padx=5, pady=5)

# 設置Canvas的滾動區域
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

# 啟用滑鼠滾輪滾動
canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units'))

# 啟動主窗口的事件迴圈
window.mainloop()
