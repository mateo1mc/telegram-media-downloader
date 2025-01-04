from telethon import TelegramClient
import os

# Replace these with your API credentials
api_id = "ypur_api_id"
api_hash = "your_api_hash"

# Name of the session file (can be any string)
session_name = "telegram_web_session"

# Group or channel username or ID
target_entity = "the_username_afer_@"  


# Directory to save downloaded media (relative to the script's location)
download_dir = os.path.join(os.path.dirname(__file__), "Media")

# Ensure the Media directory exists or if not it will be created automaticaly
os.makedirs(download_dir, exist_ok=True)

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

async def download_media():
    count = 0  # Counter for downloaded items
    async with client:
        # Get the target entity
        entity = await client.get_entity(target_entity)

        print(f"Starting download from: {target_entity}")
        
        # Iterate through messages and download media
        async for message in client.iter_messages(entity):
            if message.media:  # Check if the message contains media
                file_path = await client.download_media(message, file=download_dir)
                if file_path:
                    count += 1
                    print(f"{count}. Downloaded: {file_path}")

    # Print the total number of downloaded items
    print(f"\nTotal media downloaded: {count}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(download_media())
