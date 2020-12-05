import csv
from geopy.geocoders import Nominatim

def geo_loc(address):
    geolocator = Nominatim(user_agent="http")
    location = geolocator.geocode(address)
    try:
        return [location.latitude, location.longitude]
    except: # dirty data
        return []


def generate_list(file):
    with open(file, newline='') as csvfile:
        csvlist = []
        reader = csv.DictReader(csvfile)
        id = 0

        images = ["https://cdn.vox-cdn.com/thumbor/dIgp2rTgRWVe5RqZxsS6n2aWIik=/0x0:3200x2400/570x428/filters:focal(1344x944:1856x1456):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728608/TacoMapLittleTacoHouse.0.jpg",
        "https://cdn.vox-cdn.com/thumbor/7N-ELwR-aMgG-8gl8YmBE5YlZGY=/0x0:3200x2400/870x653/filters:focal(1344x944:1856x1456):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728607/TacoMapGlorias.0.jpg",
        "https://cdn.vox-cdn.com/thumbor/9WZva7Fg4TeIWXDkzZSSK71y0UE=/0x0:2048x1360/870x653/filters:focal(861x517:1187x843):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/66162713/BirriaTacos.0.jpg",
        "https://cdn.vox-cdn.com/thumbor/KcZGARj7ZLfVN_i9NHeziKdnkSk=/0x0:2048x1360/720x540/filters:focal(861x517:1187x843):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728603/TacoMapSinaloense.0.jpg"
        ]

        for row in reader:
            if row['Restaurant'] != "":
                d = {
                'id': id,
                'name': row['Restaurant'],
                'image': images[id%4],
                'text': row['Website'],
                'service': row['Service'],
                'location': row['Borough'],
                'address': geo_loc(row['Address']),
                'type': 'Restaurant',
                }
                id += 1
                csvlist.append(d)
                if id == 10:
                    return csvlist

        return csvlist
