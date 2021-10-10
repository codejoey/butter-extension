from flask import Flask, jsonify, request
app=Flask(__name__)

#import our functions from the price.py file
from price import cartFromUrl
from price import itemFromUrl

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
#getting the url argument       
        url = request.args.get('url')
        result=cartFromUrl(str(url))
        return jsonify(result)
    else:
        return jsonify({'Error':"This is a GET API method"})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9007)
