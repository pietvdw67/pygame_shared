import pygame
import os
import math

pygame.init()


class ImagePacker:

    SOURCE_FOLDER = 'C:/Users/f3953289/Downloads/FreeTileset/png/Tiles'
    TARGET_FILE = 'C:/Users/f3953289/Downloads/terrain.png'
    OUTPUT_COL = 4
    OUTPUT_ROW = 5

    def __init__(self):
        screen_width, screen_height = 800, 600
        screen = pygame.display.set_mode((screen_width, screen_height))

    def pack(self, source_folder, target_file, cols_text, rows_text):

        try:
            cols = int(cols_text)
            rows = int(rows_text)
            current_index = 0
            images_list = []

            max_width, max_height = ImagePacker.get_tile_width_and_height(source_folder)
            entries = os.listdir(source_folder)
            image_target = pygame.Surface((max_width * cols, max_height * rows), pygame.SRCALPHA)

            for row in range(rows):
                for col in range(cols):
                    if current_index < len(entries):
                        image = pygame.image.load(os.path.join(source_folder, entries[current_index]))
                        image_target.blit(image, (col * max_width, row*max_height))
                        current_index += 1

            pygame.image.save(image_target, target_file)
        except Exception as e:
            print(e)

        pygame.quit()
        return f'Output file created, tile size is Width: {max_width}, Height: {max_height}'

    @staticmethod
    def get_suggested_layout(amount_of_images: int) -> ():

        if amount_of_images <= 0:
            return 0, 0

        columns = math.ceil(math.sqrt(amount_of_images))
        rows = math.ceil(amount_of_images / columns)

        return columns, rows

    @staticmethod
    def get_tile_width_and_height(source_folder):
        entries = os.listdir(source_folder)
        max_height = 0
        max_width = 0
        for entry in entries:
            file_name = os.path.join(source_folder, entry)
            image = pygame.image.load(file_name)
            max_height = max(max_height, image.get_height())
            max_width = max(max_width, image.get_width())

        return max_width, max_height

if __name__ == '__main__':
    result = ImagePacker().pack(ImagePacker.SOURCE_FOLDER, ImagePacker.TARGET_FILE, ImagePacker.OUTPUT_COL,ImagePacker.OUTPUT_ROW)
    print(result)
