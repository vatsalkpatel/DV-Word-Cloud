import PySimpleGUI as sg
import os
import pdfparser

from main import Display

# Constant String
PROGRAM_NAME = "Tag Cloud"
LABEL_TEXT_FILE_RADIO = "Text File"
LABEL_PDF_FILE_RADIO = "PDF File"
LABEL_TEXTBOX_RADIO = "TextBOX"
LABEL_FILE = "File"
KEY_TEXT_FILE_RADIO = "tFileRadio"
KEY_PDF_FILE_RADIO = "pFileRadio"
KEY_TEXTBOX_RADIO = "textBoxRadio"
KEY_FILE_PATH = "fileData"
KEY_BROWSE_BUTTON = "browseButton"
KEY_TEXTBOX = "textboxData"
KEY_GO_BUTTON = "Go"
KEY_EXIT_BUTTON = "Exit"
HEADER_SELECT_IN_TYPE = "Select Input type"
EMPTY_STRING = ""
STRING_PDF_FILE = "PDF File"
STRING_TEXT_FILE = "TEXT File"
EXTENSION_PDF = ".pdf"
EXTENSION_TXT = ".txt"


def fetchData():
    layout = [
        [
            sg.Text(HEADER_SELECT_IN_TYPE)
        ],
        [
            sg.Radio(LABEL_TEXT_FILE_RADIO, 1, enable_events=True, key=KEY_TEXT_FILE_RADIO),
            sg.Radio(LABEL_PDF_FILE_RADIO, 1, enable_events=True, key=KEY_PDF_FILE_RADIO),
            sg.Radio(LABEL_TEXTBOX_RADIO, 1, default=True, enable_events=True, key=KEY_TEXTBOX_RADIO)
        ],
        [
            sg.Text(LABEL_FILE),
            sg.In(size=(100, 1), disabled=True, enable_events=True, key=KEY_FILE_PATH),
            sg.FileBrowse(disabled=True, key=KEY_BROWSE_BUTTON)
        ],
        [
            sg.Multiline(size=(120, 30), focus=True, disabled=False, key=KEY_TEXTBOX)
        ],
        [
            sg.Button(KEY_GO_BUTTON), sg.Button(KEY_EXIT_BUTTON)
        ]
    ]

    window = sg.Window(PROGRAM_NAME, layout)

    while True:
        event, values = window.read()
        if event == KEY_EXIT_BUTTON or event == sg.WIN_CLOSED:
            break
        if event == KEY_TEXT_FILE_RADIO:
            window.FindElement(KEY_BROWSE_BUTTON).FileTypes = ((STRING_TEXT_FILE, EXTENSION_TXT),)
            window[KEY_BROWSE_BUTTON].Update(disabled=False)
            window[KEY_TEXTBOX].Update(disabled=True, value=EMPTY_STRING)
            window[KEY_FILE_PATH].Update(disabled=False, value=EMPTY_STRING)
        if event == KEY_PDF_FILE_RADIO:
            window.FindElement(KEY_BROWSE_BUTTON).FileTypes = ((STRING_PDF_FILE, EXTENSION_PDF),)
            window[KEY_BROWSE_BUTTON].Update(disabled=False)
            window[KEY_TEXTBOX].Update(disabled=True, value=EMPTY_STRING)
            window[KEY_FILE_PATH].Update(disabled=False, value=EMPTY_STRING)
        if event == KEY_TEXTBOX_RADIO:
            window[KEY_BROWSE_BUTTON].Update(disabled=True)
            window[KEY_FILE_PATH].Update(disabled=True, value=EMPTY_STRING)
            window[KEY_TEXTBOX].Update(disabled=False)
        if event == KEY_GO_BUTTON:
            filePathValue = values[KEY_FILE_PATH]
            if filePathValue:
                if os.path.exists(filePathValue):
                    if values[KEY_TEXT_FILE_RADIO]:
                        if filePathValue[-4:] == EXTENSION_TXT:
                            f = open(filePathValue, "r")
                            text = f.read()
                            obj = Display(text)
                            obj.webVersion()
                            #main.Display.__init__(text)
                    elif values[KEY_PDF_FILE_RADIO]:
                        if filePathValue[-4:] == EXTENSION_PDF:
                            text = pdfparser.get_string_from_pdf(filePathValue)
                            obj = Display(text)
                            obj.webVersion()
                            #return text
            elif values[KEY_TEXTBOX]:
                text = values[KEY_TEXTBOX]
                obj = Display(text)
                obj.webVersion()
                #return text
            else:
                pass

    window.close()

fetchData()