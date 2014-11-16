import ordrin
import urllib2

ordrin_api = ordrin.APIs("SvMY8WkSk78OHhgYSs55FVkUev7FOrdtEXF_1bExeUc", ordrin.TEST)

data = ordrin_api.delivery_list("ASAP", "715 Techwood Drive", "Atlanta", "30332")

name_list = []
id_list = []

for index in range(len(data)):
    id_list.append(data[index]['id'])
    name_list.append(data[index]['na'])

for i in range(len(id_list)):
    string_id = str(id_list[i])
    print(string_id)
    details = ordrin_api.restaurant_details(string_id)

yummly_info = urllib2.urlopen("http://api.yummly.com/v1/api/recipes?_app_id=69189240&_app_key=9e160e5cce7ff68eab06dc8b9b99de71&param[]=pizza").read()
print(yummly_info)
