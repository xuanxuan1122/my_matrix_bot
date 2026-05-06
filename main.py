import asyncio
import time
import importlib
from nio import AsyncClient, MatrixRoom, RoomMessageText

# ==============================
USER_ID    = ""
PASSWORD   = ""
HOMESERVER = ""
TARGET_ROOM_ID = ""
# ==============================

APP_START_TIMESTAMP = int(time.time())

client = AsyncClient(HOMESERVER, USER_ID)

async def handle_msg(room: MatrixRoom, event: RoomMessageText):
    
    # 判断
    if (room.room_id == TARGET_ROOM_ID) and (event.server_timestamp >= APP_START_TIMESTAMP):
        msg = event.body.strip()
        if msg.startswith(".bot"):
            print(f"命令：{msg}")
            
            import ret
            importlib.reload(ret)
            
            # 自动回复内容
            reply_text = ret.ret_message(msg)

            # 发送回复
            await client.room_send(
                room_id=TARGET_ROOM_ID,
                message_type="m.room.message",
                content={
                    "msgtype": "m.text",
                    "body": reply_text
                }
            )

async def main():
    await client.login(PASSWORD)
    print(">w< ", TARGET_ROOM_ID)
    client.add_event_callback(handle_msg, RoomMessageText)
    await client.sync_forever(timeout=30000)

if __name__ == "__main__":
    asyncio.run(main())
