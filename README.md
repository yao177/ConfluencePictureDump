# ConfluencePictureDump

> Help save external-url pictures as attachments in Confluence.

## Usage
1. prepare python3 envirement
2. download `ConfluencePictureDump.py`
3. install requirements: `pip3 install python-magic atlassian-python-api BeautifulSoup4 lxml`
4. edit `ConfluencePictureDump.py` (see details in file comments)
5. run: `python3 ConfluencePictureDump.py`

## Background
When I paste external website page into confluence, it just paste the url of picture but not the picture attchment. And confluence official is not going to 'fix' it. Some cases will be listed below:
- https://community.atlassian.com/t5/Confluence-discussions/Save-Web-Image-as-local-File/td-p/1523462
- https://jira.atlassian.com/browse/CONFCLOUD-28739
- https://jira.atlassian.com/browse/CONFSERVER-28739

## P.S.
I just test on my MacBook, and it's a immature version.
So welcome report bugs and PR in issues!

## Reference
- [Atlassian Python API](https://atlassian-python-api.readthedocs.io/confluence.html)
- [Confluence REST API](https://developer.atlassian.com/cloud/confluence/rest/intro/)
