import MySQLdb
import commands
import sys
import os

bd = MySQLdb.connect("localhost","redinsa","Redinsa2015","base" )
cursor = bd.cursor()

##### Intensidades #####
I1 = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==18'")
resultado = commands.getoutput("calc %s/1000" % I1)
sql1 = "INSERT INTO intensidad1 (Servicio, Cantidad,Tabla) VALUES ('I1', '%s','intensidad1')" % resultado


I2 = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==20'")
resultado = commands.getoutput("calc %s/1000" % I2)
sql2 = "INSERT INTO intensidad2 (Servicio, Cantidad,Tabla) VALUES ('I2', '%s','intensidad2')" % resultado


I3 = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==22'")
resultado = commands.getoutput("calc %s/1000" % I3)
sql3 = "INSERT INTO intensidad3 (Servicio, Cantidad,Tabla) VALUES ('I3', '%s','intensidad3')" % resultado


In = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==24'")
resultado = commands.getoutput("calc %s/1000" % In)
sql4 = "INSERT INTO intensidadn (Servicio, Cantidad,Tabla) VALUES ('In', '%s','intensidadn')" % resultado


##### Tensiones #####
V12 = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==4'")
resultado = commands.getoutput("calc %s/100" % V12)
sql5 = "INSERT INTO tension12 (Servicio, Cantidad,Tabla) VALUES ('V12', '%s','tension12')" % resultado


V23 = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==6'")
resultado = commands.getoutput("calc %s/100" % V23)
sql6 = "INSERT INTO tension23 (Servicio, Cantidad,Tabla) VALUES ('V23', '%s','tension23')" % resultado


V31 = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==8'")
resultado = commands.getoutput("calc %s/100" % V31)
sql7 = "INSERT INTO tension31 (Servicio, Cantidad,Tabla) VALUES ('V31', '%s','tension31')" % resultado


V1n = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==10'")
resultado = commands.getoutput("calc %s/100" % V1n)
sql8 = "INSERT INTO tension1n (Servicio, Cantidad,Tabla) VALUES ('V1n', '%s','tension1n')" % resultado


V2n = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==12'")
resultado = commands.getoutput("calc %s/100" % V2n)
sql9 = "INSERT INTO tension2n (Servicio, Cantidad,Tabla) VALUES ('V2n', '%s','tension2n')" % resultado


V3n = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==14'")
resultado = commands.getoutput("calc %s/100" % V3n)
sql10 = "INSERT INTO tension3n (Servicio, Cantidad,Tabla) VALUES ('V3n', '%s','tension3n')" % resultado


##### Frecuencia #####
F = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==16'")
resultado = commands.getoutput("calc %s/100" % F)
sql11 = "INSERT INTO frecuencia (Servicio, Cantidad,Tabla) VALUES ('F', '%s','frecuencia')" % resultado


##### Potencia Activa #####
PAct = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 56 -s 50513 | awk 'NR==26'")
resultado = commands.getoutput("calc %s/100" % PAct)
sql12 = "INSERT INTO potenciaactiva (Servicio, Cantidad,Tabla) VALUES ('PAct', '%s','potenciaactiva')" % resultado



##### Energia Activa #####
EAct = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 2 -s 50851 | awk 'NR==2'")
sql13 = "INSERT INTO energiaactiva (Servicio, Cantidad,Tabla) VALUES ('EAct', '%s','energiaactiva')" % EAct



##### Energia Reactiva #####
EReact = commands.getoutput("/etc/nagios3/modbtget -H 196.168.30.130 -d 5 -f 3 -l 2 -s 50867 | awk 'NR==2'")
sql14 = "INSERT INTO energiareactiva (Servicio, Cantidad,Tabla) VALUES ('EReact', '%s','energiareactiva')" % EReact



cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)
cursor.execute(sql7)
cursor.execute(sql8)
cursor.execute(sql9)
cursor.execute(sql10)
cursor.execute(sql11)
cursor.execute(sql12)
cursor.execute(sql13)
cursor.execute(sql14)
bd.commit()
bd.close()


