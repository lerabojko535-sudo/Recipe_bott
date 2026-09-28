from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
import os


TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🍳 Сніданок", callback_data="breakfast")],
        [InlineKeyboardButton("🍲 Обід", callback_data="lunch")],
        [InlineKeyboardButton("🌙 Вечеря", callback_data="dinner")]
    ]

    await update.message.reply_text(
        "Привіт! ❤️\n"
        "Я допоможу тобі вирішити, що сьогодні приготувати 😋\n\n"
        "Обери прийом їжі:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    recipes = {
        "breakfast":
            "🍳 Сніданок\n\n"
            "🥞 Сирники\n"
            "🍳 Омлет\n"
            "🥪 Гарячі бутерброди\n"
            "🥞 Млинці",

        "lunch":
            "🍲 Обід\n\n"
            "🍗 Курка з картоплею\n"
            "🥣 Борщ\n"
            "🫔 Хачапурі\n"
            "🥣 Окрошка\n"
            "🍕 Піца\n"
            "🍰 Печінковий торт\n"
            "🫜 Шуба\n"
            "🥟 Пельмені\n"
            "🥩 Запечене м'ясо\n"
            "🍛 Гречка по-купецьки\n"
            "🍛 Плов\n"
            "🥔 Толченка\n"
            "🥣 Лазанья\n"
            "🍗 Крильця\n"
            "🥘 Жарке\n"
            "🫑 Фарширований перець\n"
            "🥩 Тефтельки\n"
            "🍄 Підлива з грибами\n"
            "🍝 Макарони з м'ясом\n"
            "🥧 Заливний пиріг з рибою\n"
            "🍗 Підлива\n"
            "🍊 М'ясо з апельсинами\n"
            "🥧 Галета\n"
            "🥖 Пиріжки\n"
            "🥐 Круасани\n"
            "😛 Тещин язик\n"
            "❤️ Шашлик з сердечок\n"
            "🌭 Хот-доги\n"
            "🥟 Вареники\n"
            "🥣 Суп з фрикадельками",

        "dinner":
            "🌙 Вечеря\n\n"
            "🍗 Запечена курка\n"
            "🥗 Салат грецький\n"
            "🥗 Салат з куркою\n"
            "🥟 Пельмені\n"
            "🍗 М'ясо з цитрусом\n"
            "🍄 Жульєн\n"
            "🥧 Кіш з куркою та грибами\n"
            "🍝 Карбонара\n"
            "🍜 Фунчоза\n"
            "🍳 Шакшука\n"
            "🪹 Гнізда\n"
            "🍗 Рублені котлети\n"
            "🥩 Медальйони у вині\n"
            "🍞 Грінки з начинками\n"
            "Еклери\n"
            "Булочки\n"
            "Медовик\n"
            "Бісквіт\n"
            "Шарлотка\n"
            "Шишки\n"
            "🍝 Паста з сиром"
    }

    await query.edit_message_text(recipes[query.data])


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Бот запущений!")
    app.run_polling()


if __name__ == "__main__":
    main()
