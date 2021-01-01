from instapy_cli import client

username = "yourusername"
password = "yourpassword"
image_path = 'docs/image-sample.jpg'
caption = 'Image Upload Example'

with client(username,password) as cli:
    cli.upload(image_path,caption)