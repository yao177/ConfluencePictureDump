# ConfluencePictureDump

> Help save external-url pictures as attachments in Confluence.

## Usage
1. prepare python3 envirement
2. download `ConfluencePictureDump.py`
3. install requirements: `pip3 install python-magic atlassian-python-api BeautifulSoup4 lxml`
4. edit `ConfluencePictureDump.py` (see details in file comments)
5. run: `python3 ConfluencePictureDump.py`

### Detailed
#### Page Directory
File directories show below.
- sourceSpace
  - sourceParentPage
    - pageA (waiting conversion)
    - pageB (waiting conversion)
    - ...
- targetSpace
  - targetParentPage
    - pageA (converted)
    - pageB (converted)
    - ...

All children pages in `sourceParentPage` will be converted.
Note, `sourceSpace` can be same as `targetSpace`, but it's NOT recommanded to set `sourceParentPage` same as `targetParentPage` because the script would convert again.

## TODO
- [x] adapt manually copied contents
- [ ] adapt Web-Clipper APP

## Background
When I paste external website page into confluence, it just paste the url of picture but not the picture attchment. And confluence official is not going to 'fix' it. Some cases will be listed below:
- https://community.atlassian.com/t5/Confluence-discussions/Save-Web-Image-as-local-File/td-p/1523462
- https://jira.atlassian.com/browse/CONFCLOUD-28739
- https://jira.atlassian.com/browse/CONFSERVER-28739

Besides these, I use [Web Clipper](https://chrome.google.com/webstore/detail/web-clipper/mhfbofiokmppgdliakminbgdgcmbhbac) to save web contents. But this App just paste picture url as confluence.

## P.S.
I just test on my MacBook, and it's a immature version.
So welcome report bugs and PR in issues!

## Reference
- [Atlassian Python API](https://atlassian-python-api.readthedocs.io/confluence.html)
- [Confluence REST API](https://developer.atlassian.com/cloud/confluence/rest/intro/)
