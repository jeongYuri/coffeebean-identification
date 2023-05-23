from flask import Flask , render_template,request,url_for,send_from_directory,session
from werkzeug.utils import secure_filename
import itertools
import imageio
import os
import cv2
import numpy as np
from flask import jsonify
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten,GlobalMaxPooling2D,GlobalMaxPooling2D
from keras.applications import VGG16,ResNet50
import keras.utils as image
from imutils import paths



app = Flask(__name__)
app.secret_key="super secret key"
app.config['UPLOAD_FOLDER'] ='경로'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


@app.route("/predict",methods=['GET','POST'])
def predict():
  if request.method =='POST':
    file=request.files['image']
    if not file: return render_template('index.html', label="No Files") 
    #Path='C:/Users/dydrk/aii_project/venvv/static/images/'+str(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename)) #저장시킨 파일..
    model=keras.models.load_model('경로/my_cofee.h5')  
    Path=(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
    
    img = image.load_img(Path) #저장시킨 파일 불러오기
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0) 
    images = np.vstack([img])/255
    classes = model.predict(images, batch_size=32)
    clas = list(itertools.chain(*classes))
    print(clas)
    if clas[0]>=max(clas):
      coffee='green'
    elif clas[1]>=max(clas):
      coffee ='light'
    elif clas[2]>=max(clas):
      coffee='medium'
    elif clas[3]>=max(clas):
       coffee='dark'
             
    return render_template('index.html', data=coffee)

   
@app.route('/') #파이썬 데코레이터 문법 =라우팅
def index():
    return render_template("index.html")
    

if __name__ == '__main__':
    #model = keras.models.load_model('my_cofee.h5')
    print(("*Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    app.run(debug=True,host="0.0.0.0",port=8001)





#@app.route('/user/<user_name>/<int:user_id>')
#def user(user_name, user_id):
  #  return f'Hello,{user_name}({user_id})!'
