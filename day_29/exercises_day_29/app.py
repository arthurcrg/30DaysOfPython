from datetime import datetime
import json
import os
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask, Response, request
import pymongo

app = Flask(__name__)

# Substitua pela sua string de conexão do MongoDB Atlas (ou use uma instância local mongodb://localhost:27017/)
# MONGODB_URI = 'mongodb://localhost:27017/'
MONGODB_URI = os.environ.get(
    'MONGODB_URI',
    'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority',
)

client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']  # Nome do banco de dados [cite: 3.1.2]
db_students = db['students']  # Nome da coleção [cite: 3.1.3]


# Rota GET: Listar todos os estudantes
@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
  students = db_students.find()
  return Response(dumps(students), mimetype='application/json')


# Rota GET por ID: Buscar um estudante específico
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def get_single_student(id):
  student = db_students.find_one({'_id': ObjectId(id)})
  return Response(dumps(student), mimetype='application/json')


# Rota POST: Adicionar um novo estudante
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
  name = request.form['name']
  country = request.form['country']
  city = request.form['city']
  skills = request.form['skills'].split(',')
  bio = request.form.get('bio', '')
  birthdate = request.form.get('birthdate', '')

  student = {
      'name': name,
      'country': country,
      'city': city,
      'skills': [s.strip() for s in skills],
      'bio': bio,
      'birthdate': birthdate,
      'created_at': datetime.now(),
  }

  db_students.insert_one(student)
  return Response(
      json.dumps({'message': 'Estudante criado com sucesso'}),
      mimetype='application/json',
      status=201,
  )


# Rota PUT: Atualizar os dados de um estudante
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
  data = request.form.to_dict()
  if 'skills' in data:
    data['skills'] = [s.strip() for s in data['skills'].split(',')]

  db_students.update_one({'_id': ObjectId(id)}, {'$set': data})
  return Response(
      json.dumps({'message': 'Estudante atualizado com sucesso'}),
      mimetype='application/json',
  )


# Rota DELETE: Remover um estudante
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
  db_students.delete_one({'_id': ObjectId(id)})
  return Response(
      json.dumps({'message': 'Estudante deletado com sucesso'}),
      mimetype='application/json',
  )


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)