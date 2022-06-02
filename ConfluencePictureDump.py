#!/usr/bin/env python3

# coding=utf-8

import logging
import argparse
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os.path

import magic
from atlassian import Confluence


confluence = Confluence(
	url="",       # confluence website base url
	username="",  # your username
	password="",  # your password
)
sourceSpaceKey = ''       # source page's space-key (space overview -> space key)
sourceParentPageName = '' # source page's directory/parent-page NAME (not page-id)
targetSpaceKey = ''       # target page's space-key
targetParentPageName = '' # source page's directory/parent-page NAME (not page-id)


def upload_pic(img_url, page_id):
	imgDir, fileName = download_pic(img_url, page_id)
	print(imgDir)
	contentType = magic.from_file(imgDir, mime=True)
	confluence.attach_file(imgDir, name=None, content_type=contentType, page_id=childId, title=None, space=None, comment=None)
	return fileName


def download_pic(pic_url, page_id):
	name = pic_url.split('/')[-1]
	dir_path = './pic/'
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
	dir_path += page_id
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
	local_pic_path = dir_path + '/' + name
	urlretrieve(pic_url, local_pic_path)
	return local_pic_path, name
	

soursePageId = confluence.get_page_id(spaceKey, sourceParentPageName)
targetPageId = confluence.get_page_id(targetSpaceKey, targetParentPageName)
childList = list(confluence.get_page_child_by_type(soursePageId, type='page', start=None, limit=None))
for child in childList:
	childId = child['id']
	print('childId:', childId)
	childPage = confluence.get_page_by_id(childId, expand='body.storage', status=None, version=None)
	childHtml = childPage.get('body').get('storage').get('value')
	soup = BeautifulSoup(childHtml, 'html.parser')
	for imgTag in soup.select('ac\:image'):
#		print(imgTag)
		for urlTag in imgTag.children:
			if urlTag.name != 'ri:url':
				continue
			fileName = upload_pic(urlTag['ri:value'], childId)
			urlTag.name = 'ri:attachment'
			del urlTag['ri:value']
			urlTag['ri:filename'] = fileName
			try:
				urlTag.parent.parent.parent.span.unwrap()
			except:
				print('Warn: unwrap fail!')
#	print(soup)
	updateRes = confluence.update_existing_page(childId, childPage.get('title'), body=str(soup))
	try:
		if updateRes.get('id') != 0:
			print(f'{childId} update success!')
			moveRes = confluence.move_page(targetSpaceKey, page_id=childId, target_id=targetPageId, position='append')
			print(f'{childId} move success!')
	except:
		print(f'{childId} update fail! Maybe something goes wrong.')
