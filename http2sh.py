#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

import subprocess

class http2sh(object):

	def __init__(self, shell_start=None, remap_slash=None):

		if shell_start is None:
			shell_start = ["echo"]

		self.shell_start = shell_start
		self.remap_slash = remap_slash

	def dispatch_request(self, request):
		args = self.shell_start.copy()
		path_args = request.path.split("/")[1:]

		if self.remap_slash:
			path_args = map( lambda x: x.replace(self.remap_slash, "/"), path_args )

		args.extend( path_args )

		subprocess.call( args )

		return Response("Executing: " + str(args))

	def wsgi_app(self, environ, start_response):
		request = Request(environ)
		response = self.dispatch_request(request)
		return response(environ, start_response)

	def __call__(self, environ, start_response):
		return self.wsgi_app(environ, start_response)


import argparse


def arg_parser():
	parser = argparse.ArgumentParser(description='A terrible hack to send paramaters to a shell command')

	parser.add_argument('shell_start', metavar='arg', nargs="*"
			, help='initial shell parameters', default=["echo"])

	parser.add_argument('-p', '--port', type=int, default=4000
			, help='the port to run on')

	parser.add_argument('-r', '--remap', default=None
			, help='remap a character to forward slash')

	return parser


if __name__ == '__main__':
	from werkzeug.serving import run_simple

	parser = arg_parser()

	args = parser.parse_args()

	app = http2sh(shell_start=args.shell_start, remap_slash=args.remap)

	run_simple('localhost', args.port, app)


