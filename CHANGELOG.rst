---------
Changelog
---------

v1.2.0 2015-09-16

Notes:
 * Version jumped to 1.2.0 in order to align with tags / ODN releases

New Features:
 * Can synchronize private [boolean] parameter now

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