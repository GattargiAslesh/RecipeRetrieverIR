from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from search_recipes import search_recipes

async def recipe_search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args)
    results = search_recipes(query)
    if results:
        response = "\n".join([f"Recipe ID: {res['id']}, Ingredients: {', '.join(res['ingredients'])}" for res in results])
    else:
        response = "No matching recipes found."
    await update.message.reply_text(response)

def main():
    app = Application.builder().token("<<YOUR TELEGRAM BOT TOKEN>>").build()
    app.add_handler(CommandHandler("recipe", recipe_search))
    app.run_polling()

if __name__ == '__main__':
    main()
