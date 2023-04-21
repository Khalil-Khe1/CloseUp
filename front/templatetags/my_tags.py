from django import template
register = template.Library()

@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    print(dict_data[key]['likes'])
    if key:
        if dict_data[key]['likes'] is not None:
            return dict_data[key]['likes']
        else:
            print("test")
            return 0
    
@register.filter('get_views')
def get_views(dict_data, key):
    if key:
        return dict_data[key]['views']