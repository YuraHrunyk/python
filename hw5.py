import sys
import os
import sqlite3

path = sys.argv[1]


sql = '''SELECT ServerPorts.port_number
		FROM ServerTypes
		INNER JOIN Servers
		ON ServerTypes.id = Servers.servertypes_id
		INNER JOIN ServerPorts
		ON ServerPorts.servers_id = Servers.id
		INNER JOIN ServerProjects
		ON ServerProjects.servers_id = Servers.id
		WHERE ServerTypes.type_name = 'apache' AND ServerProjects.projects_id = '3';'''
conn = sqlite3.connect(path)
result = conn.execute(sql).fetchall()
conn.commit()

for row in result:
	print('PortNumber= ' + str(row[0]))

conn.close()
