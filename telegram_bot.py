from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from ir_system import run_query
import config

async def recipe_search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args)
    results = run_query(query)
    response = "\n".join(results) if results else "No recipes found."
    await update.message.reply_text(response)

def main():
    app = Application.builder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("recipe", recipe_search))
    app.run_polling()

if __name__ == '__main__':
    main()
