from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    button = KeyboardButton(text="🏢 Kompaniya haqida")
    button2 = KeyboardButton(text="🧑‍🏫 Bizning Mentorlar")
    button3 = KeyboardButton(text="🎓 Kurslarimiz")
    button4 = KeyboardButton(text="📞 Kontaktlar/ Manzil")
    button5 = KeyboardButton(text="🇺🇿/🇷🇺 Til")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button4, button5]
        ],
        resize_keyboard=True
    )
    return rkm


def course_menu():
    button = KeyboardButton(text="Python")
    button2 = KeyboardButton(text="Fronted")
    button3 = KeyboardButton(text="Robototexnika")
    button4 = KeyboardButton(text="Scratch")
    button5 = KeyboardButton(text="🔙 back")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5],
        ],
        resize_keyboard=True
    )
    return rkm
