import json
import requests
from flask import Flask
from flask import request, url_for, redirect, render_template

app = Flask(__name__,
	 static_url_path='',
	 static_folder="new-web/static",
	 template_folder="new-web/templates")

@app.route("/test")
def hello():
	return render_template("index.html")
    #return "Hello From Flask!"

@app.route("/")
def mainHandler():
#    return "Test Index"
	return render_template("index.html")

@app.route("/index.html")
def indexHandler():
	return render_template("index.html")

@app.route("/home")
def HomeHandle():
	return render_template("home.html")

@app.route("/home.html")
def HomeHandler():
	return render_template("home.html")

@app.route("/blog")
def blogHandle():
	return render_template("blog.html")

@app.route("/service")
def serviceHandle():
	return render_template("service.html")

@app.route("/service.html")
def serviceHandler():
	return render_template("service.html")

@app.route("/contact.html")
def contactHandler():
	return render_template("contact.html")

@app.route("/blog.html")
def blogHandler():
	return render_template("blog.html")

@app.route("/contact")
def contactHandle():
	return render_template("contact.html")

@app.route("/about")
def aboutHandle():
	return render_template("about.html")

@app.route("/about.html")
def aboutHandler():
	return render_template("about.html")

@app.route("/updateForm.html", methods =["GET", "POST"])
def updateHandler():
	if request.method == "POST":
		email = request.form.get("email")
		university = request.form.get("uniName")
		organization = request.form.get("orgName")
		
		if university!="":
			result = requests.post("https://ikwm7ce222.execute-api.ap-south-1.amazonaws.com/StudyMate-Beta/user/update-university", data=json.dumps({"email": email, "new_university": university}))
	
		if organization!="":
			new_result = requests.post("https://ikwm7ce222.execute-api.ap-south-1.amazonaws.com/StudyMate-Beta/user/update-organization", data=json.dumps({"email": email, "new_organization" : organization}))
		
		return render_template("home.html")

	return render_template("updateForm.html")

@app.route("/filter.html", methods =["GET", "POST"])
def getFilter():
	if request.method == "POST":
		searchVal = request.form.get("searchValue")
		filter = request.form.get("choice")
		if filter == 'university':
			allUni = requests.get("https://ikwm7ce222.execute-api.ap-south-1.amazonaws.com/StudyMate-Beta/user/get-all-university", data=json.dumps({"university": searchVal}))
			str = json.loads(allUni.text)
			someRes = str['data']
			return render_template('searchResults.html', result = someRes)

		if filter == 'organization':
			allUni = requests.get("https://ikwm7ce222.execute-api.ap-south-1.amazonaws.com/StudyMate-Beta/user/get-all-organization", data=json.dumps({"organization": searchVal}))
			str = json.loads(allUni.text)
			val = str['data']
			return render_template('searchResults.html', result = val)

	return render_template("filter.html")

@app.route("/serviceLog.html")
def ServiceLogOutHandler():
	return render_template("serviceLog.html")

@app.route("/contactLog.html")
def ContactLogOutHandler():
	return render_template("contactLog.html")

@app.route("/aboutLog.html")
def AboutLogOutHandler():
	return render_template("aboutLog.html")


if __name__ == "__main__":
    app.run(ssl_context='adhoc')


