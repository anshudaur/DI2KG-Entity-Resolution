from os import listdir, walk
from os.path import isfile, join
import json
onlyfiles = [join(r,file).replace("2013_monitor_specs/","").replace(".json","") for r,d,f in walk("2013_monitor_specs/") for file in f]
set_of=set(onlyfiles)
rows=list()
brand_dict=dict()
to_delete_rules=set(['belkin','iogear'])
to_delete=set(['ergotron','compucessory','fellowes','kantek','rosewill','sports tracker',"dust off", "dust_off","dust-off"])
to_delete_files=set()
to_delete_files_rules=set()
reasons_to_delete=dict()
skip_first=True
stopwords=["17","15","display","product","led","17'","15'","21","23","24","3m","22","17","21.5","22","ve","20","allen-bradley","cd/mâ²", "color","professional","details","ultrasharp","27","3d","cinema","wide","x series","ultrasharp","19","920","ds-","new","cd/m2","1u","ohc24","2711p", "715l1009", "pe1229", "17''","e114849"]
for line in open("brand_assignations.csv"):
    if skip_first:
        skip_first=False
    else:
        rows.append(line.split(",")[0].replace("//","/"))
        brand_dict[line.split(",")[0].replace("//","/")]=line.split(",")[1].replace("\n","")
        if line.split(",")[1].replace("\n","") in to_delete:
            to_delete_files.add(line.split(",")[0].replace("//","/"))
            reasons_to_delete[line.split(",")[0].replace("//","/")]=line.split(",")[1].replace("\n","")
        elif line.split(",")[1].replace("\n","") in to_delete_rules:
            to_delete_files_rules.add(line.split(",")[0].replace("//","/"))
for item in rows:
    if not item in set_of:
        print("Missing: "+item)
rows=set(rows)
for item in set_of:
    if not item in rows:
        print("Missing: "+item)

brand_dict2= {
   "dell":[
      "dell",
      "ultrasharp",
      "optiplex",
      "wyse"
   ],
   "hp":[
      "hewlett-packard",
      "hewlett packard",
      "hhewlett",
      "zr22w"
   ],
   "nec":[
      "nec"
   ],
   "mitsubishi":[
      "mitsubishi"
   ],
   "samsung":[
      "dc series",
      "samsung",
      "essential"
   ],
   "lg":[
      "lg",
      "sva-usa"
   ],
   "apple":[
      "apple",
      "macbook"
   ],
   "acer":[
      "acer"
   ],
   "cisco":[
      "cisco"
   ],
   "philips":[
      "phillips",
      "philips"
   ],
   "asus":[
      "asus",
      "republic of gamers"
   ],
   "aver":[
      "aver",
      "avervision"
   ],
   "iiyama":[
      "iiyama",
      "ilyama"
   ],
   "epson":[
      "epson"
   ],
   "compaq":[
      "compaq"
   ],
   "sony":[
      "sony"
   ],
   "fuji":[
      "fuji",
      "fujicom"
   ],
   "viewsonic":[
      "viewsonic",
      "optiquest"
   ],
   "hyundai":[
      "hyundai",
      "hyunday"
   ],
   "lenovo":[
      "lenovo",
      "d221",
      "thinkpad"
   ],
   "ibm":[
      "ibm"
   ],
   "elo":[
      "elo",
      "tyco electronics"
   ],
   "fujitsu":[
      "fujitsu",
      "fijitsu"
   ],
   "packard bell":[
      "packard bell"
   ],
   "Yiynova":[
      "panda city"
   ],
   "datalogic":[
      "datalogic"
   ],
   "3M":[
      "microtouch"
   ],
   "touchsystems":[
      "touch systems",
      "touchsystems"
   ],
   "panasonic":[
      "panasonic"
   ],
   "olympus":[
      "olympus"
   ],
   "american dynamics":[
      "american dynamics"
   ],
   "ctx":[
      "ctx"
   ],
   "pioneerpos":[
      "pioneerpos"
   ],
   "ais":[
      "ais"
   ],
   "adesso":[
      "adesso"
   ],
   "advance one":[
      "advance one"
   ],
   "ace":[
      "ace"
   ],
   "aei":[
      "aei"
   ],
   "ag neovo":[
      "ag neovo technology corp."
   ],
   "APC":[
      "american power conversion corp"
   ],
   "aspen":[
      "aspen"
   ],
   "aten technologies":[
      "aten technologies",
      "aten corp",
      "aten"
   ],
   "automation direct":[
      "automation direct"
   ],
   "bci technology":[
      "bci technology"
   ],
   "cleartunes":[
      "cleartunes"
   ],
   "cinq":[
      "cinq"
   ],
   "cornea":[
      "cornea"
   ],
   "element electronics":[
      "element electronics"
   ],
   "ematic":[
      "ematic"
   ],
   "emerson":[
      "emerson"
   ],
   "etronix":[
      "etronix"
   ],
   "feelworld":[
      "feelworld"
   ],
   "foxboro":[
      "foxboro"
   ],
   "innolux":[
      "innolux"
   ],
   "infocus":[
      "infocus"
   ],
   "logic controls":[
      "logic controls"
   ],
   "magnavox":[
      "magnavox"
   ],
   "norwood":[
      "norwood"
   ],
   "nanovision":[
      "nanovision",
      "nano"
   ],
   "omron":[
      "omron"
   ],
   "pelco":[
      "pelco"
   ],
   "insignia":[
      "insignia"
   ],
   "crossover":[
      "crossover"
   ],
   "mag":[
      "mag innovision",
      "mag"
   ],
   "bk sems":[
      "bk sems"
   ],
   "avocent":[
      "avocent"
   ],
   "sceptre":[
      "sceptre"
   ],
   "chimei":[
      "chimei"
   ],
   "kds":[
      "kds"
   ],
   "siemens":[
      "siemens"
   ],
   "totevision":[
      "totevision",
      "TOTE VISION",
      "tote vision"
   ],
   "envision monitors":[
      "envision monitors"
   ],
   "x-star":[
      "x-star"
   ],
   "sympodium":[
      "sympodium"
   ],
   "AOC":[
      "brand new b-billion",
      "aoc international",
      "apc",
      "aoc monitor",
      "aoc envision"
   ],
   "i inc":[
      "i inc"
   ],
   "amptron":[
      "amptron"
   ],
   "gechic":[
      "gechic"
   ],
   "amw":[
      "amw"
   ],
   "pyle":[
      "Pyle audio",
      "inc"
   ],
   "adi":[
      "adi"
   ],
   "cmo":[
      "cmo"
   ],
   "vaddio":[
      "vaddio"
   ],
   "upstar":[
      "upstar"
   ],
   "commodore":[
      "commodore"
   ],
   "sansui":[
      "sansui"
   ],
   "carnetix":[
      "carnetix"
   ],
   "earth computer tech":[
      "earth computer tech"
   ],
   "itronix":[
      "itronix"
   ],
   "planar systems":[
      "planar systems"
   ],
   "schneider electric":[
      "schneider electric"
   ],
   "vizta":[
      "vizta"
   ],
   "achieva":[
      "achieva"
   ],
   "avue":[
      "avue"
   ],
   "soyo":[
      "soyo"
   ],
   "emachines":[
      "emachines"
   ],
   "gvision":[
      "gvision"
   ],
   "hkc":[
      "hkc"
   ],
   "sansui":[
      "sansui"
   ],
   "omni vision":[
      "omni vision"
   ],
   "proview":[
      "proview system desktop"
   ],
   "pyle":[
      "pylehome"
   ],
   "silicon graphics":[
      "sgi",
      "silicon graphics"
   ],
   "starlogic":[
      "star logic"
   ],
   "mimo":[
      "mimo monitors"
   ],
   "hannspree":[
      "hanns-g",
      "hanns.g",
      "hannspree",
      "hannsg",
      "hanns g",
   ],
   "evga":[
      "evga"
   ],
   "formac":[
      "formac"
   ],
   "planar":[
      "helium"
   ],
   "eizo":[
      "eizo coloredge",
      "eizo"
   ],
   "edge10":[
      "edge10"
   ]
}

quick_fix={"aoc":"AOC",
"hanns g":"hannspree",
"alienware":"alienware",
"barco":"barco",
"ultrasharp u2410":"dell",
"toshiba":"toshiba","xerox":"xerox","compaq v":"compaq","benq":"benq", 
"unbranded/generic":"unbranded/generic", "ncr":"ncr", "yamakasi":"yamakasi", "gateway":"gateway", "rockwell":"rockwell", "allen bradley":"rockwell","qnix":"qnix", "night owl":"night owl", "1plus":"1plus","wasabi mango":"wasabi mango","speco":"speco","bosto":"bosto","nanov":"nanov","westinghouse":"westinghouse","veba":"veba","pioneer pos":"pioneerpos","3m":"3M", "samsung syncmaster":"samsung", "bk sems by samsung":"samsung","autonav":"autonav","v7":"v7","tatung":"tatung","gnr":"gnr","doublesight":"doublesight","smart technologies":"smart technologies","mace":"mace","prism":"prism","lilliput":"lilliput","monoprice":"monoprice","genie":"genie","i-inc":"i-inc","ctl":"ctl","datalux":"datalux",
"auria":"auria","weldex":"weldex","innovera":"innovera","generaltouch":"generaltouch","atlona":"atlona","aten":"aten technologies","miracle business":"miracle business", "sysonic/miracle business":"miracle business","sysonic":"miracle business", "relisys":"relisys","jvc":"jvc","vigilant":"vigilant","canvys":"canvys","vizio":"vizio","pos-x":"pos-x","microtek":"microtek","viewz":"viewz","xenarc":"xenarc",
"lacie":"lacie","newline interactive":"newline interactive","okina":"okina","raritan":"raritan","princeton":"princeton","dclcd":"dclcd","sgi / silicon graphics":"silicon graphics","rog":"asus","aopen":"aopen","lyntek":"lyntek","firebox":"firebox","startech":"startech","startech.com":"startech", "StarTech":"startech", "marshall":"marshall","idesign":"idesign", "tripp":"tripp","boe hydis":"boehydis", "boehydis":"boehydis","medion":"medion","angel":"angel","advueu":"advueu","ingram":"ingram","norcent":"norcent","wren":"wren","xeno":"xeno", "sun microsystems":"sun microsystems","sunray":"sunray","emprex":"emprex"}
missing_brands=set()
items_with_missing_brands=set()
for item in brand_dict.keys():
    if not brand_dict[item] in brand_dict2:
        if brand_dict[item] in quick_fix:
            brand_dict[item] = quick_fix[brand_dict[item]]
        else:
            if (not brand_dict[item] in to_delete) and (not brand_dict[item] in to_delete_rules) and brand_dict[item]!="to_delete":
                missing_brands.add(brand_dict[item])
                items_with_missing_brands.add(item)
#print("Missing brands: ")
#print(sorted(list(missing_brands)))
will_delete=[]
will_keep=[]
will_keep_brands=[]
"""
Commented out by hand process...

start_pos=0
item_count=start_pos
for item in sorted(list(to_delete_files)[start_pos:]):
    f = open("2013_monitor_specs/"+item+".json")
    print(item) 
    data = json.load(f) 
    for i in sorted(list(data.keys())): 
        if not "â" in str(data[i]): 
            print(i+":"+str(data[i]))
    print("Reasons to delete: "+str(reasons_to_delete[item])) 
    print("Delete?")
    input_var = input("Delete? (y/n): ")
    print ("you entered " + input_var) 
    if "y" in input_var:
        will_delete.append(item)
    else:
        will_keep.append(item)  
        new_brand = input("Enter new brand: ")
        will_keep_brands.append(new_brand)
    print("*****************"+str(item_count)+"/"+str(len(to_delete_files))+"******************")
    item_count+=1
    if item_count%10==0:
        print("Will keep")
        print(will_keep)
        print("Will keep brands")
        print(will_keep_brands)        

print("You are done!")
print("Will keep")
print(will_keep)
print("Will keep brands")
print(will_keep_brands)
print("Will delete")
print(will_delete)

"""
will_keep=['catalog.com/266', 'catalog.com/337', 'catalog.com/402', 'catalog.com/619', 'ce.yikus.com/181', 'ce.yikus.com/537', 'www.best-deal-items.com/1005', 'www.best-deal-items.com/1011', 'www.best-deal-items.com/1033', 'www.best-deal-items.com/1041', 'www.best-deal-items.com/1071', 'www.best-deal-items.com/1085', 'www.best-deal-items.com/1123', 'www.best-deal-items.com/1214', 'www.best-deal-items.com/1229', 'www.best-deal-items.com/1286', 'www.best-deal-items.com/1287', 'www.best-deal-items.com/1324', 'www.best-deal-items.com/1335', 'www.best-deal-items.com/1352', 'www.best-deal-items.com/138', 'www.best-deal-items.com/1382', 'www.best-deal-items.com/1394', 'www.best-deal-items.com/1480', 'www.best-deal-items.com/1517', 'www.best-deal-items.com/1558', 'www.best-deal-items.com/1573', 'www.best-deal-items.com/1588', 'www.best-deal-items.com/159', 'www.best-deal-items.com/1679', 'www.best-deal-items.com/1717', 'www.best-deal-items.com/1788', 'www.best-deal-items.com/18', 'www.best-deal-items.com/1830', 'www.best-deal-items.com/1842', 'www.best-deal-items.com/1844', 'www.best-deal-items.com/1964', 'www.best-deal-items.com/2037', 'www.best-deal-items.com/2038', 'www.best-deal-items.com/2057', 'www.best-deal-items.com/2105', 'www.best-deal-items.com/2120', 'www.best-deal-items.com/2157', 'www.best-deal-items.com/2218', 'www.best-deal-items.com/227', 'www.best-deal-items.com/2365', 'www.best-deal-items.com/239', 'www.best-deal-items.com/2537', 'www.best-deal-items.com/2593', 'www.best-deal-items.com/2657', 'www.best-deal-items.com/2691', 'www.best-deal-items.com/2719', 'www.best-deal-items.com/2777', 'www.best-deal-items.com/28', 'www.best-deal-items.com/282', 'www.best-deal-items.com/430', 'www.best-deal-items.com/437', 'www.best-deal-items.com/509', 'www.best-deal-items.com/526', 'www.best-deal-items.com/591', 'www.best-deal-items.com/598', 'www.best-deal-items.com/628', 'www.best-deal-items.com/658', 'www.best-deal-items.com/702', 'www.best-deal-items.com/73', 'www.best-deal-items.com/742', 'www.best-deal-items.com/773', 'www.best-deal-items.com/780', 'www.best-deal-items.com/783', 'www.best-deal-items.com/857', 'www.best-deal-items.com/873', 'www.best-deal-items.com/969', 'www.cleverboxes.com/221', 'www.cleverboxes.com/516', 'www.ebay.com/10733', 'www.ebay.com/11317', 'www.ebay.com/11500', 'www.ebay.com/11630', 'www.ebay.com/15548', 'www.ebay.com/15955', 'www.ebay.com/16419', 'www.ebay.com/16801', 'www.ebay.com/18221', 'www.ebay.com/18538', 'www.ebay.com/18821', 'www.ebay.com/18895', 'www.ebay.com/18994', 'www.ebay.com/19324', 'www.ebay.com/19325', 'www.ebay.com/19400', 'www.ebay.com/19615', 'www.ebay.com/20048', 'www.ebay.com/20059', 'www.ebay.com/20238', 'www.ebay.com/20521', 'www.ebay.com/20534', 'www.ebay.com/20750', 'www.ebay.com/20913', 'www.ebay.com/21303', 'www.ebay.com/21325', 'www.ebay.com/21402', 'www.ebay.com/21445', 'www.ebay.com/21560', 'www.ebay.com/21566', 'www.ebay.com/21913', 'www.ebay.com/21991', 'www.ebay.com/22344', 'www.ebay.com/22569', 'www.ebay.com/22696', 'www.ebay.com/23445', 'www.ebay.com/23677', 'www.ebay.com/9507', 'www.ebay.com/9572', 'www.ebay.com/9639', 'www.ebay.com/9800', 'www.ebay.com/9809', 'www.pc-canada.com/315', 'www.pcconnection.com/1901', 'www.softwarecity.ca/1533']
will_keep_brands=['startech', 'startech', 'startech', 'startech', 'angel', 'angel', 'unbranded/generic', 'startech', 'acer', 'tripp', 'unbranded/generic', 'starlogic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'boehydis', 'medion', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'advueu', 'boscam', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'ingram', 'startech', 'unbranded/generic', 'norcent', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'tripp', 'unbranded/generic', 'unbranded/generic', 'nec', 'unbranded/generic', 'wren', 'unbranded/generic', 'xeno', 'sun microsystems', 'sunray', 'dell', 'unbranded/generic', 'tripp', 'unbranded/generic', 'acer', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'tripp', 'startech', 'startech', 'emprex', 'unbranded/generic', 'startech', 'unbranded/generic', 'unbranded/generic', 'startech', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'dell', 'ag neovo', 'ag neovo', 'touch controls inc', 'unbranded/generic', 'rca', 'mass multimedia', 'startech', 'arbor', 'touch controls inc', 'lenovo', 'touch displays', 'startech', 'dell', 'suntomo', 'tripp', 'wacom', 'unbranded/generic', 'norcent', 'startech', 'startech', 'dell', 'short-circuit.com', 'tripp', 'tripp', 'niko', 'startech', 'startech', 'tripp', 'unbranded/generic', 'angel', 'lilliput', 'tripp', 'ic power', 'tripp', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'tripp', 'hp', 'unbranded/generic', 'tripp', 'mgc', 'advueu', 'hp', 'tripp', 'hp']

for i in range(0,len(will_keep)):
    brand_dict[will_keep[i]]=will_keep_brands[i]

for item in to_delete_files:
    del brand_dict[item]

for item in to_delete_files_rules:
   with open("2013_monitor_specs/"+item+".json", 'r') as myfile:
       data = myfile.read().lower()
       if not "rack" in data:
           del brand_dict[item]


"""
Commented out by hand process...
start_pos=0
item_count=start_pos
will_keep2=[]
will_keep_brands2=[]
for item in sorted(list(items_with_missing_brands)[start_pos:]):
    f = open("2013_monitor_specs/"+item+".json")
    print(item) 
    data = json.load(f) 
    for i in sorted(list(data.keys())): 
        if not "â" in str(data[i]): 
            print(i+":"+str(data[i]))
    print("Delete?")
    input_var = input("Delete? (y/n): ")
    print ("you entered " + input_var) 
    if "y" in input_var:
        brand_dict[item]="to_delete"
    else:
        will_keep2.append(item)  
        new_brand = input("Enter new brand: ")
        will_keep_brands2.append(new_brand)
    print("*****************"+str(item_count)+"/"+str(len(items_with_missing_brands))+"******************")
    item_count+=1
    if item_count%10==0:
        print("Will keep2")
        print(will_keep2)
        print("Will keep brands")
        print(will_keep_brands2)        

print("Will keep")
print(will_keep2)
print("Will keep brands")
print(will_keep_brands2)
"""
will_keep2=['catalog.com/323', 'catalog.com/397', 'ce.yikus.com/264', 'ce.yikus.com/303', 'ce.yikus.com/814', 'www.best-deal-items.com/1023', 'www.best-deal-items.com/1037', 'www.best-deal-items.com/107', 'www.best-deal-items.com/1078', 'www.best-deal-items.com/1092', 'www.best-deal-items.com/1115', 'www.best-deal-items.com/1127', 'www.best-deal-items.com/1163', 'www.best-deal-items.com/1166', 'www.best-deal-items.com/1169', 'www.best-deal-items.com/1185', 'www.best-deal-items.com/1188', 'www.best-deal-items.com/1192', 'www.best-deal-items.com/1209', 'www.best-deal-items.com/1225', 'www.best-deal-items.com/1226', 'www.best-deal-items.com/1230', 'www.best-deal-items.com/1277', 'www.best-deal-items.com/1282', 'www.best-deal-items.com/1298', 'www.best-deal-items.com/1319', 'www.best-deal-items.com/1329', 'www.best-deal-items.com/1331', 'www.best-deal-items.com/1343', 'www.best-deal-items.com/1365', 'www.best-deal-items.com/1373', 'www.best-deal-items.com/1425', 'www.best-deal-items.com/1443', 'www.best-deal-items.com/1444', 'www.best-deal-items.com/1454', 'www.best-deal-items.com/1481', 'www.best-deal-items.com/1501', 'www.best-deal-items.com/1503', 'www.best-deal-items.com/1519', 'www.best-deal-items.com/1527', 'www.best-deal-items.com/155', 'www.best-deal-items.com/1559', 'www.best-deal-items.com/1602', 'www.best-deal-items.com/1620', 'www.best-deal-items.com/1625', 'www.best-deal-items.com/1626', 'www.best-deal-items.com/1630', 'www.best-deal-items.com/1645', 'www.best-deal-items.com/1656', 'www.best-deal-items.com/166', 'www.best-deal-items.com/1696', 'www.best-deal-items.com/1701', 'www.best-deal-items.com/1715', 'www.best-deal-items.com/1728', 'www.best-deal-items.com/1744', 'www.best-deal-items.com/1757', 'www.best-deal-items.com/1758', 'www.best-deal-items.com/1769', 'www.best-deal-items.com/1770', 'www.best-deal-items.com/1782', 'www.best-deal-items.com/179', 'www.best-deal-items.com/1821', 'www.best-deal-items.com/1823', 'www.best-deal-items.com/1824', 'www.best-deal-items.com/1826', 'www.best-deal-items.com/1848', 'www.best-deal-items.com/1854', 'www.best-deal-items.com/188', 'www.best-deal-items.com/1881', 'www.best-deal-items.com/1888', 'www.best-deal-items.com/189', 'www.best-deal-items.com/1906', 'www.best-deal-items.com/1929', 'www.best-deal-items.com/1940', 'www.best-deal-items.com/1942', 'www.best-deal-items.com/1953', 'www.best-deal-items.com/1957', 'www.best-deal-items.com/1972', 'www.best-deal-items.com/1988', 'www.best-deal-items.com/2003', 'www.best-deal-items.com/2013', 'www.best-deal-items.com/2021', 'www.best-deal-items.com/2060', 'www.best-deal-items.com/2062', 'www.best-deal-items.com/2071', 'www.best-deal-items.com/2095', 'www.best-deal-items.com/2098', 'www.best-deal-items.com/2132', 'www.best-deal-items.com/2133', 'www.best-deal-items.com/2138', 'www.best-deal-items.com/2139', 'www.best-deal-items.com/2151', 'www.best-deal-items.com/2170', 'www.best-deal-items.com/2190', 'www.best-deal-items.com/2199', 'www.best-deal-items.com/2213', 'www.best-deal-items.com/2220', 'www.best-deal-items.com/224', 'www.best-deal-items.com/2260', 'www.best-deal-items.com/2271', 'www.best-deal-items.com/2290', 'www.best-deal-items.com/2294', 'www.best-deal-items.com/2304', 'www.best-deal-items.com/231', 'www.best-deal-items.com/2325', 'www.best-deal-items.com/2340', 'www.best-deal-items.com/2344', 'www.best-deal-items.com/2348', 'www.best-deal-items.com/2364', 'www.best-deal-items.com/2413', 'www.best-deal-items.com/2423', 'www.best-deal-items.com/2424', 'www.best-deal-items.com/2441', 'www.best-deal-items.com/2459', 'www.best-deal-items.com/2469', 'www.best-deal-items.com/2471', 'www.best-deal-items.com/2504', 'www.best-deal-items.com/2509', 'www.best-deal-items.com/2530', 'www.best-deal-items.com/2534', 'www.best-deal-items.com/2570', 'www.best-deal-items.com/2577', 'www.best-deal-items.com/2578', 'www.best-deal-items.com/2607', 'www.best-deal-items.com/2614', 'www.best-deal-items.com/2616', 'www.best-deal-items.com/2661', 'www.best-deal-items.com/2662', 'www.best-deal-items.com/2669', 'www.best-deal-items.com/267', 'www.best-deal-items.com/2674', 'www.best-deal-items.com/2685', 'www.best-deal-items.com/2690', 'www.best-deal-items.com/2700', 'www.best-deal-items.com/2718', 'www.best-deal-items.com/274', 'www.best-deal-items.com/2768', 'www.best-deal-items.com/2776', 'www.best-deal-items.com/286', 'www.best-deal-items.com/293', 'www.best-deal-items.com/305', 'www.best-deal-items.com/385', 'www.best-deal-items.com/386', 'www.best-deal-items.com/396', 'www.best-deal-items.com/412', 'www.best-deal-items.com/424', 'www.best-deal-items.com/429', 'www.best-deal-items.com/520', 'www.best-deal-items.com/536', 'www.best-deal-items.com/546', 'www.best-deal-items.com/562', 'www.best-deal-items.com/580', 'www.best-deal-items.com/59', 'www.best-deal-items.com/592', 'www.best-deal-items.com/624', 'www.best-deal-items.com/634', 'www.best-deal-items.com/644', 'www.best-deal-items.com/666', 'www.best-deal-items.com/668', 'www.best-deal-items.com/69', 'www.best-deal-items.com/691', 'www.best-deal-items.com/701', 'www.best-deal-items.com/728', 'www.best-deal-items.com/729', 'www.best-deal-items.com/753', 'www.best-deal-items.com/761', 'www.best-deal-items.com/772', 'www.best-deal-items.com/787', 'www.best-deal-items.com/795', 'www.best-deal-items.com/811', 'www.best-deal-items.com/821', 'www.best-deal-items.com/822', 'www.best-deal-items.com/843', 'www.best-deal-items.com/854', 'www.best-deal-items.com/858', 'www.best-deal-items.com/870', 'www.best-deal-items.com/871', 'www.best-deal-items.com/874', 'www.best-deal-items.com/882', 'www.best-deal-items.com/891', 'www.best-deal-items.com/899', 'www.best-deal-items.com/906', 'www.best-deal-items.com/912', 'www.best-deal-items.com/917', 'www.best-deal-items.com/918', 'www.best-deal-items.com/948', 'www.best-deal-items.com/950', 'www.best-deal-items.com/978', 'www.best-deal-items.com/998', 'www.cleverboxes.com/206', 'www.cleverboxes.com/224', 'www.cleverboxes.com/291', 'www.cleverboxes.com/365', 'www.cleverboxes.com/368', 'www.cleverboxes.com/402', 'www.cleverboxes.com/481', 'www.cleverboxes.com/494', 'www.cleverboxes.com/63', 'www.cleverboxes.com/76', 'www.ebay.com/11016', 'www.ebay.com/11081', 'www.ebay.com/11203', 'www.ebay.com/11358', 'www.ebay.com/11443', 'www.ebay.com/11607', 'www.ebay.com/11794', 'www.ebay.com/11964', 'www.ebay.com/12114', 'www.ebay.com/14346', 'www.ebay.com/14551', 'www.ebay.com/14637', 'www.ebay.com/14697', 'www.ebay.com/15377', 'www.ebay.com/15481', 'www.ebay.com/15615', 'www.ebay.com/15648', 'www.ebay.com/16929', 'www.ebay.com/17016', 'www.ebay.com/17040', 'www.ebay.com/18090', 'www.ebay.com/18222', 'www.ebay.com/18303', 'www.ebay.com/18351', 'www.ebay.com/18797', 'www.ebay.com/18833', 'www.ebay.com/19014', 'www.ebay.com/19015', 'www.ebay.com/19097', 'www.ebay.com/19450', 'www.ebay.com/19527', 'www.ebay.com/19944', 'www.ebay.com/19961', 'www.ebay.com/20097', 'www.ebay.com/20159', 'www.ebay.com/20232', 'www.ebay.com/20416', 'www.ebay.com/20454', 'www.ebay.com/20565', 'www.ebay.com/20616', 'www.ebay.com/20686', 'www.ebay.com/20687', 'www.ebay.com/20767', 'www.ebay.com/21071', 'www.ebay.com/21078', 'www.ebay.com/21117', 'www.ebay.com/21298', 'www.ebay.com/21621', 'www.ebay.com/21634', 'www.ebay.com/21637', 'www.ebay.com/21666', 'www.ebay.com/21750', 'www.ebay.com/21893', 'www.ebay.com/21917', 'www.ebay.com/22297', 'www.ebay.com/22677', 'www.ebay.com/22811', 'www.ebay.com/22895', 'www.ebay.com/23034', 'www.ebay.com/23153', 'www.ebay.com/23179', 'www.ebay.com/23182', 'www.ebay.com/23300', 'www.ebay.com/23489', 'www.ebay.com/23684', 'www.ebay.com/9352', 'www.ebay.com/9914', 'www.getprice.com.au/148', 'www.getprice.com.au/195', 'www.getprice.com.au/226', 'www.getprice.com.au/237', 'www.getprice.com.au/239', 'www.getprice.com.au/286', 'www.getprice.com.au/298', 'www.getprice.com.au/304', 'www.getprice.com.au/306', 'www.getprice.com.au/332', 'www.getprice.com.au/336', 'www.getprice.com.au/347', 'www.getprice.com.au/376', 'www.hardware-planet.it/110', 'www.hardware-planet.it/111', 'www.hardware-planet.it/245', 'www.hardware-planet.it/5', 'www.hardware-planet.it/7', 'www.jrlinton.co.uk/1049', 'www.jrlinton.co.uk/1727', 'www.jrlinton.co.uk/464', 'www.jrlinton.co.uk/472', 'www.jrlinton.co.uk/632', 'www.jrlinton.co.uk/778', 'www.jrlinton.co.uk/817', 'www.jrlinton.co.uk/828', 'www.jrlinton.co.uk/836', 'www.jrlinton.co.uk/846', 'www.jrlinton.co.uk/860', 'www.jrlinton.co.uk/862', 'www.jrlinton.co.uk/888', 'www.jrlinton.co.uk/966', 'www.kingsfieldcomputers.co.uk/149', 'www.kingsfieldcomputers.co.uk/197', 'www.kingsfieldcomputers.co.uk/277', 'www.kingsfieldcomputers.co.uk/328', 'www.kingsfieldcomputers.co.uk/652', 'www.kingsfieldcomputers.co.uk/98', 'www.mediashopuk.com/0', 'www.mediashopuk.com/101', 'www.mediashopuk.com/104', 'www.mediashopuk.com/108', 'www.mediashopuk.com/112', 'www.mediashopuk.com/123', 'www.mediashopuk.com/13', 'www.mediashopuk.com/133', 'www.mediashopuk.com/17', 'www.mediashopuk.com/175', 'www.mediashopuk.com/19', 'www.mediashopuk.com/29', 'www.mediashopuk.com/3', 'www.mediashopuk.com/33', 'www.mediashopuk.com/37', 'www.mediashopuk.com/42', 'www.mediashopuk.com/45', 'www.mediashopuk.com/5', 'www.mediashopuk.com/52', 'www.mediashopuk.com/58', 'www.mediashopuk.com/86', 'www.mediashopuk.com/9', 'www.mrhightech.com/102', 'www.mrhightech.com/117', 'www.mrhightech.com/122', 'www.mrhightech.com/166', 'www.mrhightech.com/167', 'www.mrhightech.com/175', 'www.mrhightech.com/25', 'www.mrhightech.com/27', 'www.mrhightech.com/29', 'www.mrhightech.com/30', 'www.mrhightech.com/39', 'www.mrhightech.com/4', 'www.mrhightech.com/41', 'www.mrhightech.com/45', 'www.mrhightech.com/46', 'www.mrhightech.com/51', 'www.mrhightech.com/53', 'www.mrhightech.com/57', 'www.mrhightech.com/58', 'www.mrhightech.com/72', 'www.mrhightech.com/87', 'www.mrhightech.com/88', 'www.odsi.co.uk/108', 'www.odsi.co.uk/137', 'www.odsi.co.uk/140', 'www.odsi.co.uk/30', 'www.odsi.co.uk/32', 'www.odsi.co.uk/40', 'www.odsi.co.uk/49', 'www.odsi.co.uk/63', 'www.ohc24.ch/261', 'www.ohc24.ch/265', 'www.ohc24.ch/344', 'www.ohc24.ch/444', 'www.ohc24.ch/481', 'www.ohc24.ch/513', 'www.ohc24.ch/782', 'www.ohc24.ch/798', 'www.ohc24.ch/817', 'www.ohc24.ch/821', 'www.softwarecity.ca/1598', 'www.xpcpro.com/14', 'www.xpcpro.com/17', 'www.xpcpro.com/187', 'www.xpcpro.com/2', 'www.xpcpro.com/205', 'www.xpcpro.com/30', 'www.xpcpro.com/38', 'www.xpcpro.com/6', 'www.xpcpro.com/64', 'www.xpcpro.com/7', 'www.xpcpro.com/77', 'www.xpcpro.com/81', 'www.xpcpro.com/92']
will_keep_brands2=['unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'yiynova', 'yiynova', 'lucoms', 'unbranded/generic', 'unbranded/generic', 'neovo', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'no_comp', 'unbranded/generic', 'unbranded/generic', 'no_comp', 'ag neovo', 'unbranded/generic', 'no_comp', 'sensormatic', 'unbranded/generic', 'no_comp', 'eurosys', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'no_comp', 'unbranded/generic', 'belinea', 'unbranded/generic', 'unbranded/generic', 'silicon graphics', 'yusmart', 'unbranded/generic', 'emprex', 'videoseven', 'unbranded/generic', 'no_comp', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'belinea', 'unbranded/generic', 'unbranded/generic', 'no_comp', 'unbranded/generic', 'unbranded/Generic', 'iiyama', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generuc', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'matrox', 'no_comp', 'unbranded/generic', 'unbranded/generic', 'lyntek', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'funtica', 'unbranded/generic', 'unbranded/generic', 'bosch', 'unbranded/generic', 'silicon graphics', 'vibrant', 'skyport', 'unbranded/generic', 'unbranded/generic', 'no_comp', 'unbranded/generic', 'unbranded/generic', 'viglen', 'belinea', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'no_comp', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'alpha touch', 'unbranded/generic', 'medion', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'apple', 'unbranded/generic', 'digimate', 'unbranded/generic', 'jetway', 'unbranded/generic', 'unbranded/generic', 'aview', 'unbranded/generic', 'quanta', 'unbranded/generic', 'brilliance', 'lyntek', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'tenvis', 'sharp', 'advent', 'advent', 'unbranded/generic', 'hp', 'unbranded/generic', 'envision', 'unbranded/generic', 'megavision', 'elif brand_dict[item]=="unbranded_generuc"', 'unbranded/generic', 'bmw', 'unbranded/generic', 'belinea', 'nec', 'ikegami', 'unbranded/generic', 'vusys', 'unbranded/generic', 'unbranded/generic', 'harsper', 'unbranded/generic', 'unbranded/generic', 'angel', 'unbranded/generic', 'unbranded/generic', 'rackmux', 'unbranded/generic', 'unbranded/generic', 'envision', 'unbranded/generic', 'neova', 'yusmart', 'digimate', 'skyport', 'no_comp', 'unbranded/generic', 'belinea', 'unbranded/generic', 'belinea', 'austin hughes', 'belinea', 'unbranded/generic', 'digimate', 'hyvision', 'unbranded/generic', 'no_comp', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'iiyama', 'lucoms', 'no_comp', 'advent', 'unbranded/generic', 'tresor', 'unbranded/generic', 'unbranded/generic', 'iiyama', 'belinea', 'advent', 'sharp', 'unbranded/generic', 'viewsonic', 'medion', 'unbranded/generic', 'chunghwa', 'chatsworth', 'unbranded/generic', 'unbranded/generic', 'sharp', 'hannspree', 'hannspree', 'hannspree', 'hannspree', 'hannspree', 'hannspree', 'eaton', 'wasp', 'sharp', 'silicon graphics', 'sharp', 'envision', 'sunbrite', 'unbranded/generic', 'unbranded/generic', 'sharp', 'unbranded/generic', 'unbranded/generic', 'envision', 'envision', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'sharp', 'unbranded/generic', 'unbranded/generic', 'hitachi', 'sharp', 'hp', 'envision', 'unbranded/generic', 'hp', 'unbranded/generic', 'unbranded/generic', 'envision', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'envision', 'westinghouse', 'unbranded/generic', 'samsung', 'unbranded/generic', 'sharp', 'unbranded/generic', 'sharp', 'unbranded/generic', 'elite', 'unbranded/generic', 'zentview', 'unbranded/generic', 'unbranded/generic', 'sharp', 'envision', 'apple', 'knotron', 'unbranded/generic', 'unbranded/generic', 'sharp', 'bestech', 'unbranded/generic', 'unbranded/generic', 'gateway', 'hitachi', 'preh', 'crystalpro', 'balance', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'unbranded/generic', 'syncmaster', 'sva', 'unbranded/generic', 'starlogic', 'kogan', 'sunbrite', 'eizi', 'partnertech', 'puriton', 'kogan', 'sunbrite', 'sunbrite', 'sunbrite', 'sunbrite', 'sunbrite', 'sunbrite', 'sunbrite', 'hannspree', 'hannspree', 'hannspree', 'hannspree', 'hannspree', 'sharp', 'tv one', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'tv one', 'sharp', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'wortmann', 'sharp', 'nec', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'sharp', 'star micronics', 'neovo', 'roline', 'rotronic', 'rotronic', 'roline', 'roline', 'star micronics', 'intellinet', 'roline', 'sharp', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo', 'neovo']


for i in range(0,len(will_keep2)):
    brand_dict[will_keep2[i]]=will_keep_brands2[i]

items=list(brand_dict.keys())
for item in items:
    if brand_dict[item]=="to_delete":
        del brand_dict[item]
    elif brand_dict[item]=="unbranded_generuc":
        brand_dict[item]="unbranded/generic"
    elif brand_dict[item]=="unbranded/generuc":
        brand_dict[item]="unbranded/generic"
    elif brand_dict[item]=="unbranded/Generic":
        brand_dict[item]="unbranded/generic"
    elif brand_dict[item]=="envision":
        brand_dict[item]="envision monitors"
    elif "elif" in brand_dict[item]:
        brand_dict[item]="unbranded/generic"
brand_dict["catalog.com/323"]="sharp"
brand_dict["catalog.com/397"]="sharp"
brand_dict["www.best-deal-items.com/1166"]="boscam"
brand_dict["www.best-deal-items.com/1626"]="sharp"
brand_dict["www.best-deal-items.com/1953"]="alpha touch"
brand_dict["ce.yikus.com/264"]="envision"
items=list(brand_dict.keys())
for item in items:
    if brand_dict[item]=="no_comp":
        del brand_dict[item]
    elif brand_dict[item]=="N.A":
        del brand_dict[item]
brand_to_count=dict()
for item in brand_dict.keys():
    if not brand_dict[item] in brand_to_count:
        brand_to_count[brand_dict[item]]=1
    else:
        brand_to_count[brand_dict[item]]+=1
aux = [(brand_to_count[key], key) for key in brand_to_count]
aux.sort()
aux.reverse()
print(aux)
brands_at_the_end=set()
na_brands=set()
with open('final_brands.csv','a') as the_file:
    the_file.write("spec,brand\n")
    for item in sorted(list(brand_dict.keys())):
        the_file.write(item+","+str(brand_dict[item])+"\n")
import pickle
with open('brand_dict.pickle', 'wb') as handle:
    pickle.dump(brand_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

"""
unbranded_count=0
for item in brand_dict.keys():
    if brand_dict[item]=="unbranded/generic":
        unbranded_count+=1
        f = open("2013_monitor_specs/"+item+".json")
        data = json.load(f)
        print(str(unbranded_count)+" - "+item+" - "+str(data))
        print("----------------")
quit()
"""
data_keys=set()
model_dict=dict()
unknown_count=0
problems=set()
from_voting=set()
a=["thinkvision", "accusync","accutouch","acer", "thinkpad","syncmaster","prodisplay","pavilion","promaster","apple","flatron","dell","compaq", "acer", "aoc", "playstation","latitude","hp","asus","acerview", "asuspro", "benq","envy", "multisync", "radiforce","precision", "sparta", "brilliance", "cintiq", "deluxepro","dreamcolor","value","entuitive","foris","elitebook","intellitouch","mdcg","kingtee","prolite","smartbuy","sympodium","trutouch","viewsonic"]
for item in quick_fix.keys():
    if not type(quick_fix[item]) is list:
        quick_fix[item]=[quick_fix[item]]
del quick_fix["hanns g"]
del quick_fix["allen bradley"]

final_brand_dict = {**quick_fix, **brand_dict2}
final_brand_dict["envision monitors"]=["envision", "envision monitors"]
final_brand_dict["rockwell"]=["rockwell", "allen bradley", "allen-bradley"]
final_brand_dict["lyntek"]=["lynteck", "lyntek"]
fixes=set()
#sync master 151 v
#wasabi mango qhd275 supreme perfect pixel
import copy
bdd=copy.deepcopy(brand_dict)
brand_to_models=dict()
for item in bdd.keys():
    f = open("2013_monitor_specs/"+item+".json")
    data = json.load(f)
    search_for="nothing"
    if not bdd[item] in final_brand_dict:
        final_brand_dict[bdd[item]]=[bdd[item]]
   
    bd2=[x.lower() for x in final_brand_dict[bdd[item]]]
    bd2.append(bdd[item].lower())
    bd2=list(set(bd2))
    if "model" in data and str(data["model"]).lower() in str(data["<page title>"]).lower():
       search_for="model"
    elif "product model" in data and str(data["product model"]).lower() in str(data["<page title>"]).lower():
       search_for="product model"
    elif "product name" in data and str(data["product name"]).lower() in str(data["<page title>"]).lower():
       search_for="product name"
    elif "mpn" in data and str(data["mpn"]).lower() in str(data["<page title>"]).lower():
       search_for="mpn"
    elif "mfr part number" in data and str(data["mfr part number"]).lower() in str(data["<page title>"]).lower():
       search_for="mfr part number"
    elif "model name" in data and str(data["model name"]).lower() in str(data["<page title>"]).lower():
        search_for="model name"
    elif "series" in data and str(data["series"]).lower() in str(data["<page title>"]).lower():
       search_for="series"
    elif "model number" in data and str(data["model number"]).lower() in str(data["<page title>"]).lower():
       search_for="model number"
    elif "â model number" in data and str(data["â model number"]).lower() in str(data["<page title>"]).lower():
       search_for="â model number"
    elif "specifications" in data and str(data["specifications"]).lower() in str(data["<page title>"]).lower():
       search_for="specifications"
    elif "specs" in data and str(data["specs"]).lower() in str(data["<page title>"]).lower():
       search_for="specs"
    if search_for!="nothing":
        cand_model=str(data[search_for]).lower().replace("\n","").replace(":","").replace("'","").replace("\"","").strip()
        if (not " " in cand_model) and (cand_model not in bd2) and any(i.isdigit() for i in cand_model) and (cand_model not in a):
            for word in bd2:
                cand_model=cand_model.replace(word,"")
            cand_model=cand_model.replace("\n","").strip()
            if all(i.isdigit() for i in cand_model):
                if int(cand_model)<30:
                    model_dict[item]="unknown"
                elif len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                    if not bdd[item] in brand_to_models:
                        brand_to_models[bdd[item]]=set()
                    brand_to_models[bdd[item]].add(cand_model)
                    model_dict[item]=cand_model
            elif len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)
        elif cand_model[0]=="[" and cand_model[len(cand_model)-1]=="]":
            for word in bd2:
                cand_model=cand_model.replace(word,"")
            for word in a:
                cand_model=cand_model.replace(word,"")
            cand_model= cand_model.strip('][').split(', ')[1].split("\\n")[0].replace("\n","").replace("'","").replace("\"","").replace("\"","").strip()
            if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)        
        elif any(x in cand_model for x in ["x series","black tune","rog swift"]):
            for word in bd2:
                cand_model=cand_model.replace(word,"")
            for word in a:
                cand_model=cand_model.replace(word,"")
            cand_model= cand_model.replace("\n","").replace("'","").replace("\"","").replace("\"","").strip()
            if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)
        elif len(cand_model.split(" "))==2 and any(x in a for x in cand_model.split(" ")):
            for word in bd2:
                cand_model=cand_model.replace(word,"")
            for word in a:
                cand_model=cand_model.replace(word,"")
            cand_model=cand_model.replace("\n","").replace("'","").replace("\"","").replace("\"","").strip()
            if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)
        elif len(cand_model.split(" "))>2 and any(x in a for x in cand_model.split(" ")) and any(i.isdigit() for i in cand_model.split(" ")[1]):
            for word in bd2:
                cand_model=cand_model.replace(word,"")
            for word in a:
                cand_model=cand_model.replace(word,"")
            cand_model=(cand_model.split(" ")[0]+" "+cand_model.split(" ")[1]).replace("\n","").replace("'","").replace("\"","").strip()
            if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)
        elif len(cand_model.split(" "))>2 and any(x in a for x in [cand_model.replace(" led","").split(" ")[1]]) and any(i.isdigit() for i in cand_model.split(" ")[0]):
            cand_model=cand_model.replace(" led","")
            for word in bd2:
                cand_model=cand_model.replace(word,"")
            for word in a:
                cand_model=cand_model.replace(word,"")
            cand_model=(cand_model.split(" ")[0]+" "+cand_model.split(" ")[1]).replace("\n","").replace("'","").replace("\"","").strip()
            if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)
        elif "model" in cand_model:
            cand_model= cand_model.split("model")[1].split(" ")[0].replace("\n","").replace("'","").replace("\"","").strip()
            if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)
        #elif any(i.isdigit for i in cand_model.split(" ")[0]):
        #    cand_model=cand_model.split(" ")[0]
        #    if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
        #        model_dict[item]=cand_model
        #        if not bdd[item] in brand_to_models:
        #            brand_to_models[bdd[item]]=set()
        #        brand_to_models[bdd[item]].add(cand_model)
model_freq=dict()
for item in model_dict.keys():
    if not model_dict[item] in model_freq:
        model_freq[model_dict[item]]=1
    else:
        model_freq[model_dict[item]]+=1

for item in bdd.keys():
    f = open("2013_monitor_specs/"+item+".json")
    data = json.load(f)
    search_for="nothing"
    if not bdd[item] in final_brand_dict:
        final_brand_dict[bdd[item]]=[bdd[item]]
   
    bd2=[x.lower() for x in final_brand_dict[bdd[item]]]
    bd2.append(bdd[item].lower())
    bd2=list(set(bd2))
    if (not item in model_dict) or model_dict[item]=="unknown":
        model_chosen=False
        if bdd[item] in brand_to_models:
            inner_dict=dict() 
            for k in list(brand_to_models[bdd[item]]):
                inner_dict[k]=model_freq[k]
            for it in list(sorted(inner_dict, key=inner_dict.get, reverse=True)):
                if it in data["<page title>"].lower():
                    model_dict[item]=it
                    model_freq[it]+=1
                    model_chosen=True
                    from_voting.add(item)
                    break
            if not model_chosen:
                inner_dict=dict() 
                for k in list(brand_to_models[bdd[item]]):
                    inner_dict[k]=model_freq[k]
                for it in list(sorted(inner_dict, key=inner_dict.get, reverse=True)):
                    for key in data.keys():
                        if it in str(data[key]).lower():
                            model_dict[item]=it
                            model_freq[it]+=1
                            model_chosen=True
                            from_voting.add(item)
                            break
                    if model_chosen:
                        break

for item in bdd.keys():
    f = open("2013_monitor_specs/"+item+".json")
    data = json.load(f)
    search_for="nothing"
    if not bdd[item] in final_brand_dict:
        final_brand_dict[bdd[item]]=[bdd[item]]
    bd2=[x.lower() for x in final_brand_dict[bdd[item]]]
    bd2.append(bdd[item].lower())
    bd2=list(set(bd2))
    if (not item in model_dict) or model_dict[item]=="unknown":
        if any(x in bd2 for x in data["<page title>"].lower().replace("(","").replace(")","").split(" ")) or any([x in data["<page title>"].lower().replace("(","").replace(")","") for x in bd2]):
            brand_mention=""
            for word in bd2:
                if word in data["<page title>"].lower().replace("(","").replace(")","").split(" ") or word in data["<page title>"].lower().replace("(","").replace(")",""):
                    brand_mention=word
            cand_model=""
            string_to_search=data["<page title>"].lower().replace("(","").replace(")","").replace("\"","").split(brand_mention)[1]
            if len(string_to_search.split(" "))>1:
                string_to_search=string_to_search.split(" ")[1]
            else:
                string_to_search=data["<page title>"].lower().replace("(","").replace(")","").replace("\"","").split(" ")[0]
            if any(i.isdigit() for i in string_to_search):
                cand_model=string_to_search
            if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model) and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))):
                model_dict[item]=cand_model
                if not bdd[item] in brand_to_models:
                    brand_to_models[bdd[item]]=set()
                brand_to_models[bdd[item]].add(cand_model)
            else:
                strings_to_search=data["<page title>"].lower().replace("(","").replace(")","").replace("\"","").split(" ")
                longest_with_digits_and_letters=-1
                length_wdal=-1
                longest_with_digits=-1
                length_wd=-1
                for k in range(0,len(strings_to_search)):
                    sts=strings_to_search[k]
                    if any(i.isdigit() for i in sts):
                        if all(i.isdigit() for i in sts.replace("-","").replace(".","").replace(",","").replace("inch","").replace("\"","").replace(":","").replace("²","")) and len(sts)>length_wd:
                            length_wd=len(sts)
                            longest_with_digits=k
                        elif len(sts)>length_wdal:
                            length_wdal=len(sts)
                            longest_with_digits_and_letters=k
                if length_wdal>=3 and longest_with_digits_and_letters>=0 and ("\"" not in strings_to_search[longest_with_digits_and_letters]):
                    cand_model=strings_to_search[longest_with_digits_and_letters]
                    if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                        model_dict[item]=cand_model
                        if not bdd[item] in brand_to_models:
                            brand_to_models[bdd[item]]=set()
                        brand_to_models[bdd[item]].add(cand_model)
                elif length_wd>=3 and longest_with_digits>=0:
                    cand_model=strings_to_search[longest_with_digits]
                    if len(cand_model)>0 and cand_model not in stopwords and not(len(cand_model.split("."))=="2" and all(i.isdigit() for i in cand_model.replace(".",""))) and not all(i.isdigit() for i in cand_model):
                        model_dict[item]=cand_model
                        if not bdd[item] in brand_to_models:
                            brand_to_models[bdd[item]]=set()
                        brand_to_models[bdd[item]].add(cand_model)

model_freq=dict()
for item in model_dict.keys():
    if not model_dict[item] in model_freq:
        model_freq[model_dict[item]]=1
    else:
        model_freq[model_dict[item]]+=1
for item in bdd.keys():
    f = open("2013_monitor_specs/"+item+".json")
    data = json.load(f)
    search_for="nothing"
    if not bdd[item] in final_brand_dict:
        final_brand_dict[bdd[item]]=[bdd[item]]
   
    bd2=[x.lower() for x in final_brand_dict[bdd[item]]]
    bd2.append(bdd[item].lower())
    bd2=list(set(bd2))
    if (not item in model_dict) or model_dict[item]=="unknown":
        model_chosen=False
        if bdd[item] in brand_to_models: 
            inner_dict=dict()
            for k in list(brand_to_models[bdd[item]]):
                inner_dict[k]=model_freq[k]
            for it in list(sorted(inner_dict, key=inner_dict.get, reverse=True)):
                if it in data["<page title>"].lower():
                    model_dict[item]=it
                    model_freq[it]+=1
                    from_voting.add(item)
                    model_chosen=True
                    break
            if not model_chosen:
                inner_dict=dict() 
                for k in list(brand_to_models[bdd[item]]):
                    inner_dict[k]=model_freq[k]
                for it in list(sorted(inner_dict, key=inner_dict.get, reverse=True)):
                    for key in data.keys():
                        if it in str(data[key]).lower():
                            model_dict[item]=it
                            model_freq[it]+=1
                            model_chosen=True
                            from_voting.add(item)
                            break
                    if model_chosen:
                        break
        if not model_chosen:
            model_dict[item]="unknown"
            unknown_count+=1

#Final clean... (where we allow several items)
for item in bdd.keys():
    f = open("2013_monitor_specs/"+item+".json")
    data = json.load(f)
    if not bdd[item] in final_brand_dict:
        final_brand_dict[bdd[item]]=[bdd[item]]   
    bd2=[x.lower() for x in final_brand_dict[bdd[item]]]
    bd2.append(bdd[item].lower())
    bd2=list(set(bd2))
    if model_dict[item]!="unknown":# and item in from_voting:
        if bdd[item] in brand_to_models: 
            inner_dict=dict()
            for k in list(brand_to_models[bdd[item]]):
                inner_dict[k]=model_freq[k]
            for it in list(sorted(inner_dict, key=inner_dict.get, reverse=True)):
                if (it in data["<page title>"].lower()) and it!=model_dict[item] and model_freq[it]>model_freq[model_dict[item]]:
                    model_freq[model_dict[item]]-=1
                    model_dict[item]=it
                    model_freq[it]=+1
                    break
         
brand_to_items=dict()
for item in brand_dict:
    if brand_dict[item]!="unbranded/generic":
        if not brand_dict[item] in brand_to_items:
            brand_to_items[brand_dict[item]]=set([item])
        else:
            brand_to_items[brand_dict[item]].add(item)
#print(sorted(list(brand_to_items.keys()), key=len))  
print(sorted(list(set([model_dict[k] for k in model_dict.keys()]))))
#print("Problems")
#print(len(problems))
#for item in sorted(list(problems)):
#    print(item)
print("----------------------------------------------------")
print(brand_to_models)
print("----------------------------------------------------")
print("Unknown: "+str(unknown_count)+"/"+str(len(model_dict.keys())))
model_freq=dict()
for item in brand_dict.keys():
    if not model_dict[item] in model_freq:
        model_freq[model_dict[item]]=1
    else:
        model_freq[model_dict[item]]+=1
aux = [(model_freq[key], key) for key in model_freq]
aux.sort()
aux.reverse()
print(aux)


#for item in sorted(list(model_dict.keys())):
#    if model_dict[item]=="unknown":
#        f = open("2013_monitor_specs/"+item+".json")
#        data = json.load(f)
#        print(item+" "+data["<page title>"])


k=sorted(list(data_keys))
#for item in k:
#    print(item) 
from difflib import SequenceMatcher
import itertools
count1=0
count2=0
with open('model_dict.pkl', 'wb') as handle:
    pickle.dump(model_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('pairs_to_evaluate.csv','a') as the_file:
    the_file.write("left,right\n")
    for brand in brand_to_items:
        #print(brand_to_items[brand])
        pairs_to_evaluate=list(itertools.combinations(brand_to_items[brand], 2))
        #print(str(count1)+"/"+str(len(brand_to_items))+"- brands")
        #count2=0
        for item in pairs_to_evaluate:
            #print(str(count2)+"/"+str(len(pairs_to_evaluate))+"- items to compare")
            #print(item)
            #count2+=1    
            #f = open("2013_monitor_specs/"+item[0]+".json")
            #print(item[0]) 
            #data1 = json.load(f) 
            #for i in sorted(list(data.keys())): 
            #    if not "â" in str(data[i]): 
            #        print(i+":"+str(data[i]))
            #print("***")
            #f2 = open("2013_monitor_specs/"+item[1]+".json")
            #print(item[1]) 
            #data2 = json.load(f2) 
            #for i in sorted(list(data.keys())): 
            #    if not "â" in str(data[i]): 
            #        print(i+":"+str(data[i]))
            #print("Skip the comparison?")
            #input_var = input("Skip? (y/n) (b: next brand): ")
            #print ("you entered " + input_var) 
            #if input_var=='n':
            if model_dict[item[0]]!="unknown" and model_dict[item[1]]!="unknown" and (model_dict[item[0]]==model_dict[item[1]] or SequenceMatcher(None, model_dict[item[0]], model_dict[item[1]]).ratio() > 0.7):
                the_file.write(item[0]+","+item[1]+"\n")
        count1+=1
        print(str(count1)+"/"+str(len(brand_to_items))+" : "+brand)

