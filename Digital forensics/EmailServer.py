import asyncio
from aiosmtpd.controller import Controller

class CustomSMTPHandler:
    async def handle_DATA(self,server,session, envelope):
        print('Message from: ',envelope.mail_from)
        print('Message for: ',envelope.rcpt_tos)
        print('Message data:\n ',envelope.content.decode('utf8',errors='replace'))
        return '250 Message accepted for deliver'
    

async def main():
    handler = CustomSMTPHandler()
    controller = Controller(handler, port=1025)
    controller.start()
    print('SMTP Server running on localhost:1025...')

    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()

if __name__ == '__main__':
    asyncio.run(main())


        
