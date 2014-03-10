#! /usr/bin/env python

from subprocess import call
import datetime
import time
import sys
import os.path
import glob


#src = './tiffs/**/*.tiff'
src = '/cygdrive/z/NAIP/Pennsylvania/2013/TOUPLOAD/*/**.sid'
tags = 'autoupload:2013-11-25:01'
key = './3bdd03d0a00be20af4c3138fad74fe2f9acd7259-privatekey.p12'


#src_files = glob.glob (src)
#for s in src_files:
#	print s
params = [
	"/home/SkytTruth/github/gme_tools/gme_tools/mapsengineupload.py",
	"--email=533386216003@developer.gserviceaccount.com",
	"--projectid=06136759344167181854",
#	'--name=' + os.path.basename(s),
	'--attribution=Copyright SKYTRUTH',
#	'--time=' + time,
	'--tags=' + tags,
	'--key=' + key,
	src	
]
print params	
call(params)
	
		

