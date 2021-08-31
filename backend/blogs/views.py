from django.shortcuts import render
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import keras
import tensorflow as tf
from django.http import HttpResponse

# Create your views here.
model = load_model('model/DenseNet121.h5')

def img_predict(request):
    IMG_SIZE = 224
    file = ['test/NORMAL-1017237-1.jpeg', 'test/CNV-1016042-1.jpeg', 'test/DME-1081406-1.jpeg', 'test/DRUSEN-1083159-1.jpeg']
    res = ''
    for i in range(len(file)):
        image = load_img(file[i],target_size=(IMG_SIZE,IMG_SIZE))
        data = img_to_array(image)
        samples = np.expand_dims(data, 0)
        datagen = ImageDataGenerator(samplewise_center=True, 
                                samplewise_std_normalization=True, 
                                horizontal_flip = True, 
                                vertical_flip = False, 
                                height_shift_range= 0.05, 
                                width_shift_range=0.1, 
                                rotation_range=15, 
                                zoom_range=0.15,
                                validation_split=0.2)
        datagenflow = datagen.flow(samples,batch_size=1)

        predicted = model.predict(datagenflow)[0] * 100
        # predicted = [round(int(p),3) for p in predicted[0]]
        # pred_class = np.argmax(predicted)
        # print(predicted[0])
    
        res += f"<h2>file : {file[i][5:]}<h2><h5>CNV : {predicted[0]} %<h5><h5>DME : {predicted[1]} %<h5><h5>DRUSEN : {predicted[2]} %<h5><h5>NORMAL : {predicted[3]} %<h5>"
    return HttpResponse(res)

def get_statistic(request):
    return HttpResponse()

def login(request):
    return HttpResponse()

def patients(request):
    return HttpResponse()

def patient_information(request):
    return HttpResponse()

def patients_risk(request):
    return HttpResponse()

def patients_normal(request):
    return HttpResponse()

def medtech_submit(request):
    return HttpResponse()

def undiagnosed(request):
    return HttpResponse()

def diagnosed(request):
    return HttpResponse()

def medical_submit(request):
    return HttpResponse()

def patient_add(request):
    return HttpResponse()

def patient_edit(request):
    return HttpResponse()

def patient_remove(request):
    return HttpResponse()

