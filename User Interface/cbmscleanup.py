import json

f = open('practiceValenzuela.json','w', encoding="utf-8")

with open('valenzuela_201702.json',encoding="utf-8") as z:
    for line in z:
        data = json.loads(line)
        f.write("{\"id\":\"")
        f.write(data['_id']['$oid'])
        f.write("\", \"latitude\":\"")
        if data['geopoint_hh']['latitude'] is None:
            f.write(str(0))
        else:
            f.write(data['geopoint_hh']['latitude'])
        f.write("\", \"longitude\":\"")
        if data['geopoint_hh']['longitude'] is None:
            f.write(str(0))
        else:
            f.write(data['geopoint_hh']['longitude'])
        f.write("\", \"hnum\":\"")
        if data['hnum'] is None:
            f.write(str(0))
        else:
            f.write(data['hnum'])
        f.write("\", \"house_type\":\"")
        if data['house_type'] is None:
            f.write(str(0))
        else:
            f.write(data['house_type'])
        f.write("\", \"nbr\":\"")
        if data['nbr'] is None:
            f.write(str(0))
        else:
            f.write(str(data['nbr']))
        f.write("\", \"phsize\":\"")
        if data['phsize'] is None:
            f.write(str(0))
        else:
            f.write(str(data['phsize']))
        f.write("\", \"car\":\"")
        if data['car'] is None:
            f.write(str(0))
        else:
            f.write(str(data['car']))
        f.write("\", \"motor\":\"")
        if data['motor'] is None:
            f.write(str(0))
        else:
            f.write(str(data['motor']))
        f.write("\", \"landagri\":\"")
        if data['landagri'] is None:
            f.write(str(0))
        else:
            f.write(str(data['landagri']))
        f.write("\", \"landres\":\"")
        if data['landres'] is None:
            f.write(str(0))
        else:
            f.write(str(data['landres']))
        f.write("\", \"landcomm\":\"")
        if data['landcomm'] is None:
            f.write(str(0))
        else:
            f.write(str(data['landcomm']))
        f.write("\", \"salind\":\"")
        if data['salind'] is None:
            f.write(str(0))
        else:
            f.write(data['salind'])
        f.write("\", \"servind\":\"")
        if data['servind'] is None:
            f.write(str(0))
        else:
            f.write(data['servind'])
        f.write("\", \"trnind\":\"")
        if data['trnind'] is None:
            f.write(str(0))
        else:
            f.write(data['trnind'])
        f.write("\", \"minind\":\"")
        if data['minind'] is None:
            f.write(str(0))
        else:
            f.write(data['minind'])
        f.write("\", \"totin\":\"")
        if data['totin'] is None:
            f.write(str(0))
        else:
            f.write(str(data['totin']))
        f.write("\", \"hpq_mem\":[")
        educind = 0
        jobind = 0
        fjob = 0
        ctr = 0
        for x in data['hpq_mem']:
            if x['educind'] is '1':
                educind = educind + 1
            if x['jobind'] is '1':
                jobind = jobind + 1
            if x['fjob'] is '1':
                fjob = fjob + 1
            if ctr != 0:
                f.write(", ")
            f.write("{")
            f.write("\"memno\":\"")
            if x['memno'] is None:
                f.write(str(0))
            else:
                f.write(x['memno'])
            f.write("\", ")
            f.write("\"educind\":\"")
            if x['educind'] is None:
                f.write(str(2))
            else:
                f.write(str(x['educind']))
            f.write("\", ")
            f.write("\"jobind\":\"")
            if x['jobind'] is None:
                f.write(str(2))
            else:
                f.write(str(x['jobind']))
            f.write("\", ")
            f.write("\"indust\":\"")
            f.write(x['indust'])
            f.write("\", ")
            f.write("\"fjob\":\"")
            if x['fjob'] is None:
                f.write(str(2))
            else:
                f.write(str(x['fjob']))
            f.write("\"}")
            ctr = ctr + 1
        f.write("], ")
        f.write("\"toteduc\":\"")
        f.write(str(educind))
        f.write("\", ")
        f.write("\"totjob\":\"")
        f.write(str(jobind))
        f.write("\", ")
        f.write("\"totfjob\":\"")
        f.write(str(fjob))
        f.write("\"}")
        f.write("\n")
f.close()
z.close()