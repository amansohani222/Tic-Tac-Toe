import tkinter
from tkinter import messagebox
root = tkinter.Tk()
window = tkinter.Frame(root)
window.pack()
x=1
b = []
def check_game(p):
    flagG=0;
    t='O'
    if p==1:
       t='X'
    for i in range(0, 3):
        flag=1
        for j in range(0, 3):
            if b[i][j]["text"]!=t:
                flag=0
        if flag==1:
            messagebox.showinfo("You Won", "Winner is player"+str(p))
    for i in range(0, 3):
        flag=1
        for j in range(0, 3):
            if b[j][i]["text"]!=t:
                flag=0
        if flag==1:
            messagebox.showinfo("Result", "Winner is player"+str(p))
    if ((b[0][0]["text"]==t)and(b[1][1]["text"]==t)and(b[2][2]["text"]==t))or((b[0][2]["text"]==t)and(b[1][1]["text"]==t)and(b[2][0]["text"]==t)):
        messagebox.showinfo("Result", "Winner is player" + str(p))
    flagG=1;
    for i in range(0, 3):
        for j in range(0, 3):
            if b[i][j]["text"]==' ':
                flagG=0
    if flagG==1:
        messagebox.showinfo("Result", "It's a DRAW")

def click(event):
    global x
    global b
    if event.widget['text']==' ':
        if x == 1:
            #print(x);
            event.widget.config(text='X')
            check_game(x)
            x=0
        else:
            #print(x);
            event.widget.config(text='O')
            check_game(x)
            x=1
        event.widget.config(state=DISABLED)
        print(event.widget['text'])

def start_game():
    global x
    x=1;
    for i in range(0, 3):
        a = []
        for j in range(0, 3):
            btn = tkinter.Button(window, width='7', height='3');
            btn.grid(row=(i + 1), column=(j + 1))
            btn['text']=' ';
            btn.bind('<Button-1>', click)
            a.append(btn)
        b.append(a)

start_game()
l1 = tkinter.Label(window, text='Player '+str(x)+' move').grid(row = '4', column = '2');
cnt=0;

window.mainloop();
