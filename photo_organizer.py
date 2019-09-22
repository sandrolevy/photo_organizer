import os
import shutil
import mimetypes
from datetime import datetime
from PIL import Image

class PhotoOrganizer:
    def folder_path_from_photo_date(self, file):
        date = self.photo_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    def photo_shooting_date(self, file):
        photo = Image.open(file)
        info = photo._getexif()
        date = datetime.fromtimestamp(os.path.getmtime(file))
        if info:
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        return date

    def move_photo(self, file):
        new_folder = self.folder_path_from_photo_date(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file,new_folder + '/' + file)

    def organize_photos(self):
        all_photos = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.get_extensions_for_type_of_file())
        ]
        for filename in all_photos:
            self.move_photo(filename)

    def get_extensions_for_type_of_file(self):
        general_type = 'image'
        image_extensions = []
        for ext in mimetypes.types_map:
            if mimetypes.types_map[ext].split('/')[0] == general_type:
                image_extensions.append(ext)
        return image_extensions

PO = PhotoOrganizer()
PO.organize_photos()

