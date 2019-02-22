from PIL import Image, ImageTk
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import*
from tkinter.filedialog import*
from tkinter.simpledialog import*
from tkinter.colorchooser import*
from tkinter import messagebox
from datetime import*
from wand.image import*

    
## 함수 선언 부분 ##
    
## 이미지 열기 및 화면 출력 ##
def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + "x" + str(height))
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, width = width, height = height)
    paper = PhotoImage(width = width, height = height)
    canvas.create_image((width / 2, height / 2), image = paper, state = "normal")

    blob = img.make_blob(format = 'RGB')
    for i in range(0, width):
        for k in range(0, height):
            r = blob[(i*3*width) + (k*3) + 0]
            g = blob[(i*3*width) + (k*3) + 1]
            b = blob[(i*3*width) + (k*3) + 2]
            paper.put("#%02x%02x%02x" % (r,g,b), (k, i))

    canvas.pack()
    
def func_open(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent = window, filetypes = (("모든 그림 파일", "*jpg; *.jpg; *.bmp; *.png; *.tif; *.gif"), ("모든 파일", "*.*")))
    photo = Image(filename = readFp)
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

## 이미지 저장 ##
def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None :
        return
    saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg", filetypes = (("JPG 파일", "*.jpg; *.jepg"), ("모든 파일", "*.*")))
    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename = saveFp.name)
    
## 파일 종료 ##
def func_exit():
    window.quit()
    window.destroy

## 워터마크 ##
def func_watermark():
    messagebox.showinfo("워터마크란", "원본출처 및 정보를 삽입해 지적재산권을 보호할 수 있어요.")

    def watermark_text(input_image_path, output_image_path, text, pos):
        photo = Image.open(input_image_path)

        # make the image editable
        drawing = ImageDraw.Draw(photo)

        black = (3, 8, 12)
        font = ImageFont.truetype("궁서체", 40)
        drawing.text(pos, text, fill=black, font=font)
        photo.show()
        photo.save(output_image_path)

    if __name__ == '__main__':
        img = photo.clone()
        watermark_text(img, text="kyunghee's photoshop",  pos=(0, 0))

    
## 이미지 확대 및 축소 ##
def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대", "확대할 배율을 입력하세요", minvalue = 2, maxvalue = 4)
    photo2 = photo.clone()
    photo2.resize(int(oriX*scale), int(oriY*scale))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소", "축소할 배율을 입력하세요", minvalue = 2, maxvalue = 4)
    photo2 = photo.clone()
    photo2.resize(int(oriX/scale), int(oriY/scale))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

## 자르기 ##
def func_crop():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    cropped = photo2.crop((0, 0, 200 ,200))
    tk_im = ImageTk.PhotoImage(cropped)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
## 이미지 상하 및 좌우 반전 ##
def func_mirror1():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flip()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror2():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flop()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

## 이미지 회전 ##
def func_rotate(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue = 0, maxvalue = 360)
    photo2 = photo.clone()
    photo2.rotate(degree)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

## 이미지를 밝게 및 어둡게 ##
def func_bright(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue = 100, maxvalue = 200)
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_dark(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue = 0, maxvalue = 100)
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)    
    
## 이미지를 선명하게 및 탁하게 ##
def func_clear(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("선명하게", "값을 입력하세요(100~200)", minvalue = 100, maxvalue = 200)
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_unclear(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("탁하게", "값을 입력하세요(0~100)", minvalue = 0, maxvalue = 100)
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

## 이미지를 흑백으로 변경 ##
def func_bw(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.type = "grayscale"
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

## 그리기 ##
def mouseClick(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y
def mouseDrop(event):
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width=penWidth, fill=penColor)
def getColor():
    global penColor
    color = askcolor()
    penColor = color[1]
def getWidth():
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue = 1, maxvalue = 10)


##전역 변수 선언 부분##
window, canvas, paper = None, None, None
photo, photo2 = None,None
oriX, oriY = 0, 0
x1, y1, x2, y2 = None,None,None,None
penColor = 'black'
penWidth = 5
startDate, curDate, tm = '', '', None


##메인 코드 부분##
window= Tk()
window.geometry("300x300")
window.title("경희의 포토샵")

mainMenu = Menu(window)
window.config(menu = mainMenu)
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)
canvas = Canvas(window, height = 300, width = 300, bg = "pink", image = None)
canvas.bind("<Button - 1>", mouseClick)
canvas.bind("<ButtonRelease - 1>", mouseDrop)
canvas.pack()

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기",command = func_open)
fileMenu.add_command(label = "파일 저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "워터마크", command = func_watermark)
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

sizeMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "크기", menu = sizeMenu)
sizeMenu.add_command(label = "확대", command = func_zoomin)
sizeMenu.add_command(label = "축소", command = func_zoomout)
sizeMenu.add_command(label = "자르기", command = func_crop)

rotateMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "회전", menu = rotateMenu)
rotateMenu.add_command(label = "상하 반전", command = func_mirror1)
rotateMenu.add_command(label = "좌우 반전", command = func_mirror2)
rotateMenu.add_command(label = "회전", command = func_rotate)

colorMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "색상", menu = colorMenu)
colorMenu.add_command(label = "밝게", command = func_bright)
colorMenu.add_command(label = "어둡게", command = func_dark)
colorMenu.add_separator()
colorMenu.add_command(label = "선명하게", command = func_clear)
colorMenu.add_command(label = "탁하게", command = func_unclear)
colorMenu.add_separator()
colorMenu.add_command(label = "흑백이미지", command = func_bw)

decorateMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "꾸미기", menu = decorateMenu)
decorateMenu.add_command(label = "선 색상 선택", command = getColor)
decorateMenu.add_command(label = "선 두께 설정", command = getWidth)

window.mainloop()






















