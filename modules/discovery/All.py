#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Server Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import AdminInterfaces
import AllowMethod
import ApacheUsers
import ApacheXss
import Backdoor
import Backup 
import Captcha
import ClientAccessPolicy
import CommonDirectory
import CommonFile
import Cookie
import HtmlObject 
import LDAPInjection
import ModStatus
import Email 
import MultiIndex
import PrivateIP 
import Robots

def All(url,agent,proxy,redirect):
	common_modules = [
		Cookie.Cookie,
		AllowMethod.AllowMethod,
		Robots.Robots,
		ClientAccessPolicy.ClientAccessPolicy,
		PrivateIP.PrivateIP,
		Email.Email,
		MultiIndex.MultiIndex,
		Captcha.Captcha,
		ApacheUsers.ApacheUsers,
		ApacheXss.ApacheXss,
		HtmlObject.HtmlObject,
		LDAPInjection.LDAPInjection,
		ModStatus.ModStatus,
		AdminInterfaces.AdminInterfaces,
		Backdoor.Backdoors,
		Backup.Backup,
		CommonDirectory.CommonDirectory,
		CommonFile.CommonFile
	]
	for module in common_modules:
		module(url,agent,proxy,redirect).Run()

def AdminInterface(url,agent,proxy,redirect):
	common_modules = [
		AdminInterfaces.AdminInterfaces
	]
	for module in common_modules:
		module(url,agent,proxy,redirect).Run()

def Misconfiguration(url,agent,proxy,redirect):
	common_modules = [
		MultiIndex.MultiIndex,
		ModStatus.ModStatus,
		Backdoor.Backdoors,
		Backup.Backup,
		CommonDirectory.CommonDirectory,
		CommonFile.CommonFile
	]
	for module in common_modules:
		module(url,agent,proxy,redirect).Run()

def InfoDisclosure(url,agent,proxy,redirect):
	common_modules = [
		Robots.Robots,
		ClientAccessPolicy.ClientAccessPolicy,
		PrivateIP.PrivateIP,
		Email.Email
	]
	for module in common_modules:
		module(url,agent,proxy,redirect)
