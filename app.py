#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__)
#__something__ has meaning in python eg.__main__, __name__


# In[3]:


import joblib

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        rate= float(request.form.get("rate"))
        print(rate)
        model= joblib.load("DBS_prediction")
        result_final = model.predict([[rate]])
        return(render_template("index.html",result = result_final))
    else:
        #before you enter the button
        return(render_template("index.html",result ="waiting"))


# In[4]:


if __name__=="__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




