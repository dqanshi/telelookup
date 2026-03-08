from pyrogram import Client, filters
from config import *

from db import search_database
from csv_engine import search_csv
from formatter import format_results


app = Client(
    "telelookup",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=16
)


@app.on_message(filters.command("start"))
async def start(_, message):

    await message.reply_text(
        "🔎 TeleLookup OSINT Bot\n\n"
        "Use:\n"
        "`/info username`\n"
        "`/info userid`\n"
        "`/info phone`"
    )


@app.on_message(filters.command("info"))
async def info(_, message):

    # OWNER CHECK
    if message.from_user.id not in OWNER_IDS:
        await message.reply_text("❌ Unauthorized")
        return

    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        await message.reply_text("Usage:\n`/info query`")
        return

    query = parts[1]

    msg = await message.reply_text("🔎 Searching...")

    results = []

    # Search ClickHouse database
    results.extend(search_database(query))

    # Search CSV dataset
    results.extend(search_csv(query))

    text = format_results(results)

    await msg.edit_text(text)


print("TeleLookup Started")

app.run()
