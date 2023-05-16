from pathlib import Path
from abc import ABC, abstractmethod

from django.core.files.images import ImageFile
from django.conf import settings


class IConvertor(ABC):

    @abstractmethod
    def save_resized_image(self, width: int = 270) -> str:
        pass

    @abstractmethod
    def save_webp_image(self) -> str:
        pass


class ImageConvertor(IConvertor):

    SMALL_PREFIX = 'small_'

    def __init__(self, img: ImageFile, upload_path: str):
        self.img = img
        self.upload_path = upload_path
        self.media_dir = settings.BASE_DIR / settings.MEDIA_FOLDER
        self.full_upload_path = self.media_dir / self.upload_path

    def save_resized_image(self, width: int = 270) -> str:
        self.__resize(width)
        name = self._get_name_of_resized()
        self._save_in_media_folder(name)
        relative_path = self._get_relative_path(name)
        return relative_path

    def save_webp_image(self) -> str:
        name = self._get_new_file_name()
        self._save_in_media_folder(name)
        relative_path = self._get_relative_path(name)
        return relative_path

    def _save_in_media_folder(self, name: str, format: str = None) -> None:
        full_path = self.full_upload_path / name
        self.img.save(full_path, format=format)

    def _get_relative_path(self, name: str) -> str:
        relative_path = self.upload_path + name
        return relative_path

    def __resize(self, width: int) -> None:
        r = self.__get_ratio()
        self.img.thumbnail((width, int(width / r)))

    def __get_ratio(self) -> float:
        w, h = self.img.size
        ratio = w / h
        return ratio

    def _get_name_of_resized(self) -> str:
        prefix = ImageConvertor.SMALL_PREFIX
        name = self._get_new_file_name(prefix)
        return name

    def _get_new_file_name(self, prefix='') -> str:
        file_name = Path(self.img.filename).stem
        return f'{prefix}{file_name}.webp'


class ImageConvertorFactory:

    @staticmethod
    def get_convertor(img: ImageFile, upload_path: str) -> IConvertor:
        return ImageConvertor(img, upload_path)
