import re
import csv
import sys
import json

def create_dict(keys, field_value):
    if keys:
        if isinstance(keys[0], tuple):
            return {keys[0][0]:[create_dict(keys[1:], field_value)]}
        return {keys[0]:create_dict(keys[1:], field_value)}
    else:
        return field_value

def update_dict(d_, keys, field_value):
    if isinstance(keys[0], tuple):
        key, idx = keys[0][0], int(keys[0][1])
        update_list(d_, [key] + keys[1:], field_value, idx)
    elif keys[0] not in d_:
        d_[keys[0]] = create_dict(keys[1:], field_value)
    else:
        update_dict(d_[keys[0]], keys[1:], field_value)

def write_line(headers,values):
    assert len(headers) == len(values), 'Fieldnames and values lengths are differents'
    headers = [h.split('.') for h in headers]
    for fieldnames in headers:
        for i,name in enumerate(fieldnames):
            fieldnames[i] = islist(name)
    local_dict = {}
    for fieldname,value in zip(headers,values):
        update_dict(local_dict, fieldname ,value)
    return local_dict

def update_list(d_, keys, field_value, idx):
    if keys[0] not in d_:
        d_[keys[0]] = [create_dict(keys[1:], field_value)]
    elif int(idx) < len(d_[keys[0]]):
        update_dict(d_[keys[0]][idx], keys[1:], field_value)
    else:
        d_[keys[0]].append(create_dict(keys[1:], field_value))

def islist(string):
    translation = {91:None,
                  93:None}
    digits = re.findall('\[\d+\]', string)
    if digits:
        digits = digits[0]
        digits = int(digits.translate(translation))
        clean_string = re.sub('\[\d+\]' ,'', string)
        return clean_string, digits
    else:
        return string
    
def csv_to_json(filename, outfile_name, headers = None):
    with open(filename, 'r') as infile:
        data = csv.reader(infile)
        
        if not headers:
            headers = next(data)
        else:
            next(data)
        with open(outfile_name,'w') as outfile:
            for line in data:
                outfile.write(json.dumps(write_line(headers, line)) + '\n\n')
        outfile.close()
    infile.close()

if __name__ == '__main__':
    try:
        csv_to_json(sys.argv[1], sys.argv[2])
    except:
        print('Could not convert')