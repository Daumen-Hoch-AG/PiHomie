#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# - One-to-Many:
# > One 	: db.relationship('CLASS', backref='new-column-name-in-foreign-class')
# > Many 	: db.Column(db.Integer, db.ForeignKey('COLUMN.id'))


class Noodle(db.Model):
	"""Table: Sensoren und Aktoren im PiHomie Netz und darüber hinaus"""
	id = db.Column(db.Integer, primary_key=True)
	bezeichnung = db.Column(db.String(100), nullable=True)
	art = db.Column(db.String(100), nullable=False)

	einheit = db.Column(db.String(100), nullable=True)
	function_umrechnung = db.Column(db.String(100), nullable=True)

	node_id = db.Column(db.Integer, db.ForeignKey('node.id'), nullable=False)
	raum_id = db.Column(db.Integer, db.ForeignKey('raum.id'), nullable=True)
	szene_id = db.Column(db.Integer, db.ForeignKey('szene.id'), nullable=True)


class Node(db.Model):
	"""Table: Knotenpunkte über die die Noodles angesteuert werden können"""
	id = db.Column(db.Integer, primary_key=True)
	bezeichnung = db.Column(db.String(100), nullable=True)

	noodles = db.relationship('Noodle', backref='parent_node')


class Raum(db.Model):
	"""Table: Sammlung von Nodes und Noodles nach ihrem Ort. Raum ist dabei eine frei definierbare Größe wie Raum, Etage, Haus oder Garten"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)

	noodles = db.relationship('Noodle', backref='raum')


class Szene(db.Model):
	"""Table: Einstellungen und Bedingungen für Makros, die Noodles in Szene setzen"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	noodles = db.relationship('Noodle', backref='szene')


class Event(db.Model):
	"""Table: Ereignisse und Bedingungen für Aktionen ohne Benutzerinteraktion"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
