import csv


def store_suggestion(file, slist):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Type of Business', 'Borough',
                      'Service', 'Website', 'Image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in slist:
            writer.writerow({'Name': i["name"], 'Type of Business': i["type"],
                             'Borough': i["location"], 'Service': i["service"],
                             'Website': i["text"], 'Image': i["image"]})
