import base64
file = '/home/hd/Documents/Python/Django/personal_project/Django/smart-tools/media/the_blob'

with open('file.webm', 'wb') as f_vid:
    f_vid.write(base64.b64encode(file))