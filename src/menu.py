import PySimpleGUI as sg

from const import (
    FONT_SIZE,
    GENRE_NAME_DATA_NUMBER,
    DATE_BIRTH_DATA_NUMBER,
    COMPANY_NAME_DATA_NUMBER,
    ONE_COLUMN_LENGTH,
)


class MainMenu:
    HEADINGS_NAME = ['ゲーム名', 'ジャンル', '発売年', '会社名']
    BUTTON_NAME = ['追加', '編集', '詳細', '削除', '検索', '再読込']

    def __init__(self, number, sum_number, game_list, genre, date_birth, company):
        self.number = number
        self.sum_number = sum_number
        self.game_list = game_list
        self.genre = genre
        self.date_birth = date_birth
        self.company = company

    def show(self, input_text, values_data):
        previous_page = []
        next_page = []

        headings = [
            [sg.Text(text=self.HEADINGS_NAME[0], size=(20, 1), font=FONT_SIZE),
             sg.ButtonMenu(button_text=self.HEADINGS_NAME[1], menu_def=['', self.genre], size=(14, 1), font=FONT_SIZE,
                           key=GENRE_NAME_DATA_NUMBER),
             sg.ButtonMenu(button_text=self.HEADINGS_NAME[2], menu_def=['', self.date_birth], size=(14, 1),
                           font=FONT_SIZE, key=DATE_BIRTH_DATA_NUMBER),
             sg.ButtonMenu(button_text=self.HEADINGS_NAME[3], menu_def=['', self.company], size=(14, 1), font=FONT_SIZE,
                           key=COMPANY_NAME_DATA_NUMBER),
             ]
        ]

        if len(values_data) != 0 and values_data[0] == input_text:
            input_text = ''

        layout = [
            [sg.Text(size=(13, 1)),
             sg.Input(size=(20, 1), font=FONT_SIZE, default_text=input_text),
             sg.Button(button_text=self.BUTTON_NAME[4], size=(20, 1), font=FONT_SIZE, key='search'),
             sg.Button(button_text=self.BUTTON_NAME[5], size=(13, 1), font=FONT_SIZE),
             ]
        ]
        layout += headings

        for game in self.game_list:
            if game.site == 'site':
                button_color = ('white', 'black')

            else:
                button_color = ('black', 'white')

            layout += [
                [sg.Button(game.name, size=(19, 1), font=FONT_SIZE, button_color=button_color),
                 sg.Text(game.genre, size=(15, 1), font=FONT_SIZE),
                 sg.Text(game.date_birth + '年', size=(15, 1), font=FONT_SIZE),
                 sg.Text(game.company, size=(15, 1), font=FONT_SIZE),
                 ]
            ]
        # Determine if you need a button
        if self.number > 0:
            previous_page = [sg.Submit(button_text='前の10件', size=(33, 1), font=FONT_SIZE, key='previous')]

        if self.sum_number > (self.number + 1) * ONE_COLUMN_LENGTH:
            # Adjust the position by putting in a space
            if self.number == 0:
                previous_page = [sg.Text(' ', size=(32, 1), font=FONT_SIZE)]

            next_page = [sg.Submit(button_text='次の10件', size=(33, 1), font=FONT_SIZE, key='next')]
            next_number = self.number + ONE_COLUMN_LENGTH

        else:
            next_number = self.sum_number

        layout += [previous_page + next_page,
                   [sg.Button(button_text=self.BUTTON_NAME[0], size=(15, 1), font=FONT_SIZE),
                    sg.Button(button_text=self.BUTTON_NAME[1], size=(15, 1), font=FONT_SIZE),
                    sg.Button(button_text=self.BUTTON_NAME[2], size=(15, 1), font=FONT_SIZE),
                    sg.Button(button_text=self.BUTTON_NAME[3], size=(15, 1), font=FONT_SIZE),
                    ],
                   [sg.Text(f'{self.sum_number}件のうち、　{self.number}から{next_number}件を表示しています',
                            size=(40, 1), font=FONT_SIZE),
                    sg.Text('', size=(30, 1), font=FONT_SIZE, key='INPUT')],
                   ]

        return sg.Window('Game menu').Layout(layout)
