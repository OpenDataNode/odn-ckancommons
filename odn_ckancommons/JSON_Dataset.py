RESOURCE_FIELDS = ['url', 'name', 'url_type', 'format', 'description',
                    'created', 'last_modified', 'mimetype', 'mimetype_inner']

def load_from_dict(package):
    dat = JSON_Dataset()
    # we DO NOT want here id of package
    dat.name = package['name']
    dat.title = package['title']
    dat.notes = package['notes']
    dat.author = package['author']
    dat.extras = package['extras']
    dat.resources = package['resources']
    dat.tags = prepare_tags(package['tags'])
    # license is creative commons by default 
    dat.license = package['license_id']
    dat.owner_org = package['owner_org']
    dat.organization = package['organization']
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
        self.extras = []
        self.resources = []
        self.tags = []
        # license is creative commons by default 
        self.license = 'cc-by'
        self.owner_org = []
        self.organization = []


    def tostring(self):
        return   u"[%s] name: [%s] title: [%s] notes: [%s] author: [%s] extras: [%s] resource: [%s] owner_org:[%s]" % (self.__class__.__name__, self.name, self.title , self.notes , self.author, self.extras, self.resources, self.owner_org)

    def tojson_without_resource(self):
        return { "name" : self.name, "title" :  self.title, "notes": self.notes, "author": self.author, "extras": self.extras, "license_id" : self.license, "tags": self.tags, "owner_org" : self.owner_org}

    def tojson_all(self):
        return { "name" : self.name, "title" :  self.title, "notes": self.notes, "author": self.author, "extras": self.extras , "license_id"  : self.license, "resources": self.resources, "tags": self.tags, "owner_org" : self.owner_org}

    def tojson_resource(self):
        if len(self.resources) > 0:
            result = self.resources[0]
        else:
            result = { }

        return result

    def __str__(self):
        return self.tostring().encode('utf8')