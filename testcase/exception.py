#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	try:
		print(d[0])
	except Exception as e:
		print(e.__class__.__name__)
		raise e

if __name__ == "__main__":
	main()