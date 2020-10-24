from PIL import Image
import PIL
import os

def combineImages():
    images = []
    
    for i,filename in enumerate(os.listdir(glbl_folder)):
        temp_image = Image.open(glbl_folder + os.path.sep + filename)
        images.append(temp_image)
        if (i > 0):
            images[i] = PIL.ImageChops.multiply(images[i-1], images[i])
    images[len(images)-1].show()
    images[len(images)-1].save(glbl_folder + os.path.sep + "OUTPUT.png","PNG")

if __name__ == '__main__':
    # Dear User, please create a folder "imagesz" right next to where your python file is located.
    # You will put your input files in there. 
    # After running this program you can also find OUTPUT.png in there as well.
    glbl_folder = "imagesz"
    if os.path.isdir(glbl_folder):
        combineImages()
    else:
        os.path.
        print('INVALID... FOLDER %s RESTART.' % glbl_folder)
