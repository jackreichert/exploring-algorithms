#!/usr/local/bin/python3
class Stack:
	def __init__(self):
		self.size = 0
		self.values = []

	def isEmpty(self):
		return 0 == self.getSize()

	def push(self, value):
		self.values.insert(0, value)

	def getSize(self):
		return len(self.values)

	def pop(self):
		if self.isEmpty():
			raise self.Underflow("Underflow")
		return self.values.pop(0)

	def top(self):
		if self.isEmpty():
			raise self.Empty("Empty")
		return self.values[0]

	def find(self, value):
		try:
			return self.values.index(value)
		except:
			return None

	class Underflow(Exception):
		pass

	class Empty(Exception):
		pass
