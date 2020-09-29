from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import request
from App import app
import os,os.path

from PIL import Image as Image
import numpy as np

# salvando com mesmo nome o arquivo é substituido
digitalBd = ''

def AuthFinger(fingerUser):
    image = request.files['image']
    global digitalBd
    
    digitalBd = os.path.join(app.config['UPLOAD_FOLDER'],fingerUser)
    
    return fingerstandard(image)

    # Função para redimensionamento

def fingerstandard(digitalUpload):
    finger1 = Image.open(digitalUpload).resize((800,800)).convert("L")
    finger_array = np.array(finger1)
    result = check_finger(finger_array)
    
    return result
    
# Função para normalizar a impressão teste
def check_finger(array):
    normalizedArray = (((array - array.min())/(array.max() - array.min())))
    global digitalBd
    result2 = mse(normalizedArray, digitalBd)
    return result2
    
def mse(array, imageBd):  
    imagem1 = Image.open(imageBd).resize((800,800)).convert("L")
    matriz1 = np.array(imagem1)
    finger_normalized = (((matriz1 - matriz1.min())/(matriz1.max() - matriz1.min())))
    
    # Array = digital do usuário 
    # finger_nomralized = arquivo de digitais
    result3 = ((array - finger_normalized) ** 2)
    
    # Com o array normalizado ficou mais claro se o acesso será permitido ou não, pois
    # se a digital for a mesma o resultado será zero, caso contrario sera um erro de quase 30% aproximadamente
    if result3.mean() <= 0.03:
        print(result3.mean())
        return True
    else:
        print(result3.mean())
        return False


def Register():
    image = request.files['image']
    # os.path pega o caminho absoluto para a pasta
    # permanece o nome original da imagem
    # filename = secure_filename(image.filename.rsplit('.', 1)[0])
    folder = app.config['UPLOAD_FOLDER']
    filename = 'image'
    ext = '.'+image.filename.rsplit('.', 1)[1]
    qtdArchives = str(len(os.listdir('Images')))

    print(filename)
    imageName = filename + qtdArchives + ext
    image.save(os.path.join(folder , imageName))
    return imageName