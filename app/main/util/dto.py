from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True,
                               description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True,
                                  description='The user password'),
    })

class MaterialDto:
    api = Namespace('material', description='material related operations')
    material = api.model('material', {
        'id': fields.String(description='The material id'),
        'name': fields.String(description='The name of the material'),
        'type': fields.String(description='The material type', attribute='type._value_', enum=['bsdf', 'light_source', 'opaque', 'translucent']),
        'red': fields.Float(min=0, max=1, description='The red hue of the Light material'),
        'green': fields.Float(min=0, max=1, description='The green hue of the Light material'),
        'blue': fields.Float(min=0, max=1, description='The blue hue of the Light material'),
        'radius': fields.Float(min=0, exclusiveMin=True, description='The radius of the Light material'),

        'r_reflectance': fields.Float(min=0, max=1, description='The red reflectance of the Opaque material'),
        'g_reflectance': fields.Float(min=0, max=1, description='The green reflectance of the Opaque material'),
        'b_reflectance': fields.Float(min=0, max=1, description='The blue reflectance of the Opaque material'),
        'specularity': fields.Float(min=0, max=1, description='The specularity of the Opaque material'),
        'roughness': fields.Float(min=0, max=1, description='The roughmess of the Opaque material'),

        'r_transmittance': fields.Float(min=0, max=1, description='The red transmittance of the Translucent material'),
        'g_transmittance': fields.Float(min=0, max=1, description='The green transmittance of the Translucent material'),
        'b_transmittance': fields.Float(min=0, max=1, description='The blue transmittance of the Translucent material'),

        'xml_data': fields.String(description='The XML string representation of the BSDF material'),
        'up_orientation': fields.Float(min=0, max=1, description='The orientation of the BSDF material'),
        'thickness': fields.Float(min=0, exclusiveMin=True, description='The thickness of the BSDF material'),

        'refraction': fields.Float(min=0, max=1, description='The refraction index of the material'),
        'modifier': fields.String(description='The string modifier of the material')
    })


class HoneybeeSurfaceDto:
    api = Namespace('honeybee_surface', description='honeybee surface related operations')
    honeybee_surface = api.model('honeybee_surface', {
        'id': fields.String(description='The honeybee surface id'),
        'name': fields.String(description='The name of the honeybee surface'),
        'type': fields.String(required=True, description='The type of surface', enum=['wall', 'underground wall', 'roof', 'underground ceiling', 'floor', 'slab on grade', 'exposed floor', 'ceiling', 'window', 'context']),
        'state_name': fields.String(description='the name of the default honeybee surface state, usually \'default\''),
        'radiance_material': fields.Nested(MaterialDto.material),
        'vertices': fields.List(fields.Nested(api.model('vertex', {
            'x': fields.Float(required=True),
            'y': fields.Float(required=True),
            'z': fields.Float(required=True)
        }))),
        'states': fields.List(fields.Nested(api.model('surface state', {
            'name': fields.String(description='Name of the state'),
            'type': fields.String(require=True, description='The type of surface', attribute='type._value_', enum=['wall', 'underground wall', 'roof', 'underground ceiling', 'floor', 'slab on grade', 'exposed floor', 'ceiling', 'window', 'context']),
            'radiance_material': fields.Nested(MaterialDto.material)
        })))
    })

