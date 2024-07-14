import xml.etree.ElementTree as ET

def xml_string_to_json(xml_string):
    root = ET.fromstring(xml_string) 
    node_id = 0 
    json_list = []  


    def process_node(node, parent_id=-1):
        nonlocal node_id
        current_id = node_id
        node_id += 1  
        

        node_dict = {
            "bounds": convert_bounds(node.get('bounds', '')),
            "checkable": node.get('checkable', 'false') == 'true',
            "checked": node.get('checked', 'false') == 'true',
            "children": [],          
            "class": node.get('class',None),
            "clickable": node.get('clickable', 'false') == 'true',     
            "content_description": node.get('content-desc', None),
            "editable": False, 
            "enabled": node.get('enabled', 'true') == 'true',
            "focusable": node.get('focusable', 'false') == 'true',
            "focused": node.get('focused', 'false') == 'true',
            "is_password": node.get('password', 'false') == 'true',
            "long_clickable": node.get('long-clickable', 'false') == 'true',
            "package": node.get('package', ''),
            "parent": parent_id,
            "resource_id": node.get('resource-id', None),
            "scrollable": node.get('scrollable', 'false') == 'true',
            "selected": node.get('selected', 'false') == 'true',
            "size": "1080*2400",
            "temp_id": current_id, 
            "text": node.get('text', None),
            "visible": True, 
           
        }
        

        child_nodes = list(node)
        node_dict["child_count"] = len(child_nodes)
        
        child_ids = []
        for child in child_nodes:
            child_dict = process_node(child, parent_id=current_id)
            child_ids.append(child_dict["temp_id"])
        node_dict["children"] = child_ids

        json_list.append(node_dict)
        return node_dict
    

    def convert_bounds(bounds_str):
        """Convert bounds from string format '[x0,y0][x1,y1]' to a list [[x0, y0], [x1, y1]]"""
        if bounds_str:
            parts = bounds_str.replace('[', '').split(']')
            start = list(map(int, parts[0].split(',')))
            end = list(map(int, parts[1].split(',')))
            return [start, end]
        return [[0, 0], [0, 0]]


    process_node(root)
    # Sort list of nodes by temp_id in ascending order
    sorted_json_list = sorted(json_list, key=lambda x: x['temp_id'])
    return sorted_json_list


