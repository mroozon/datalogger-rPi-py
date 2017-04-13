import os, datetime, fnmatch, json
from time import sleep


sensors = os.listdir("/sys/bus/w1/devices")

n = 5

while (n>0):
        print "Logging... %d" % n
        data = {}
        for sensor in sensors:
                if not fnmatch.fnmatch(sensor, 'w1_bus*'):
                        with open("/sys/bus/w1/devices/" + sensor + "/w1_slave") as fileobj:
                                lines = fileobj.readlines()
                                if lines[0].find("YES"):
                                        pok = lines[1].find('=')
                                        date = datetime.datetime.now().isoformat()
                                        temperature = float(lines[1][pok+1:pok+6])/1000
                                        data[date] = {sensor : temperature}
        #list.append(data)
        n -= 1
        with open('data.json', 'a') as outfile:
                json.dump(data, outfile)
                #if fnmatch.fnmatch(outfile, '}{'):
                #       print 'Nieprawidlowy format pliku'
#       sleep(1)
print "Done! Data saved in file: 'data.json'"
