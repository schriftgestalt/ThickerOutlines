# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class ThickerOutlines(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Thicker Outlines',
			})

	@objc.python_method
	def foreground(self, layer):
		graphicView = self.controller.graphicView()
		print(graphicView.backgroundColor(), graphicView.foregroundColor())
		graphicView.backgroundColor().set()
		bezierPath = layer.bezierPath
		openBezierPath = layer.openBezierPath
		bezierPath.setLineWidth_(2.25 / self.getScale())
		bezierPath.stroke()
		openBezierPath.setLineWidth_(2.25 / self.getScale())
		openBezierPath.stroke()
		graphicView.foregroundStrokeColor().set()
		bezierPath.setLineWidth_(1.5 / self.getScale())
		bezierPath.stroke()
		openBezierPath.setLineWidth_(1.5 / self.getScale())
		openBezierPath.stroke()
		

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
