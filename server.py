from flask import *
# Flask,render_template,url_for
import csv
app=Flask(__name__)

@app.route('/')
def myhome():
    return render_template('index.html')
@app.route('/<string:page_name>')
def htmlpage(page_name):
    return render_template(page_name)
def WriteToFile(data):
    with open('database.txt',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email} || {subject} || {message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_write=csv.writer(database2,delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])
@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method =='POST':
        data= request.form.to_dict()
        write_to_csv(data)
        return render_template('/thankyou.html')
    return "Something went wrong. Try again!"


if __name__=="__main__":
    app.run(debug=True)
