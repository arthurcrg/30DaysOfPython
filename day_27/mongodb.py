# Mongo DB is a NoSQL database that stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time. It is designed for scalability and performance, making it suitable for handling large volumes of unstructured data.
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo # importing pymongo module
from bson.objectid import ObjectId # id object
MONGODB_URI = 'mongodb+srv://batatazeda:1903@30daysofpython.9fbspsq.mongodb.net/?appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
db.students.drop()