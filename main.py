from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio
from default_keyboard import main_menu, course_menu

API_TOKEN = "6405919911:AAFzc45ERQNnnCI9hfb59gYkMFjjT8fRVUU"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
image_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz0fj6e2bltOwszWk-IbO4hLqPd8okt2zVrQ&s"
company_image = "https://avatars.mds.yandex.net/get-altay/11873493/2a0000018d7cd4ff0b0f0ded0574df9b24bd/L_height"

mentor_images = {"Bunyod Naimov": "https://framerusercontent.com/images/kXVV58GAu8fRErxTCCErYzk0i4.webp",
                 "Shohruh Abdurahmon": "https://framerusercontent.com/images/YqHAVasnW1eTKymnTB5dqiUMA.webp",
                 "Muhammadaziz To'lqinboyev": "https://framerusercontent.com/images/QzA0DHsPdTOxQ62dFyWslK4mT1Y.webp",
                 "Daler Badiyev": "https://framerusercontent.com/images/KNPILEJeDuGPQhkVMZY35hsyltg.webp",
                 "Asilbek Mamadaliyev": "https://framerusercontent.com/images/YxvMJWtMDSRGPD2IabC9CQdlBiU.webp",
                 "Habibulloh Nuriddin": "https://framerusercontent.com/images/rTCJHxT1yCe2LsYwsfZFrrBDds.webp",
                 "Asliddin Abdullayev": "https://framerusercontent.com/images/s6j0WzUvfog8RJHmnTeOurwR4.webp"}

python_image = "https://framerusercontent.com/images/842SsoUmQMhdORw9rDC5e1EyO1U.png?scale-down-to=512"
robototexnika_image = "https://framerusercontent.com/images/kx3nFOZSgvqHlhAejBBHdTNyI.png"
scratch_image = "https://framerusercontent.com/images/GbPBaWtopR178MP8DQSZzc8h8.png?scale-down-to=1024"
frontend_image = "https://framerusercontent.com/images/kkNJyRECmT2kslWfE5JM8lluQg.png?scale-down-to=512"

address_image = "https://media.istockphoto.com/id/1409911141/vector/red-map-pin-vector-icon-clipart-location-symbol.jpg?s=612x612&w=0&k=20&c=zIyeXjdLDZzqO9y69ZfdpQRjscaRGCCMgSaBcJxeVk0="


@dp.message(Command("start"))
async def menu_handler(message: types.Message):
    await message.answer_photo(photo=image_logo,
                               caption="Assalamu alaykum PDP Junior botiga xush kelibsiz11",
                               reply_markup=main_menu())


@dp.message(F.text == "🏢 Kompaniya haqida")
async def menu_handler(message: types.Message):
    await message.answer_photo(photo=company_image,
                               caption="""8 yillik tajribaga, 2000 mingdan ortiq o'quvchilar va
                               tarjibali mentorlar ega""")


@dp.message(F.text == "🧑‍🏫 Bizning Mentorlar")
async def menu_handler(message: types.Message):
    for name, image in mentor_images.items():
        await message.answer_photo(photo=image,
                                   caption=f"Mentor: {name}")


@dp.message(F.text == "🎓 Kurslarimiz")
async def menu_handler(message: types.Message):
    await message.answer(text="Bizning kurslarimiz",
                         reply_markup=course_menu())


@dp.message(F.text == "Python")
async def menu_handler(message: types.Message):
    await message.answer_photo(photo=python_image,
                               caption="""Python - Mantiqiy fikrlash va dasturlash asoslari""",
                               reply_markup=course_menu())


@dp.message(F.text == "Fronted")
async def menu_handler(message: types.Message):
    await message.answer_photo(photo=frontend_image,
                               caption="""Frontend - Veb dasturlashda dastalabki qadamlar""",
                               reply_markup=course_menu())


@dp.message(F.text == "Robototexnika")
async def menu_handler(message: types.Message):
    await message.answer_photo(photo=robototexnika_image,
                               caption="""Robototexnika - Texnik ko’nikmalar va amaliy ishlar""",
                               reply_markup=course_menu())


@dp.message(F.text == "Scratch")
async def menu_handler(message: types.Message):
    await message.answer_photo(photo=scratch_image,
                               caption="""Scratch - Vizual dasturlash orqali kreativ fikrlash""",
                               reply_markup=course_menu())


@dp.message(F.text == "🔙 back")
async def menu_handler(message: types.Message):
    await message.answer(text="Ortga",
                         reply_markup=main_menu())


@dp.message(F.text == "📞 Kontaktlar/ Manzil")
async def menu_handler(message: types.Message):
    await message.answer_photo(photo=address_image,
                               caption="""📞 -> +998 78 777-74-77
📍 -> Toshkent shahri, Shayxontohur tum,
Chorsu, Xadra, Zarqaynar 3-uy""",
                               reply_markup=main_menu())


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
