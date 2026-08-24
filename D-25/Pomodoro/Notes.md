>> NOTES ON POMODORO:

there is class called photo image which can be use to save a image as file

PhotoImage(file= "image.png")

there is another class canvas which is used to add images on the gui window
first create canvas object canvas = Canvas() inside () keep canvas width and height
then to add the image use create_image() module on canvas object and pass args as tuple for image location,
also image key with its value as the photoimage class

canvas = Canvas(width=200,height=224)
canvas.create_image(100,112,image= tomato_image)
canvas.pack()

you can add bg color to the canvas and window using bg as a key in the canvas class and to wndows using config.