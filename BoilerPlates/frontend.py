from tkinter import *
import cv2

def camera():
    cap = cv2.VideoCapture(0)
    while TRUE:
        ret, frame = cap.read()
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



main = Tk()
main.geometry('800x400')
main.title('Software')
enter = Entry(main)
enter.pack()
Button = Button(main, text="Click me")
Button.place(x=100, y=100)
main.mainloop()