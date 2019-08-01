from app import app
from flask import render_template, request
from app.models import model, formopener
import random

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")
    

@app.route('/')
@app.route('/results', methods = ["POST", "GET"])
@app.route('/results.html', methods = ["POST", "GET"])
def results():
    
    userdata = request.form
    Theme = userdata["Theme"]
    result=""
    if Theme == "Cheesy":
        print(model.pickup_lines["Cheesy"])
        cheesyPickuplines = (model.pickup_lines ["Cheesy"])
        result = random.choice(cheesyPickuplines)
        
    if Theme == "Cute":
        print(model.pickup_lines ["Cute"])
        cutePickuplines = (model.pickup_lines ["Cute"])
        result = random.choice(cutePickuplines)
        
    if Theme == "Cringey":
        print(model.pickup_lines ["Cringy"])
        cringyPickuplines = (model.pickup_lines ["Cringy"])
        result = random.choice(cringyPickuplines)
        
    if Theme == "Technology":
        print(model.pickup_lines ["Technology"])
        technologyPickuplines = (model.pickup_lines ["Technology"])
        result = random.choice(technologyPickuplines)
        
    if Theme == "Random":
        print(model.pickup_lines ["Random"])
        randomPickuplines = (model.pickup_lines ["Random"])
        result = random.choice(randomPickuplines)   
    
    if Theme == "Ethnicity":
        print(model.pickup_lines ["Ethnicity"])
        ethnicityPickuplines = (model.pickup_lines ["Ethnicity"])
        result = random.choice(ethnicityPickuplines)
        
    return render_template('results.html', result=result)
    
    
    
    
    
    