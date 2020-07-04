
import os.path
import subprocess
from image_downloader import ImageDownloader
from scrapy.crawler import CrawlerProcess
from scrapper import Scrapper
import pandas as pd
import os
import pathlib


def main():
    data_filename = 'data.csv'
    image_filename = 'image.jpg'
    absolute_path = str(pathlib.Path(__file__).parent.absolute())
    image_filename_absolute_path = absolute_path + '/' + image_filename
    os.remove(data_filename)
    process = CrawlerProcess()
    process.crawl(Scrapper)
    process.start()
    data_parsed = parse_data(data_filename)
    sample = data_parsed.sample()
    imageDownloader = ImageDownloader(sample['url_image'].item(), image_filename)
    if imageDownloader.successfull_download:
        set_gnome_wallpaper(image_filename_absolute_path)
    else: 
        print('Error downloading, cannot set gnome wallpaper')


def set_gnome_wallpaper(file_path):
    if os.path.isfile(file_path):
        command = "gsettings set org.gnome.desktop.background picture-uri {}".format(
            file_path)
        list_command = list(command.split(' '))
        subprocess.run(list_command)
        print('Changed Succesfully')
    else:
        print('Does not exists {}'.format(file_path))


def parse_data(filename):
    base_url = 'https://unsplash.com'
    data = pd.read_csv(filename)
    data.dropna(inplace=True)
    data['url_image'] = data['url_image'].apply(
        lambda url: base_url + url + '/download?force=true')
    return data


if __name__ == '__main__':
    main()
