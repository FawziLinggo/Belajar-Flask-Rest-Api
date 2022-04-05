#import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisialisasi object flask
app = Flask(__name__)
#inisialisasi object flask_restful
api = Api(app)

#inisialisasi objek flask_cors
CORS(app)

#inisialisasi variabel kosong bertipe dictonary
identitas={}

#membuat class Resource
class contohResource(Resource):
    # metode get  dan post
    def get(self):
        #response = {"msg":"hi, ini app restfull pertama saya :D"}
        
        return identitas 

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data Berhasil dimasukan"}
        return response

#setup resource nya
api.add_resource(contohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
