from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid
from LuciferMoringstar_Robot.database.autofilter_db import is_subscribed, get_file_details
from LuciferMoringstar_Robot.database._utils import get_size
from translation import LuciferMoringstar
from config import BUTTONS, FORCES_SUB, CUSTOM_FILE_CAPTION, START_MSG, DEV_NAME, bot_info, ADMINS


@LuciferMoringstar_Robot.on_callback_query()
async def cb_handler(client: LuciferMoringstar_Robot, query):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):


# ---------- 🔘 [ | 𝗚𝗥𝗢𝗨𝗣 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- #

        if query.data.startswith("nextgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"backgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴𝚂 {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🎗️ 𝙵𝙸𝙻𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙿𝙼 𝙲𝙷𝙴𝙲𝙺 🎗️", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"backgroup_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴𝚂 {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🎗️ 𝙵𝙸𝙻𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙿𝙼 𝙲𝙷𝙴𝙲𝙺 🎗️", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙽𝙴𝚇𝚃 𝙿𝙰𝙶𝙴", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴 {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🎗️ 𝙵𝙸𝙻𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙿𝙼 𝙲𝙷𝙴𝙲𝙺 🎗️", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"backgroup_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴 {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🎗️ 𝙵𝙸𝙻𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙿𝙼 𝙲𝙷𝙴𝙲𝙺 🎗️", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- 🔘 [ | 𝗕𝗢𝗧 𝗣𝗠 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- #


        elif query.data.startswith("nextbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"backbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴𝚂 {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"backbot_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴𝚂 {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙽𝙴𝚇𝚃 𝙿𝙰𝙶𝙴", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴𝚂 {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"backbot_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎭 𝙿𝙰𝙶𝙴𝚂 {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- 📁 [ | 𝗚𝗘𝗧 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data.startswith("lucifermoringstar_robot"):
            ident, file_id = query.data.split("#")
            files_ = await get_file_details(file_id)
            if not files_:
                return await query.answer('No such file exist.')
            files = files_[0]
            title = files.file_name
            size=get_size(files.file_size)
            f_caption=files.caption
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, file_name=title, file_size=size, file_caption=f_caption)
                except Exception as e:
                        print(e)
                f_caption=f_caption
            if f_caption is None:
                f_caption = LuciferMoringstar.FILE_CAPTIONS.format(mention=query.from_user.mention, title=title, size=size)
            
            try:
                if FORCES_SUB and not await is_subscribed(client, query):
                    await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                    return
                else:
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=file_id,
                        caption=f_caption
                        )
                    await query.answer('𝙷𝙴𝚈 𝙼𝚈 𝙵𝚁𝙸𝙴𝙽𝙳 𝙲𝙷𝙴𝙲𝙺 𝙿𝙼, 𝙸 𝙷𝙰𝚅𝙴 𝚂𝙴𝙽𝚃 𝙵𝙸𝙻𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙿𝙼.. ❤️❤️',show_alert = True)
            except UserIsBlocked:
                await query.answer('Unblock the bot mahn !',show_alert = True)
            except PeerIdInvalid:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
            except Exception as e:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")

# ---------- 📁 [ | 𝗣𝗠 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #

        elif query.data.startswith("pmfile"):
            if FORCES_SUB and not await is_subscribed(client, query):
                await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = LuciferMoringstar.FILE_CAPTIONS
                buttons = [[
                  InlineKeyboardButton('💡 𝗚𝗥𝗢𝗨𝗣 💡', url='https://t.me/ADHOLOKAMHD')
                  ]]                 
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


# ---------- 📁 [ | 𝗠𝗢𝗗𝗨𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data == "start":
            if query.from_user.id not in ADMINS: 
                buttons = [[
                 InlineKeyboardButton("✈️ ᗩᗪᗪ ᗰᗴ TO ᗩ ᑕᕼᗩT ᘜᖇOᑌᑭ ✈️", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("❤️ ᕼᗴᒪᑭ", callback_data="help"),
                 InlineKeyboardButton("👻 ᗩᗷOᑌT", callback_data="about") 
                 ],[
                 InlineKeyboardButton("💡 ᘜᖇOᑌᑭ", url="https://t.me/ADHOLOKAMHD"),
                 InlineKeyboardButton("💡 ᑕᕼᗩᑎᑎᗴᒪ", url="https://t.me/ADHOLOKAMHDCHANNEL")
                 ]]
            else:
                buttons = [[
                 InlineKeyboardButton("✈️ ᗩᗪᗪ ᗰᗴ TO ᗩ ᑕᕼᗩT ᘜᖇOᑌᑭ ✈️", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("❤️ ᕼᗴᒪᑭ", callback_data="bot_owner"),
                 InlineKeyboardButton("👻 ᗩᗷOᑌT", callback_data="about") 
                 ],[
                 InlineKeyboardButton("💡 ᘜᖇOᑌᑭ", url="https://t.me/ADHOLOKAMHD"),
                 InlineKeyboardButton("💡 ᑕᕼᗩᑎᑎᗴᒪ", url="https://t.me/ADHOLOKAMHDCHANNEL")
                 ]]               
            await query.message.edit(text=START_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "help":
            buttons = [[
              InlineKeyboardButton("🏡 ᕼOᗰᗴ", callback_data="start"),
              InlineKeyboardButton("👻 ᗩᗷOᑌT", callback_data="about")
              ]]               
            await query.message.edit(text=LuciferMoringstar.HELP_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "about":
            buttons = [[
             InlineKeyboardButton("🏡 ᕼOᗰᗴ", callback_data="start"),
             InlineKeyboardButton("ᑕᒪOՏᗴ", callback_data="close")
             ]]               
            await query.message.edit(text=LuciferMoringstar.ABOUT_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "bot_owner":
            buttons = [[
             InlineKeyboardButton('🏡 ᕼOᗰᗴ', callback_data="start"),
             InlineKeyboardButton('👻 ᗩᗷOᑌT', callback_data="about")
             ]]               
            await query.message.edit(text=LuciferMoringstar.PR0FESS0R_99.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "pages":
            await query.answer()

    else:
        await query.answer("Please Request",show_alert=True)




