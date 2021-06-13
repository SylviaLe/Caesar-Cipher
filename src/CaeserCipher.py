# Sylvia Le
# Date: 10/08/2019
# File: CaesarCipher.py
# Let the user choose encode a decode, then let them choose to type in the original message directly or get it from a file
 
from graphics import *
from tkinter.filedialog import askopenfilename    #import dialogue box for user to choose files from
from tkinter import messagebox                    #import message box to show notification

def isClick(pt, corner1, corner2, window):   #Function to check if user click a button
    x1 = corner1.getX()
    x2 = corner2.getX()
    y1 = corner1.getY()
    y2 = corner2.getY()

    if (pt.getX() >= x1 and pt.getX() <= x2) and pt.getY() >= y1 and pt.getY() <= y2:  #check if the mouse click is within the button
        return True
    else:
        return False

def drawButton(pt1,pt2,color,labelText,window):  #Funtion to draw button
    button=Rectangle(pt1,pt2)
    button.setFill(color)
    button.draw(window)

    centerX = (pt1.getX()+pt2.getX())/2
    centerY = (pt1.getY()+pt2.getY())/2
    
    #Put label on button
    label = Text(Point(centerX,centerY),labelText)
    label.setFill("black")
    label.setSize(11)
    label.draw(window)

def drawBox(pt1, pt2, pt3, window):   #create option box for user to choose their input source
    box1 = Rectangle(pt1, pt2)  
    box1.setFill('white')
    box1.draw(window)

    box2 = box1.clone()   #create a box similar to the first one, then move it
    box2.move(0, -15)
    box2.draw(window)

    #write description for the boxes
    choice1 = Text(pt3, "Type in the message  ")  
    choice1.setSize(9)
    choice1.setFill('white')
    choice1.draw(window)
    
    choice2 = choice1.clone()
    choice2.move(0, -15)
    choice2.setText("Get message from file")
    choice2.draw(window)

def encode(string, key):  #main encode function
    message = ""
    for char in string:
        if char.isalpha():   #check if the current digit is a letter, if yes then decode, if no then keep and add to the string
            newOrd = ord(char) + key    #move the order of the char by 'key' value forward

            if char.islower():
                newChar = chr(newOrd)
                if newOrd > ord("z"):
                    newChar = chr(newOrd - 26) #wrap around the alphabet 
            
            elif char.isupper() == True:
                newChar = chr(newOrd)
                if newOrd > ord("Z"):
                    newChar = chr(newOrd - 26) #wrap around the alphabet 
            message += newChar

        else:
            message += char   #keep the non-alphabetical stuff and add to the new string
    return message

def decode(string, key):  #main decode function
    message = ""
    for char in string:
        if char.isalpha():   #check if the current digit is a letter, if yes then decode, if no then keep and add to the string
            newOrd = ord(char) - key  ##move the order of the char by 'key' value backward

            if char.islower() == True:
                newChar = chr(newOrd)
                if newOrd < ord("a"):
                    newChar = chr(newOrd + 26) #wrap around the alphabet
            
            elif char.isupper() == True:
                newChar = chr(newOrd)
                if newOrd < ord("A"):
                    newChar = chr(newOrd + 26) #wrap around the alphabet
            message += newChar

        else:
            message += char  #keep the non-alphabetical stuff and add to the new string
    return message

def encodeDirect(window):  #let the user directly type in the message that needed to encode
    #draw and title the entry box for message
    inputPrompt = Text(Point(60, 400), "Enter the message:")
    inputPrompt.setSize(10)
    inputPrompt.setFill("white")
    inputPrompt.draw(window)
    inputMess = Entry(Point(150, 380), 50)
    inputMess.setSize(10)
    inputMess.draw(window)

    #draw and title the entry box for key
    keyPrompt = Text(Point(147, 360), "Enter the key between 1 and 26, then press Enter to encode")
    keyPrompt.setSize(10)
    keyPrompt.setFill('white')
    keyPrompt.draw(window)
    inputKey = Entry(Point(22, 340), 2)
    inputKey.setSize(10)
    inputKey.draw(window)

    #check for Enter key press
    while not window.getKey() == "Return":
        window.getKey()
        if window.getKey() == "Return":
            break     
    #If the user press Enter 
    try:
        message = inputMess.getText()
        key = int(inputKey.getText())
        #print the encoded message on te GUI window
        output = Text(Point(150, 300), "The translated text: " + encode(message, key))
        output.setFill('white')
        output.setSize(11)
        output.draw(window)
    #catch the error if the user type in invalid key  
    except:
        messagebox.showerror("Error", "Something you entered was invalid!")  #Show an error box notification if there is an error
    

def decodeDirect(window):  #let the user directly type in the message that needed to decode
    ##draw and title the entry box for message
    inputPrompt = Text(Point(360, 400), "Enter the message:")
    inputPrompt.setSize(10)
    inputPrompt.setFill("white")
    inputPrompt.draw(window)
    inputMess = Entry(Point(450, 380), 50)
    inputMess.setSize(10)
    inputMess.draw(window)                                                                                                                                                                                                                                                                                                                                    

    #draw and title the entry box for key
    keyPrompt = Text(Point(447, 360), "Enter the key between 1 and 26, then press Enter to encode")#because an other key >26 just doesn't make sense, 
    keyPrompt.setSize(10)
    keyPrompt.setFill('white')
    keyPrompt.draw(window)
    inputKey = Entry(Point(322, 340), 2)
    inputKey.setSize(10)
    inputKey.draw(window)
    
    #check for Enter key press
    while not window.getKey() == "Return":
        window.getKey()
        if window.getKey() == "Return":
            break     
    try:
        message = inputMess.getText()
        key = int(inputKey.getText())
        #print the decoded message on the GUI window
        output = Text(Point(450, 300), "The translated text:" + decode(message, key))
        output.setFill('white')
        output.setSize(11)
        output.draw(window)
    
    #catch the error if the user type in invalid key 
    except:
        messagebox.showerror("Error", "Something you entered was invalid!")

def encodeFile(window):    #let the user choose the file from their computer that they want tot encode
    #write the propmt for users to choose file, draw and title choose file button 
    inputPrompt = Text(Point(60, 400), "Choose the file: ")
    inputPrompt.setSize(10)
    inputPrompt.setFill("white")
    inputPrompt.draw(window)
    drawButton(Point(40, 370), Point(120, 390), "white", "Choose File...", window)

    #draw and title the entry box for key
    keyPrompt = Text(Point(157, 360), "Enter the key between 1 and 26, then click Encode to encode")
    keyPrompt.setSize(10)
    keyPrompt.setFill('white')
    keyPrompt.draw(window)
    inputKey = Entry(Point(35, 340), 2)
    inputKey.setSize(10)
    inputKey.draw(window)
    
    pt = window.getMouse()
    if isClick(pt, Point(40, 370), Point(120, 390), window):  #check if users click 'Choose File' button, then open file dialogue
        fileName = askopenfilename()
    
    pt1 = window.getMouse() 
    if isClick(pt1, Point(112.5, 450), Point(187.5, 475), window):  #check if users click the 'Encode' button again to start encoding
        try:  
            file = open(fileName, "r", encoding="utf8")
            text = file.read()
            key = int(inputKey.getText())
            encodedMess = encode(text, key)
            #write encoded message to another file
            encodeFile = open("Encoded File.txt", "w", encoding = "utf8")
            encodeFile.write(encodedMess)
            encodeFile.close()

            #tell the user that a new file is successfully written
            messagebox.showinfo("Information","Your file has been encoded and save in the file: Encoded File.txt")
        #error catching
        except:
            messagebox.showerror("Error", "Something went wrong")

def decodeFile(window):   #let the user choose the file from their computer that they want to decode
    #write the propmt for users to choose file, draw and title choose file button
    inputPrompt = Text(Point(360, 400), "Choose the file:")
    inputPrompt.setSize(10)
    inputPrompt.setFill("white")
    inputPrompt.draw(window)
    drawButton(Point(340, 370), Point(420, 390), "white", "Choose File...", window)
    
    #draw and title the entry box for key
    keyPrompt = Text(Point(458, 360), "Enter the key between 1 and 26, then click Decode to decode")
    keyPrompt.setSize(10)
    keyPrompt.setFill('white')
    keyPrompt.draw(window)
    inputKey = Entry(Point(331, 340), 2)
    inputKey.setSize(10)
    inputKey.draw(window)

    pt = window.getMouse()
    if isClick(pt, Point(340, 370), Point(420, 390), window): #check if users click 'Choose File' button, then open file dialogue
        fileName = askopenfilename()
        
    pt1 = window.getMouse()
    if isClick(pt1, Point(412.5, 450), Point(487.5, 475), window): #check if users click the 'Encode' button again to start encoding
        try:
            key = int(inputKey.getText())
            file = open(fileName, "r", encoding="utf8")
            text = file.read()
            decodedMess = decode(text, key)
            #write the decoded message into another file
            decodeFile = open("Decoded File.txt", "w", encoding = "utf8")
            decodeFile.write(decodedMess)
            decodeFile.close()

            #tell the user that a new file is successfully writtem
            messagebox.showinfo("Information","Your file has been decoded and save in the file: Decoded File.txt")
        except:
            messagebox.showerror("Error", "Something went wrong")

def main():
    #create GUI window and setup basic "canvas"
    win = GraphWin("Caesar Cipher", 800, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("black")
    
    #draw the program name
    proName = Text(Point(300, 550), "Caesar Cipher")
    proName.setFace("courier")
    proName.setSize(30)
    proName.setTextColor("SpringGreen2")
    proName.setStyle('bold')
    proName.draw(win)
    
           
    
    #draw prompts
    choicePrompt = Text(Point(300, 500), "Click the button to encode or decode")
    choicePrompt.setFace('arial')
    choicePrompt.setSize(11)
    choicePrompt.setTextColor('snow')
    choicePrompt.draw(win)

    #Create 3 basics button for user to choose
    drawButton(Point(112.5, 450), Point(187.5, 475), "white", "Encode", win)
    drawButton(Point(412.5, 450), Point(487.5, 475), "white", "Decode", win)
    drawButton(Point(275, 200), Point(325, 225), "white", "Quit", win )

    pt = win.getMouse()
    while isClick(pt, Point(275, 200), Point(325, 225), win) == False:  #while the "Quit" button is not clicked
        
        if isClick(pt, Point(112.5, 450), Point(187.5, 475), win):  #if the Encode button is clicked
            #Create option boxes. The user will either choose to type in directly or choose text from a file
            drawBox(Point(70, 430), Point(80, 440), Point(150, 435), win)

            pt1 = win.getMouse()
            if isClick(pt1, Point(70, 430), Point(80, 440), win): #if the user click the box that says to type in message to encode
                pt1.draw(win)
                encodeDirect(win)
                
            elif isClick(pt1, Point(70, 415), Point(80, 425), win): #if the user click the box that says to choose file to encode
                pt1.draw(win)
                encodeFile(win)

        elif isClick(pt, Point(412.5, 450), Point(487.5, 475), win):  #if the Decode button is clicked
            #Create option boxes. The user will either choose to type in directly or choose text from a file
            drawBox(Point(370, 430), Point(380, 440), Point(450, 435), win)
        
            pt2 = win.getMouse()
            
            if isClick(pt2, Point(370, 430), Point(380, 440), win):  #if the user click the box that says to type in message to decode
                pt2.draw(win)
                decodeDirect(win)
                
            elif isClick(pt2, Point(370, 415), Point(380, 425), win): #if the user click the box that says to type in message to decode
                pt2.draw(win)
                decodeFile(win)

        pt = win.getMouse()
    win.close()
main()



