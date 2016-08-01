---------
Changelog
---------
v1.3.1 2016-08-01
 * removed certificate verification during update of resources, because problem with publishing resource to public catalog
 
v1.3.0 2016-08-01
 * added certificate verification during update of resources
 
v1.2.4 2016-3-17
 * support urllib2 in version in version lower then 2.7.9 [OpenDataNode/ckanext-odn-ic2pc-sync#15]
 
v1.2.3 2016-3-17
 * added support certificate validation [OpenDataNode/ckanext-odn-ic2pc-sync#15]

v1.2.2 2015-12-17
 * state parameter added to dataset object [OpenDataNode/open-data-node#110]

v1.2.1 2015-10-02

Bug Fixes:
 * When uploading file to resource and its size is bigger than allowed be CKAN, clearer error message is returned

v1.2.0 2015-09-23

Notes:
 * Version jumped to 1.2.0 in order to align with tags / ODN releases

New Features:
 * Can synchronize private [boolean] parameter now

Bug Fixes:
 * fixed request not closed when internal error

v0.5.8 2015-08-05

Bug Fixes:
 * ckan_helper.has_edit_rights checked if the user had admin rights on organization, fixed to check rights to create and edit datasets

v0.5.7 2015-07-15

Bug Fixes:
 * fixed return value when checking CKAN site status of non responding CKAN or URL of this CKAN is wrong (for ic2pc plugin)

v0.5.6 2015-06-23

New Features:
 * Added site_read for checking if the url given belongs to CKAN
 * Added has_edit_rights for checking if the user has rights to organization dataset
 * Added redirection safe organization_show2

Bug fixes:
 * None