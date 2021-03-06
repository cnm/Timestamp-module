import xml

def new_html_description_div(slot, name_of_description, description):
    first_div_id = slot.source.replace('.','_') + '-' + name_of_description +'-description-header'
    second_div_id = slot.source.replace('.','_') + '-' + name_of_description +'-description'
    html = xml.element('div', xml.element('div','+', class_ = 'plussign') + " Description\n\t" + xml.element('div', description, id_ = second_div_id, class_='description') + "\n", id_ = first_div_id, class_ = 'desc_header')
    return html
    
def new_html_packet_delay_div(slot):
    return xml.element('div', new_html_description_div(slot, 'packet-delay', "This graph represents the instant in which each packet arrived.<br /><br />On the X axis we have the number of each packet. On the Y axis the instant at which each packet arrived, that is the number of milliseconds that have elapsed since the first packet was created.<br /><br />In perfect conditions, one should expect a linear growth described by this graph, which would mean that the delay of each packet is 0. However sometimes a small tolerable delay can occur."), id_ = slot.source.replace('.','_') + '-packet-delay')

def new_html_packet_data_div(slot):
    return xml.element('div', new_html_description_div(slot, 'packet-data', "This graph represents the data collected by node " + slot.source), id_ = slot.source.replace('.','_') + '-packet-data')

def new_html_slot(slot):
    html_id = slot.source.replace('.','_')
    html = xml.element('h2', slot.source) + "\n"
    html += xml.element('div', "\n" + new_html_packet_data_div(slot) + "\n" + new_html_packet_delay_div(slot) + "\n", id_ = slot.source.replace('.', '_') + '-graphs', class_ = 'slot_graphs')
    return xml.element('div', html, id_ = slot.source.replace('.', '_'), class_ = 'slot')

def include_scripts(*slot_list):
    html = xml.element('script',None, src = 'scripts/jQuery.js', type = 'text/javascript') + xml.element('script',None, src = 'scripts/jgcharts/jgcharts.js', type = 'text/javascript') + xml.element('script',None, src = 'scripts/analise.js', type = 'text/javascript') 
    script = "\njQuery(document).ready(function(){\n"
    for sl in slot_list:
        script += 'execute' + sl.source.replace('.', '_') + "();\n"
    script += "jQuery('.desc_header').click(function(){jQuery(this).children().first().next().slideToggle(); if(jQuery(this).children().first().text() == '+') jQuery(this).children().first().text('-'); else jQuery(this).children().first().text('+');});"
    script += "});"
    html += xml.element('script', script, type = 'text/javascript')
    return html

def include_css():
    return xml.element('link', None, href = 'stylesheets/main.css', rel = 'stylesheet', type="text/css")

def new_html_page(*slot_list):
    html = xml.element('h1', 'Results', id_ = 'main-header')
    for sl in slot_list:
        html += new_html_slot(sl) + xml.element('hr')
    html = xml.element('html', xml.element('head', xml.element('title','Results') + "\n" + include_scripts(*slot_list)) + "\n" + include_css() +"\n" + xml.element('body',html))
    return html
