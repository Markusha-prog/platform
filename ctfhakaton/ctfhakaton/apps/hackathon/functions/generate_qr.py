import qrcode  # Модуль для создания QR-кодов
from docx import Document  # Модуль для открытия текстового файла в формате (docx)
from docx.shared import Inches
import secrets
import string
import numpy as np
import cv2
from ..models import File_QR

def generate_qr(data):
    data = int(data) + 1
    try:
        letters_and_digits = string.ascii_letters + string.digits
        crypt_rand_string = ''.join(secrets.choice(
            letters_and_digits) for i in range(8))
        filename = (f'Hackathon_{crypt_rand_string}')  # Название получаемого файла с QR-кодом
        document = Document()

        for a in range(data):
            img = qrcode.make(a)  # Создаем QR
            img.save(filename)  # Сохраняем QR
            image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
            position = (1, 30)
            cv2.putText(
                image,
                str(a),
                position,
                cv2.FONT_HERSHEY_SIMPLEX,
                1,(0, 0, 0, 0),
                4)
            cv2.imwrite(f'media/qr_code/qr_{filename}.png', image)
            document.add_picture(f'media/qr_code/qr_{filename}.png', width=Inches(1.35), height=Inches(1.35))



        document.save(f'media/qr_code/{filename}.docx')

        object_m = File_QR()
        object_m.file = f'qr_code/{filename}.docx'
        object_m.save()

        return object_m.id
    except:
        return False