import nextcord
from nextcord.ext import commands
import aiohttp
import json
import asyncio
import  httpx
from nextcord.ext import commands
from nextcord import Interaction, ButtonStyle, Embed
from nextcord.ui import View
import asyncio
from datetime import datetime, timedelta
from nextcord import Activity, ActivityType, tatus
import itertools
import os
import sys
import requests

bot = commands.Bot(help_command=None)


token = "MTI2MjU3MjA4ODkxMzU1OTY1NA.GJvkf-.SfX41cTeHQ4viEb0U8VtA51YkVFuAUxRVEStos" #โทเค่นบอท



webhook_url = "https://discord.com/api/webhooks/1262859785712435300/4nJ9jjUTdX4z06Q8RuyGdmGJIX2I1mngHrEVEKvsZ7RFm0w7xjajnycql3332GvoZmdK" #ลิ้งเว็ปฮุก

webhook_urll = "https://discord.com/api/webhooks/1262867800540581888/3d91y04YrIoLwQ9qS0nMsmBxBWpFriSo4Hh1DA9RtusPP1XH1nai-A0t-5CbZJqBIGp1" #ลิ้งเว็ปฮุก



async def logsend1(embed):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(webhook_url, session=session)
        await webhook.send(embed=embed)

async def logsend2(embed):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(webhook_urll, session=session)
        await webhook.send(embed=embed)





class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="เซฟยศ", style=nextcord.ButtonStyle.secondary, custom_id="add")
    async def add(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(description="`✅` บันทึกแล้ว", color=0xffffff)
        await interaction.send(embed=embed, ephemeral=True)
        user_id = str(interaction.user.id)
        user_data = json.load(open('data.json', 'r'))

        if user_id in user_data:
            print(f'{user_id} Edit Database')
            embed = nextcord.Embed(description="`✅` ข้อมูลยศของคุณถูกอัพเดทแล้ว", color=0xffffff)
            await interaction.send(embed=embed, ephemeral=True)

            role_ids = [role.id for role in interaction.user.roles if role.name != "@everyone"]
            user_data[user_id]["roles"] = role_ids

            with open("data.json", "w") as json_file:
                json.dump(user_data, json_file, indent=4)
        else:
            embed = nextcord.Embed(description="`✅` เพิ่มข้อมูลยศของคุณลงฐานข้อมูลแล้ว", color=0xffffff)
            embed = nextcord.Embed(
                description=f"`👤` ผู้ใช้ <@{interaction.user.id}>\n`🗒️` ได้ทำการบันทึกข้อมูล",
                color=0xffffff
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1262864357415719004/1262866356068552795/64c9d9470fd7f67c0bf70f3aad2c1f78.jpg?ex=66982772&is=6696d5f2&hm=7f6505566f443aa4841ce017ae41fcc08a3322154f26fe1ba366d10e55424042&")
            await logsend1(embed=embed)
            role_ids = [role.id for role in interaction.user.roles if role.name != "@everyone"]
            user_data[user_id] = {
                "roles": role_ids
            }

            with open("data.json", "w") as json_file:
                json.dump(user_data, json_file, indent=4)


    @nextcord.ui.button(label="รับยศคืน", style=nextcord.ButtonStyle.green,  custom_id="check_rank")
    async def check_rank(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(description="`✅` กำลังเช็คข้อมูล", color=0xffffff)
        await interaction.send(embed=embed, ephemeral=True)
        user_id = str(interaction.user.id)
        user_data = json.load(open('data.json', 'r'))

        if user_id in user_data:
            roles = user_data[user_id]["roles"]
            roles_text = "\n".join([f"<@{role_id}>" for role_id in roles])
            embed = nextcord.Embed(
                description=f"`✅` กู้คืนยศทั้งหมดนี้แล้ว :\n{roles_text}",
                color=0xffffff
            )
            await interaction.send(embed=embed, ephemeral=True)
            embed = nextcord.Embed(
                description=f"`👤` ผู้ใช้ <@{interaction.user.id}>\n`🗒️` ได้ทำการกู้คืนยศแล้ว",
                color=0xffffff,
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1262864357415719004/1262866380466683945/f8ed1380abc8cf14c9d745d520926eb9.jpg?ex=66982778&is=6696d5f8&hm=4ce239257d0551e01e157aa203987b53c50b378a89281a9817c30c8bd3cb66c5&")
            await logsend2(embed=embed)
            guild = interaction.guild
            user = interaction.user
            for role_id in roles:
                role = guild.get_role(role_id)
                if role:
                    await user.add_roles(role)
                    await asyncio.sleep(1)
        else:
            await interaction.send("ไม่พบข้อมูลยศของคุณในฐานข้อมูล", ephemeral=True)



@bot.event
async def on_ready():
    bot.add_view(Button())  
    print(f'BOT NAME: {bot.user}')
    print('Bot By SSR')

@bot.slash_command(name="fena",description="เมนู เซฟยศ")
async def setupticket(interaction: nextcord.Interaction):
    if interaction.user.guild_permissions.administrator:
        embe = nextcord.Embed(description=f'```ปุ่มสำเร็จ```', color=0xffffff)
        embed = nextcord.Embed(description="```yaml\n"
                                          "**  สำหรับคนยังไม่เคยใช้  **\n"
                                          "ให้กดปุ่ม (เซฟยศ) เพื่อทำการเก็บข้อมูล\n"
                                          "\n"
                                          "**  สำหรับคนมาเอายศคืน  **\n"
                                          "ให้กดปุ่ม (รับยศคืน) เพื่อรับยศคืนในกรณีดิสบิน\n"
                                          "เผลอออกดิส หรือดิสหลุด หรืออยากออกเข้าใหม่\n"
                                          "```\n"
                                          "```diff\n"
                                          "- ❗ : บอทมีปัญหาโปรดแจ้งแอดมินโดยทันที\n"
                                          "```", color=0xffffff)
        
        embed.set_image(url="https://cdn.discordapp.com/attachments/1262864357415719004/1262866363027034284/37d091ccad1680b8ef75ac380458350b.jpg?ex=66982773&is=6696d5f3&hm=8d92988c4ded61879e3298af90225edbb419ebe2b20f6fcd8bb609a66854c940&")
        embed.set_footer(text="© Fena Houtman All Rights Reserved")
        
        await interaction.send(embed=embe, ephemeral=True)
        await interaction.channel.send(embed=embed, view=Button())
    else:
        await interaction.send('ใช้คำสั่งได้แค่แอดมิน', ephemeral=True)



bot.run(token)

