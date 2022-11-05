"""
STATUS: Working

OVERVIEW: Uses the [Image Extractor] and [PDF Converter] to extract a chapters of manga in pdf format

IMPROVEMENTS:
    - TODO Document this shit

"""

# @ Imports
from Images_Extractor import ExtractPanels
from Practice.PDF_Converter import Solo
import os

images_folder_path = 'F://NP DATA BACKUP\Mangas/Images/'
pdf_folder_path = 'F://NP DATA BACKUP\Mangas/PDFS/'

# * Defining

def ExctractSeries(main_url, series_name, extra_chapters=[], endingChapter=1, startingChapter=0, mode=0):
  """
  """
  list_manga_links = [f'{main_url[:-1]}{index + startingChapter + 1}/' for index in range(endingChapter - startingChapter - 1)]

  # * If we need to recover only one chapter of manga hence extra_chapters in in string
  if type(extra_chapters) is str:
      manga_chapter_name = f'{series_name}_Chapter_{extra_chapters}'
      pdfs_folder_path = os.path.join(pdf_folder_path, manga_chapter_name)

      link = f'{main_url}{extra_chapters}'

      try:
        ExtractPanels(link, images_folder_path)

        os.chdir(pdf_folder_path)
        os.mkdir(manga_chapter_name)
        os.chdir(pdfs_folder_path)

        converter = Solo(images_folder_path, pdf_folder_path)

        print('-----------------------------------------')      
        converter.D_MakePdfs(pdfs_folder_path=pdfs_folder_path)

        print('Files made into pdfs!')

        converter.D_Pdfs_Merger(pdfs_folder_path, manga_chapter_name)

      except Exception as exception:
        print(exception)
        print(link)

  # * This for multiple chapters of the manga extra_chapters will be empty hence no extra chapters will be added
  elif type(extra_chapters) is list:
      list_manga_links.extend(extra_chapters)

      for chapter_index, links  in enumerate(list_manga_links, startingChapter):
        manga_chapter_name = f'{series_name}_Chapter_{chapter_index}'
        pdfs_folder_path = os.path.join(pdf_folder_path, manga_chapter_name)

        try:
          ExtractPanels(links, images_folder_path)

          os.chdir(pdf_folder_path)
          os.mkdir(manga_chapter_name)
          os.chdir(pdfs_folder_path)

          converter = Solo(images_folder_path, pdf_folder_path)

          print('-----------------------------------------')
          converter.D_MakePdfs(pdfs_folder_path)

          print('Files made into pdfs!')

          converter.D_Pdfs_Merger(pdfs_folder_path, manga_chapter_name)

        except Exception as exception:
          print(exception)
          print(links)


# ? Implementation
if __name__ == "__main__":
  url = input('Enter M- Url: ')
  extra_chapter = input('Enter Extra chapter: ')
  starting_chapter = int(input('Starting Chapter: '))
  ending_chapter = int(input('Ending Chapter: '))
  chapter_name = input('Chapter name: ')
  ExctractSeries(url, chapter_name, extra_chapters=extra_chapter if extra_chapter else [],startingChapter=starting_chapter, endingChapter=ending_chapter)

