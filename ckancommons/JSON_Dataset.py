def load_from_dict(package):
    dat = JSON_Dataset()
    # we DO NOT want here id of package
    dat.name = package['name']
    dat.title = package['title']
    dat.notes = package['notes']
    dat.author = package['author']
    dat.extras = package['extras']
    dat.resources = package['resources']
    # license is creative commons by default 
    dat.license = package['license_id']
    return dat


def load_from_resource_dict(resource):
    '''
    Copies resource [dictionary] from ckan resource [dictionary]
    The main purpose is getting rid of unwanted parameters
    
    :param resource: ckan resource
    :return: [dictionary] resource that can be used for create / update
    '''
    resource_parameters = ['url', 'name', 'url_type', 'format']
    res = {}
    for par in resource_parameters:
        if  resource[par]:
            res[par] = resource[par].encode('utf8')
        else:
            res[par] = ''
    return res

def resource_create_update_with_upload(dest_ckan, resource, package_id):
        resource_to_create_update = load_from_resource_dict(resource)
        found, resource_id = dest_ckan.resource_search_by_url(resource['url'], package_id)
                    
        if found:
            resource_to_create_update['id'] = resource_id
            dest_ckan.resource_update(resource_to_create_update)
        else:
            # needs package id to know which package to associate it with
            resource_to_create_update['package_id'] = package_id
            dest_ckan.resource_create(resource_to_create_update)

class JSON_Dataset():
    def __init__(self):
        self.name = ''
        self.title = ''
        self.notes = ''
        self.author = ''
        self.extras = []
        self.resources = []
        # license is creative commons by default 
        self.license = 'cc-by'
   
    def tostring(self):
        return   u"[%s] name: [%s] title: [%s] notes: [%s] author: [%s] extras: [%s] resource: [%s]" % (self.__class__.__name__, self.name, self.title , self.notes , self.author, self.extras, self.resources)  
        
    def tojson_without_resource(self):
        return { "name" : self.name, "title" :  self.title, "notes": self.notes, "author": self.author, "extras": self.extras , "resources" : [], "license_id"  : self.license}
    
    def tojson_all(self):
        return { "name" : self.name, "title" :  self.title, "notes": self.notes, "author": self.author, "extras": self.extras , "license_id"  : self.license, "resources" : self.resources}

    def tojson_resource(self):
        if len(self.resources) > 0:
            result = self.resources[0]
        else:
            result = { }
            
        return result
    
    def __str__(self):
        return self.tostring().encode('utf8')