#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_login import UserMixin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask import Flask, request
from sqlalchemy import func, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DB_NAME = "medicode.db"

# initialize the app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey?'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)
# db.init_app(app)


class Patient(Base):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    id_number = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))


class Institution(Base):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Record(Base):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'))
    date = db.Column(db.DateTime, default=func.now())
    prescription = db.Column(db.String(256))
    diagnosis = db.Column(db.String(256))
    patient = db.relationship(
            'Patient',
            backref=db.backref('records', lazy='dynamic'))
    hospital = db.relationship(
            'Institution',
            backref=db.backref('records', lazy='dynamic'))
