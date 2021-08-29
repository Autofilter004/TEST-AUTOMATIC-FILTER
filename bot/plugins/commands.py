#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL
db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = FORCESUB_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text=""" <b> ⚠️ YOU ARE NOT SUBSCRIBED OUR CHANNEL⚠️

Join on our channel to get movies ✅


⚠️താങ്കൾ ഞങ്ങളുടെ ചാനൽ സബ്സ്ക്രൈബ് ചെയ്തിട്ട് ഇല്ല ! ⚠️


ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്യതാൽ താങ്കൾക്ക് movies കിട്ടുന്നത് ആണ് ✅

⬇️Channel link⬇️ </b>""",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="⚡ Join My Channel⚡️", url=f"{update_channel}")]
              ])
            )
            return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👨‍🔬 𝗢𝗡𝗪𝗘𝗥 👨‍🔬', url="https://t.me/mhd_thanzeer"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👨‍🔬 𝗢𝗡𝗪𝗘𝗥 👨‍🔬', url="https://t.me/mhd_thanzeer"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👨‍🔬 𝗢𝗡𝗪𝗘𝗥 👨‍🔬', url="https://t.me/mhd_thanzeer"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('👨‍🔬𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥👨‍🔬', url='https://t.me/mhd_thanzeer'),
        InlineKeyboardButton('💥𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘💥', url ='https://telegra.ph/file/587de9bdd9486b806aeba.jpg')
    ],[
        InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏🛠', url='https://t.me/wolfpackmedia')
    ],[
        InlineKeyboardButton('💡ＨＥＬＰ💡', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(

        chat_id=update.chat.id,

        text=Translation.HELP_TEXT,

        reply_markup=reply_markup,

        parse_mode="html",

        reply_to_message_id=update.message_id

    )
    
    await bot.send_photo(

        chat_id=update.chat.id,

        photo = 'https://telegra.ph/file/f48f62bc9d3194c429a85.jpg',

        caption=Translation.START_TEXT.format(

                update.from_user.first_name),

        parse_mode="html",

        reply_to_message_id=update.message_id

    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
