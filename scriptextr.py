f=open("stdout.txt", "r")
contador=0
diccionario = {}
for line in (list(f)):
    contador=contador+1

    if "instanceID" in line and "complete data backup" in line:
        #print line
        vinicio=int(line.find("instanceID"))
        finicio=int(line.find("latestBackupStartTime"))
        IDbackup= int (line.find("latestBackupID"))
        SID= line[vinicio+12:vinicio+15]
        print ("Fecha respaldo nivel HANA: "+line[finicio+23:finicio+52])
        print ("Fecha respaldo nivel appmgr: "+line.rstrip()[0:26])
        print ("Instancia respaldada: "+ SID)
        print ("ID backup: "+ line[IDbackup+16:IDbackup+29])
        print ("Numero de linea :" + str(contador))
        print ("")
        diccionario[line[finicio+23:finicio+52]]={'SID':SID, 'ID':line[IDbackup+16:IDbackup+29],'Status':'n.a', 'HoraBackup':line[finicio+23:finicio+52] }



        #

        #print (line[1:6])
        ##Almacenar todo esto en un diccionario
g=open("stdout.txt","r")

while(True):
    linea = g.readline()
    if "Value" in linea and "successful" in linea:
        #print linea[7:-9]
        comparekey = g.readline()
        #print comparekey[7:36]
#        if comparekey[7:36] in diccionario:
        if diccionario.has_key(comparekey[7:36]):
            print (comparekey[7:36])
            diccionario[comparekey[7:36]]['Status'] = linea[7:-9]
            #print (diccionario[comparekey[7:36])
    if not linea:
        break
g.close()


#lineas=g.readline(5)

#print lineas
#for line in reversed(list(g)):
    #print(line)
print diccionario
        ##Tomar la variable del diccionario que traiga la hora nivel HANA, y anotar el value de
        ##la linea

for iteracion in diccionario:
    print diccionario[iteracion]

#<Value>successful</Value>




#[29 Apr 2020 08:53:03:701]/
