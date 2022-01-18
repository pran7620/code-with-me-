import fitz as ft

file = ft.open("11.pdf")
for i in range(len(file)):
    for image in file.get_page_images(i):
        xref= image[0]
        pix = ft.Pixmap(file,xref)
        if pix.n < 5:
            pix.save("I%s-%s.png" % (i,xref))
        else:
            pixy=ft.Pixmap(ft.csRGB,pix)
            pixy.save("I%s-%s.png" % (i,xref))
            pixy=None
        pix= None

print("image extraction is completed")        
