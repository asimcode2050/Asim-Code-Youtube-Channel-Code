/*
WhatsApp API client
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
*/
const qrcode = require('qrcode-terminal');

const { Client } = require('whatsapp-web.js');
const client = new Client();
client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
});
client.on('ready', () => {
    console.log('Client is ready!');
});
client.initialize();
