from CoinCollector import CoinCollector
from DataProcessor import DataProcessor

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )

TOKEN = 'xxxxxxxxxx'
COINS = ['bitcoin', 'ethereum', 'solana', 'dogecoin']
FIAT = ['brl']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '👋 Olá, eu sou o Cypto Pip! Use /preços para ver as cotações.'
    )

async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '🤖 Buscando e processando dados da CoinGecko, aguarde...'
    )

    collector = CoinCollector(COINS, FIAT)
    brute_data = collector.fetch_data()
    if not brute_data:
        await update.message.reply_text('❌ Falha ao buscar dados da API. Motivo: Conexão ou API indisponível.')
        return

    processor = DataProcessor(brute_data)
    df_final = processor.process_and_analysis()

    if df_final.empty:
        await update.message.reply_text('❌ Os dados processados estão vazios.')
        return

    message = '📊 **Cotaçoes Atuais**\n\n'
    for index, row in df_final.iterrows():
        symbol = 'R$' if row['symbol'].upper() == 'BRL' else '$'

        message += (
            f'🔸 **{row['name']}** ({row['symbol'].upper()}):\n'
            f'Preço: {symbol} {row['preço']:,.2f}\n'
            f'Variação 24h: {row['status_variacao']}\n'
            '-------------------------------\n'
        )

    await update.message.reply_text(
        message,
        parse_mode= 'Markdown'
    )
def main() -> None:
    print('Iniciando Bot. Pressione Ctrl + C para finalizar...')

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('precos', prices))
    application.run_polling(poll_interval=1.0)

if __name__ == '__main__':
    main()

