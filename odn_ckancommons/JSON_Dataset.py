RESOURCE_FIELDS = ['url', 'name', 'url_type', 'format', 'description',
                    'created', 'last_modified', 'mimetype', 'mimetype_inner']

def load_from_dict(package):
    dat = JSON_Dataset()
    # we DO NOT want here id of package
    dat.name = package['name']
    dat.title = package['title']
    dat.notes = package['notes']
    dat.author = package['author']
    dat.author_email = package['author_email']
    dat.maintainer = package['maintainer']
    dat.maintainer_email = package['maintainer_email']
    dat.url = package['url']
    dat.version = package['version']
    dat.extras = package['extras']
    dat.resources = package['resources']
    dat.tags = prepare_tags(package['tags'])
    # license is creative commons by default 
    dat.license = package['license_id']
    dat.owner_org = package['owner_org']
    dat.organization = package['organization']
    dat.private = package['private']
    return dat


def prepare_tags(tags_dicts):
    """Makes from the package tags free tags

    :param tags_dicts: tags of dataset
    :type tags_dicts: list of dictionaries
    
    :return: list of free tags
    """
    free_tags = []
    for tag in tags_dicts:
        free_tag = {
            'vocabulary_id':None,
            'name':tag['name']
        }
        free_tags.append(free_tag)
    return free_tags    


def load_from_resource_dict(resource, whitelist_extras=None):
    '''
    Copies resource [dictionary] from ckan resource [dictionary]
    The main purpose is getting rid of unwanted parameters
    
    :param resource: ckan resource
    :type resource: dictionary
    :param whitelist_extras: whitelist of extras keys
    :param whitelist_extras: list of strings
    
    :return: [dictionary] resource that can be used for create / update
    '''
    resource_fields = RESOURCE_FIELDS
    
    if whitelist_extras:
        resource_fields += whitelist_extras
    
    res = {}
    for par in resource_fields:
        if par in resource and resource[par]:
            res[par] = resource[par].encode('utf8')
        else:
            res[par] = ''
    return res


def resource_create_update_with_upload(dest_ckan, resource, package_id, whitelist_extras=None):
        resource_to_create_update = load_from_resource_dict(resource, whitelist_extras)
        found, resource_id = dest_ckan.get_package_resource_by_name(resource['name'], package_id)

        if found:
            resource_to_create_update['id'] = resource_id
            return dest_ckan.resource_update(resource_to_create_update)
        else:
            # needs package id to know which package to associate it with
            resource_to_create_update['package_id'] = package_id
            return dest_ckan.resource_create(resource_to_create_update)


def filter_package_extras(dataset_obj, whitelist_extras):
    if not whitelist_extras:
        return []
        
    dataset_obj.extras = [x for x in dataset_obj.extras if x['key'] in whitelist_extras]
    
    
def filter_resource_extras(resource, whitelist_extras):
    if not whitelist_extras:
        whitelist_extras = []
            
    allowed_fields = RESOURCE_FIELDS + whitelist_extras
        
    for field in resource.keys():
        if field not in allowed_fields:
            resource.pop(field)
                

class JSON_Dataset():
    def __init__(self):
        self.name = ''
        self.title = ''
        self.notes = ''
        self.author = ''
        self.author_email = ''
        self.maintainer = ''
        self.maintainer_email = ''
        self.url = ''
        self.version = ''
        self.extras = []
        self.resources = []
        self.tags = []
        # license is creative commons by default 
        self.license = 'cc-by'
        self.owner_org = []
        self.organization = []
        self.private = False


    def tostring(self):
        return   u"[%s] name: [%s] title: [%s] notes: [%s] author: [%s] author_email: [%s] maintainer: [%s] maintainer_email: [%s] url: [%s] version: [%s] extras: [%s] resource: [%s] owner_org:[%s] private:[%s]" % (self.__class__.__name__, self.name, self.title , self.notes , self.author, self.author_email, self.maintainer, self.maintainer_email, self.url, self.version, self.extras, self.resources, self.owner_org, self.private)

    def tojson_without_resource(self):
        return {
            "name" : self.name,
            "title" :  self.title,
            "notes": self.notes,
            "author": self.author,
            "author_email": self.author_email,
            "maintainer": self.maintainer,
            "maintainer_email": self.maintainer_email,
            "url": self.url,
            "version": self.version,
            "extras": self.extras, 
            "license_id" : self.license,
            "tags": self.tags, 
            "owner_org" : self.owner_org,
            "private" : self.private
        }

    def tojson_all(self):
        dict = self.tojson_without_resource()
        dict["resources"] = self.resources
        return dict

    def tojson_resource(self):
        if len(self.resources) > 0:
            result = self.resources[0]
        else:
            result = { }

        return result

    def __str__(self):
        return self.tostring().encode('utf8')