from os import listdir, walk, path
from bs4 import BeautifulSoup
import copy


class IndexMaker:

    def __init__(self, main_dir):

        self.exclude = ['.DS_Store', 'landing_page.html']
        self.main_dir = main_dir
        base_dir = open(path.dirname(path.abspath(__file__)) + '/baseline.html')
        self.base_html = BeautifulSoup(base_dir, 'lxml')

    def generate_contents(self):

        subdirectories = [loc[0]for loc in walk(self.main_dir)]  # extracting all sub/directories

        for location in subdirectories:

            titles = [f for f in listdir(location) if f not in self.exclude]  # pulling all folder/file names
            local_html = copy.copy(self.base_html)  # creating a new copy of the baseline contents table

            if len(titles) == 0:
                continue

            page_title = location.split('/')[-1]  # setting standard title
            local_html.title.string = page_title
            local_html.find("h1").string = page_title

            button_loc = local_html.find("div", class_="btn-group")  # button area

            display_fix = False
            for title in titles:
                display_title = title.split('.html')[0]  # differentiates between folders and files
                if len(display_title) > 42:
                    display_fix = True
                if '.html' not in title and '.pdf' not in title:
                    link_title = title + '/landing_page.html'
                else:
                    link_title = title
                # attach a new tag per item
                new_tag = local_html.new_tag('button', onclick="window.location.href='./%s'" % link_title)
                new_tag.string = display_title

                button_loc.append(new_tag)

            if display_fix or len(titles) == 1:
                local_html.style.string = local_html.style.string.replace('width: 70%', 'width: 100%')

            with open(location+'/landing_page.html', "w") as file:
                file.write(str(local_html.prettify()))
