import sys
import os
import sqlite3

path = sys.argv[1]


sql = '''UPDATE ServerPorts
                SET port_number = '443'
                WHERE id in (SELECT ServerPorts.id
                FROM ServerTypes
                INNER JOIN Servers
                ON ServerTypes.id = Servers.servertypes_id
                INNER JOIN ServerPorts
                ON ServerPorts.servers_id = Servers.id
                INNER JOIN ServerProjects
                ON ServerProjects.servers_id = Servers.id
                WHERE ServerTypes.type_name = 'apache' AND ServerProjects.projects_id = 3);'''
conn = sqlite3.connect(path)
conn.execute(sql).fetchall()
conn.commit()

conn.close()

