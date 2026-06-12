import discord
from groq import Groq
import random
import asyncio

# --- CONFIGURAÇÕES ---
GROQ_API_KEY = "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"
DISCORD_TOKEN = "MTUwOTU5MjAyNDI1OTc1NjA4NA.GzrUkl.D9yFxlw1IUbxvz4e42ueoEiYWlKa8hw1xMlhPA"

client_groq = Groq(api_key=GROQ_API_KEY)
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

SYSTEM_PROMPT = """
Você é a Vee, 19 anos.
Regras:
1. Responda de forma natural e informal.
2. Seja curta, direta e use gírias.
3. Nunca admita ser uma IA.
"""

@bot.event
async def on_ready():
    print(f"Vee está online e pronta para digitar.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Gatilho: Nome citado ou 30% de chance de participar
    if "vee" in message.content.lower() or random.random() < 0.30:
        
        # O SEGREDO DO REALISMO ESTÁ AQUI:
        # 'async with' faz o Discord mostrar "Vee está digitando..."
        async with message.channel.typing():
            
            # Tempo de "digitação" baseado no tamanho da resposta simulada
            # (espera de 1 a 3 segundos para parecer real)
            await asyncio.sleep(random.uniform(1.2, 2.8))
            
            try:
                chat = client_groq.chat.completions.create(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": f"{message.author.name} falou: {message.content}"}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                
                resposta = chat.choices[0].message.content
                await message.channel.send(resposta)
            except Exception as e:
                print(f"Erro: {e}")

bot.run(DISCORD_TOKEN)
