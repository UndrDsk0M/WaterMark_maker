import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from picture.picture import watemarker


# -------------------------------- session info --------------------------------
api_hash = ""
api_id = 

bot_token = ""
# -------------------------------- session info --------------------------------

app = Client("Watermarkbot", api_hash=api_hash, api_id=api_id, bot_token=bot_token)

STEP = ""


# -------------------------------- Bot | start and functions --------------------------------
@app.on_message()
def echo(client, message):
    global STEP

    # -------------------------------- On start or cancel command --------------------------------
    if message.text in ["/start", "/cancel"]:
        STEP = "home"
        # -------------------------------- Set step and run function --------------------------------
        app.send_message(
            chat_id=message.chat.id,
            text=f"سلام  `{message.from_user.first_name}` به بات بنر ادیتور خوش اومدی",
            reply_to_message_id=message.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="آپلود بنر جدید📤", callback_data="uploadNewFile"
                        )
                    ]
                ]
            ),
        )

    # -------------------------------- UPLOAD STEP --------------------------------
    if STEP == "upload":
        # -------------------------------- Download input omage--------------------------------
        app.download_media(message, file_name="image.jpg")

        # -------------------------------- Send OK message --------------------------------
        app.send_message(
            chat_id=message.chat.id,
            reply_to_message_id=message.id,
            text=f"فایلتو ذخیره کردم الان تغییرات رو روش انجام میدم و برات میفرستم!",
        )

        # -------------------------------- Watermark Process --------------------------------
        watemarker(img_path="./downloads/image.jpg")

        # -------------------------------- Send watermarked image --------------------------------
        app.send_photo(chat_id=message.chat.id, photo="./resualt.png")

        # -------------------------------- Remove files --------------------------------
        os.remove("resualt.png")
        os.remove("./downloads/image.jpg")


# -------------------------------- button callbacks --------------------------------
@app.on_callback_query()
def answer(client, callback_query):
    global STEP
    query = callback_query

    # -------------------------------- On upload new file click --------------------------------
    if query.data == "uploadNewFile":
        STEP = "upload"
        app.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=query.message.id,
            text=f"حالا فایلتو برام بفرست تا تغییراتو روش انجام بدم",
        )


# -------------------------------- RUN FILE --------------------------------
app.run()


# -------------------------------- this project is used to add watermarks to images of CodeExplore telegram channel
# -------------------------------- bot developer : t.me/amiroim
# -------------------------------- watermark side : t.me/underdskm
# -------------------------------- thats it
# -------------------------------- go away
# -------------------------------- get lost
# -------------------------------- ayo get lost
# -------------------------------- go awwwwwwwway
