import requests
from flask import Flask,request
from flask_restful import Resource, Api
from flask_jwt import JWT,jwt_required


from http import HTTPStatus
import json

app= Flask(__name__)

api=Api(app)


def fetch_rates(currency):
    response= requests.get(f'http://data.fixer.io/api/latest?access_key=7e7981a11dcb63ab495e9a1058306a09&format=1')
    print("API Called")

    if response.status_code == HTTPStatus.OK:
        return json.loads(response.text)


import pymongo


myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = myclient["mydatabase"]
collection = mydb["customers"]      


def put_data(list1):
    collection.insert_one(list1)


def delete_once():
    collection.drop()



from pprint import pprint as pp
# if collection==None or 
# x = fetch_rates('BRL')    


def get_rates(cur1,cur2):
    res=[]
    cursor = collection.find({})

    for document in cursor: 
        exchange1=document['rates'][cur1]
        exchange2=document['rates'][cur2]
        time=document['timestamp']
        x=(exchange1,exchange2,time)
        res.append(x)

    return res  







import time

six_hours=6*60*60



def apiRequest(cur1,cur2):
    array=get_rates(cur1,cur2)
    time1=array[0][2]
    miliseconds = int(round(time.time()))
    print(miliseconds,time1)
    if miliseconds-time1 > six_hours:
        x=fetch_rates('INR')
        delete_once()
        put_data(x)
        y=get_rates(cur1,cur2)
        return y

    return array

# ans=apiRequest()
# print(ans)
# ans=(ans[0][1]/ans[0][0]) 


class Convert(Resource):
    def get(self,cur1,cur2,amt):
        ans=apiRequest(cur1,cur2)
        ans=(ans[0][1]/ans[0][0]) * amt
        return {"ans":ans}

api.add_resource(Convert,'/<string:cur1>/<string:cur2>/<int:amt>')

app.run(port=4999,debug=True)



    


    




# from currency_converter.core import fetch_rates

# >>> from pprint import pprint as pp
# >>> exchange_rates = fetch_rates('BRL')
# >>> pp(exchange_rates)
    
        