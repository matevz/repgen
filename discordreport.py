import discord
import markdown
import re
import asyncio
from datetime import datetime, timezone
import os

def fetch_channel_messages(token, channel_id, date_start, date_end):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    messages = []

    @client.event
    async def on_ready():
        nonlocal messages
        try:
            start_datetime = datetime.combine(date_start, datetime.min.time()).replace(tzinfo=timezone.utc)
            end_datetime = datetime.combine(date_end, datetime.max.time()).replace(tzinfo=timezone.utc)

            channel = client.get_channel(channel_id)
            if not channel:
                channel = await client.fetch_channel(channel_id)

            async for msg in channel.history(limit=None, after=start_datetime, before=end_datetime):
                content = markdown.markdown(msg.content, extensions=['extra'])
                url_pattern = r'<(https?://[^\s>]+)>|(?<!\<)(https?://[^\s]+)'

                def replace_url(match):
                    if match.group(1):  # Discord format <url>
                        url = match.group(1)
                        return f'<a href="{url}" target="_blank">{url}</a>'
                    elif match.group(2):  # Regular URL
                        url = match.group(2)
                        return f'<a href="{url}" target="_blank">{url}</a>'

                content = re.sub(url_pattern, replace_url, content)
                if content.startswith('<p>') and content.endswith('</p>'):
                    content = content[3:-4]
                # Trim the message id <@&1002516039034208288> from the beginning of the content
                content = content.split(' ', 1)[1]

                messages.append(f"[{msg.created_at.strftime('%Y-%m-%d')}] {msg.author.name}: {content}")
        except Exception as e:
            print(f"Error fetching messages: {e}")
        finally:
            await client.close()

    client.run(token)

    return messages

# Main function to get chats
def get_chats(channel_id: int, date_start: datetime.date, date_end: datetime.date) -> str:
    if 'DISCORD_TOKEN' not in os.environ:
        print("Error: DISCORD_TOKEN env variable not defined")
        return ""

    token = os.environ["DISCORD_TOKEN"]

    chats = fetch_channel_messages(token, channel_id, date_start, date_end)
    return "<br/><br/>\n".join(chats)