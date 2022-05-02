from pyrogram import filters
from LuciferMoringstar_Robot.helpers.admin_check import admin_check


async def admin_filter_f(filt, client, message):
    return (
        # t, lt, fl 2013
        not message.edit_date
        and await admin_check(message)
    )


admin_fliter = filters.create(func=admin_filter_f, name="AdminFilter")
