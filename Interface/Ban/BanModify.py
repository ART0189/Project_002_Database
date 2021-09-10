from DataBase import db
from flask import Blueprint, jsonify, request
from Models.Ban.TelephoneBanned import TelephoneBanned
from Models.Ban.HardwareCodeBanned import HardwareCodeBanned

def PyAddTelephoneBanned(telephone):
    tptele=TelephoneBanned(TelephoneBanned=telephone)
    db.session.add(tptele)
    db.session.commit()
    return

def PyAddHardwareCodeBanned(hardwarecode):
    tphard=HardwareCodeBanned(HardwareCodeBanned=hardwarecode)
    db.session.add(tphard)
    db.session.commit()
    return

def FindTelephoneBanned(newtele):
    return bool(TelephoneBanned.query.filter_by(TelephoneBanned=newtele).first())

def FindHardwareCodeBanned(newhard):
    return bool(HardwareCodeBanned.query.filter_by(HardwareCodeBanned=newhard).first())