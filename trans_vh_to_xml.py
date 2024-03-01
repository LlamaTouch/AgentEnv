import xml.etree.ElementTree as ET
import json

def clean_text(text):
    if text:
        # 转义特殊字符
        text = (text.replace('&', '&amp;')
                    .replace('<', '&lt;')
                    .replace('>', '&gt;')
                    .replace('"', '&quot;')
                    .replace("'", '&apos;'))

    return text

def vh_to_xml(vh_nodes):

    root = ET.Element("hierarchy")
    root.set("rotation", clean_text(vh_nodes[0].get("rotation", "0")))
    node_dict = {}
    child_index_counter = {}
    
    for vh_node in vh_nodes:

        node = ET.Element("node")
        node_dict[vh_node["temp_id"]] = node
        node.set("index", "0")

        for key, attr_name in [('text', 'text'), ('resource_id', 'resource-id'), ('class', 'class'),
                               ('package', 'package'), ('content_description', 'content-desc'),
                               ('checkable', 'checkable'), ('checked', 'checked'), ('clickable', 'clickable'),
                               ('enabled', 'enabled'), ('focusable', 'focusable'), ('focused', 'focused'),
                               ('scrollable', 'scrollable'), ('long_clickable', 'long-clickable'),
                               ('is_password', 'password'), ('selected', 'selected')]:
            value = vh_node.get(key)
            if value is not None:
                node.set(attr_name, clean_text(str(value).lower()) if isinstance(value, bool) else clean_text(value))


        if 'bounds' in vh_node and vh_node['bounds'] is not None:
            bounds_str = f"[{vh_node['bounds'][0][0]},{vh_node['bounds'][0][1]}][{vh_node['bounds'][1][0]},{vh_node['bounds'][1][1]}]"
            node.set('bounds', bounds_str)

    # 设置父子关系
    for vh_node in vh_nodes:
        temp_id = vh_node["temp_id"]
        parent_id = vh_node.get("parent")
        
        if parent_id is not None and parent_id in node_dict:
            parent_node = node_dict[parent_id]
            
            # 更新index
            index = child_index_counter.get(parent_id, 0)
            node_dict[temp_id].set('index', str(index))
            child_index_counter[parent_id] = index + 1
            
            # 添加到父节点
            parent_node.append(node_dict[temp_id])
        else:
            # 根节点的子节点
            index = child_index_counter.get("hierarchy", 0)
            node_dict[temp_id].set('index', str(index))
            child_index_counter["hierarchy"] = index + 1
            
            root.append(node_dict[temp_id])
    
    return ET.tostring(root, encoding='utf8', method='xml').decode('utf8')



if __name__ == '__main__':
    # vh_nodes = [
    #     {"package": "com.android.chrome", "visible": True, "checkable": False, "child_count": 3, "editable": False, "clickable": False, "is_password": False, "focusable": False, "enabled": True, "content_description": None, "children": [1, 119, 120], "focused": False, "bounds": [[0, 0], [1440, 3200]], "resource_id": None, "checked": False, "text": None, "class": "android.widget.FrameLayout", "scrollable": False, "selected": False, "long_clickable": False, "parent": -1, "temp_id": 0, "size": "1440*3200"},
    #     # ... 其他节点 ...
    # ]
    vh_path = "/data/jxq/mobile-agent/aitw_replay_data/151130279482320639/captured_data/view_hierarchy/0.json"
    with open(vh_path, "r") as f:
        vh_nodes = json.load(f)
    xml_path = "/data/jxq/0.xml"

    xml_data = vh_to_xml(vh_nodes)
    with open(xml_path, "w") as f:
        f.write(xml_data)