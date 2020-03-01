import os
import sqlite3

from scripts.ilapfuncs import logfunc, is_platform_windows 

def get_installedappsGass(files_found, report_folder):
        
    db = sqlite3.connect(files_found[0])
    cursor = db.cursor()
    cursor.execute('''
    SELECT 
        package_name 
        FROM
        app_info  
    ''')

    all_rows = cursor.fetchall()
    usageentries = len(all_rows)
    if usageentries > 0:
        with open(os.path.join(report_folder, 'Installed Apps (GMS).html'), 'w', encoding='utf8') as f:
            f.write('<html><body>')
            f.write('<h2> Installed Apps report</h2>')
            f.write(f'Installed Apps entries: {usageentries}<br>')
            f.write(f'Installed Apps list located at: {files_found[0]}<br>')
            f.write('<style> table, td {border: 1px solid black; border-collapse: collapse;}tr:nth-child(even) {background-color: #f2f2f2;} .table th { background: #888888; color: #ffffff}.table.sticky th{ position:sticky; top: 0; }</style>')
            f.write('<br/>')
            f.write('')
            f.write(f'<table class="table sticky">')
            f.write(f'<tr><th>Bundle ID</th></tr>')
            for row in all_rows:
                f.write(f'<tr><td>{row[0]}</td></tr>')
            f.write(f'</table></body></html>')
    else:
            logfunc('No Installed Apps data available')
    
    db.close()
    return