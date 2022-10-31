import json,pickle
import numpy as np
try:
    import config
except:
    pass

class iris():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.sep_len=SepalLengthCm
        self.sep_wid=SepalWidthCm
        self.pet_len=PetalLengthCm
        self.pet_wid=PetalWidthCm

    def load_model(self):
        try:

            with open(config.MODEL_PATH,"rb") as f:
                self.knnf=pickle.load(f)
        
            with open(config.JSON_PATH,"r") as m:
                self.data=json.load(m)
        except:

            with open("iris.pkl","rb") as f:
                self.knnf=pickle.load(f)
        
            with open("data.json","r") as m:
                self.data=json.load(m)

                
    def prediction(self):
        self.load_model()
        array=np.ones(4)
        array[0]=self.sep_len
        array[1]=self.sep_wid
        array[2]=self.pet_len
        array[3]=self.pet_wid

        result=self.knnf.predict([array])
        print(result)
        return result
if __name__=="__main__":
    res=iris(3.8,4.6,1.9,0.8)
    res.prediction()