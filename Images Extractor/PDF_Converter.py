
"""
STATUS: This shit works

OVERVIEW: Mainly converts images into pdfs, other function also avail

IMPROVEMENTS:
    - TODO Read through

What has beeen done:
    1. Importing all the necessary modules
    2. We need two path for:
        1. First path should be of a folder were the images are stored
        2. Second where we will store the pdfs
        ** These path are for checking and debugging of code
    3. ** There are two class Main/Solo
        1. Main class will only do the job required
        2. Solo is like a documented pdf making where we will print each file names which are made pdf
    4. Main:
        1. Initialising the pdf_folder_path and image_folder_path in the class
        2. MakePdf:
            ** This function will make pdf of an image whose name is given, and is in the images folder
        3. MakePdfs:
            ** This function will make all the images in the images folder into a seperate files in the a folder specified
        4. Pdfs_Merger:
            ** This function will merge all the pdfs in a specified folder
    5. Solo:
        1. This class does the same thing as above just one difference that we ae printing all the reseults in the console as output like:
            1. What files are made into pdf
            2. What files are merged
            3. If the merged files making is success or not
"""

# @ Imports
from PIL import Image # ! import name pillow
import os
from os import path
from PyPDF2 import PdfFileMerger


# * Defining
images_path = path.join('E:\Coding\Projects\Images Extractor\Database')
pdfs_path = path.join('E:\Coding\Projects\Images Extractor\Database')

class Main():
    """
    """

    @staticmethod
    def MakePdf(image_name, images_path, pdfs_path):
        image_object = Image.open(path.join(images_path, image_name))
        image = image_object.convert('RGB')

        pdf_image_name = f'{image_name[:-4]}.pdf'
        pdf_image_path = path.join(pdfs_path, pdf_image_name)

        image.save(pdf_image_path)

    def MakePdfs(self, images_folder_path, pdfs_folder_path):
        list_images = os.listdir(images_folder_path)

        for image in list_images:
            self.MakePdf(image, images_folder_path, pdfs_folder_path) 

    @staticmethod
    def Pdfs_Merger(pdfs_folder_path, filename):
        """
        """
        os.chdir(pdfs_folder_path)
        pdfs = os.listdir()

        merger = PdfFileMerger()

        for pdf in pdfs:
            merger.append(pdf)

        merger.write(filename + '.pdf')
        merger.close()

        list_images = os.listdir(images_path)

        for image in list_images:
            os.remove(f'{images_path}{image}')

        for pdf in pdfs:
            os.remove(f'{pdfs_path}{pdf}')

class Solo():
    def __init__(self, image_folder_path, pdf_folder_path):
        """
            So this functions makes a class a constructor
        """
        self.image_folder_path = image_folder_path
        self.pdf_folder_path = pdf_folder_path

    def D_MakePdf(self, pdf_folder_path, image_name):
        """
            What is done:
                1. Opening the image with PIL module
                2. Then converting the image into RGB format
                3. We will make a name for pdf file using f-string
                4. The we will make a path for that pdf file then we will save that pdf file
        """
        image_object = Image.open(path.join(self.image_folder_path, image_name))
        image = image_object.convert('RGB')

        image_name, _ = image_name.rsplit('.')
        pdf_image_name = f'{image_name}.pdf'

        pdf_image_path = path.join(pdf_folder_path, pdf_image_name)

        image.save(pdf_image_path)

    def D_MakePdfs(self, pdf_folder_path):
        """
            What is done:
                1. Making a list of name of images in the image_folder
                2. Also saving the list of format for simultanious images
                3. Trying to sort the images list via int number
                4. Similtaniously looping over both the above list to make pdf via above defined MakePdf
                    ** Printing success message is pdf is sucessfully made
        """
        list_images = [image[:-4] for image in os.listdir(self.image_folder_path)]

        try:
            list_images.sort(key=int)
        except:
            pass

        for image in list_images:
            try:
                self.D_MakePdf(pdf_folder_path, image + '.jpg')

            except Exception  as exception:
                print(f'{f"{image}.pdf"} unsucessfull, error! > MakePDFS')
                print(exception)

            else:
                print(f'{f"{image}.pdf"} sucessfully made! > MakePDFS')

        print('--------------------------------------------------------')

    @staticmethod
    def D_Pdfs_Merger(pdf_folder_path, filename, removePdfs=False, removeImages=True):
        """
            What is done:
                1. Changing the directories for conveniences
                2. Storting the names of the pdfs in the folder-path
                3. Storting the the pdfs with int format is it can be done
                4. Initialising the a merger from the PYPDF2 module
                5. Looping through all the pdf names(files):
                    1. Confirming is it a file or not
                    2. If yes the adding the file to the merger
                    3. And printing success message
                6. After all the pages are added to the pdf the intiliasing the file
                    ** Printing a success message
                7. Storing all the images name in a list
                8. Removing all the images files from the images-folder
                    ** Printing al remove statement

            Extra:
                9. We can also the pdf files if need

        """
        os.chdir(pdf_folder_path)
        int_pdfs = [pdf[:-4] for pdf in os.listdir()]

        try:
            int_pdfs.sort(key=int)
        except:
            pass

        merger = PdfFileMerger()

        for pdf in int_pdfs:
            if not path.isdir(path.join(pdf_folder_path, pdf)):
                print(f'{pdf}.pdf is merged with {filename}')
                merger.append(pdf+'.pdf')
            else:
                print(f'The directory {pdf} is not a file!')
        print('--------------------------------------------------------')

        merger.write(filename + '.pdf')
        merger.close()

        print(f'{filename} sucessfully made!')
        print('--------------------------------------------------------')

        list_images = os.listdir(images_path)

        if removeImages:
            for image in list_images:
                os.remove(f'{images_path}{image}')
                print(f'{image} sucessfully removed!')
            print('--------------------------------------------------------')

        if removePdfs:
            list_pdfs = os.listdir(pdf_folder_path)
            for pdf in list_pdfs:
                os.remove(f'{pdfs_path}{pdf}')
                print(f'{pdf} sucessfully removed!')
            print('--------------------------------------------------------')


# ? Implementation
if __name__ == "__main__":
    converter = Solo(images_path, pdfs_path)
    converter.D_MakePdfs(pdfs_path)
    converter.D_Pdfs_Merger(pdfs_path, 'GeekGods')
