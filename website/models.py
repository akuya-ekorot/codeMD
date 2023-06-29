#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db
from flask_login import UserMixin
from sqlalchemy import func


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))


class Institution(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Record(db.Model, UserMixin):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'))
    date = db.Column(db.DateTime, default=func.now())
    prescription = db.Column(db.String(50))
    patient = db.relationship(
            'Patient',
            backref=db.backref('records', lazy='dynamic'))
    hospital = db.relationship(
            'Institution',
            backref=db.backref('records', lazy='dynamic'))
