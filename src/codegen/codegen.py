import os
import json
import string
import random
import jinja2

R = lambda x=8:''.join(random.sample(string.ascii_letters + string.digits, x))
RL = lambda x=10, y=8: [R(y) for i in range(x)] 
T = lambda x,s='':x[0].upper()+x[1:]+s

class CodeGen():
	def __init__(self, code, name):
		self.code = code
		self.name = name
		
		self.package = 'com.example'
		
		self.method = code
		self.clazz = T(code)
		self.interface = T(code)
		self.enum = T(code)
		self.title = T(code)
		
		self.bo = T(code, 'BO')
		self.qo = T(code, 'QO')
		self.vo = T(code, 'VO')
		self.listvo = T(code, 'ListVO')

		self.req = T(code, 'Request')
		self.res = T(code, 'Response')
		self.listres = T(code, 'ListResponse')

		self.rpc = T(code, 'Rpc')
		self.rpcFallback = T(code, 'RpcFallBack')

		self.service = T(code, 'Service')
		self.serviceImpl = T(code, 'ServiceImpl')
		self.biz = T(code, 'Biz')

		self.controller = T(code, 'Controller')

		self.bolist = []
		self.volist = []

		self.path = './'
		self.extends = ''
		self.implements = ''

	def items(self):
		fl = ['items', 'keys', 'values', 'template']
		for i in dir(self):
			if '__' not in i and i not in fl:
				v = self.__getattribute__(i)
				yield i, f"'{v}'" if isinstance(v, str) else str(v)

	def keys(self):
		for k,v in self.items():
			yield k

	def values(self):
		for k,v in self.items():
			yield v

	def __str__(self):
		return f'[{self.clazz}-{self.name}]({dict(self.items())})'


	def template(self, tpl):
		msg = jinja2.Template(tpl).render(api=self)
		return msg
