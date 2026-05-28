from django.shortcuts import render
from.models import Party
import pandas as pd
import os
import csv
from django.conf import settings
from django.http import HttpResponse


def create_xls(request, item):
    party = Party.objects.get(pk=item)
    
    file_name_xls = party.report_party_file.filename_root + '.xlsx'
    file_path_xls = os.path.join(settings.MEDIA_ROOT, file_name_xls) 

    if os.path.isfile(file_path_xls):
        os.remove(file_path_xls)

    with open(party.report_party_file.path_full, mode="r", encoding="utf-8") as csv_file, \
        pd.ExcelWriter(file_path_xls, engine="xlsxwriter") as writer:  
        csv_reader = csv.reader(csv_file)
        
        for index, row in enumerate(csv_reader):
            ro = row[0].split(chr(29))[0]
            df_row = pd.DataFrame([ro])
            df_row.to_excel(
                writer,
                sheet_name='sheet1',
                index=False,
                header=False,
                startrow=index  # Increments by 1 every loop to stack rows sequentially
            )

    with open(file_path_xls, 'rb') as f:
        response = HttpResponse(f.read(), content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name_xls)
        return response

def read_csv_file(request, item):
    party = Party.objects.get(pk=item)
    file_path = party.report_party_file.path_full
    context_data = []
    with open (file_path, 'r') as csvfile: 
        plotlist = csv.reader(csvfile, dialect=csv.excel_tab)
        for i, row in enumerate(plotlist, start = 1):
            context_data.append({'enum': i, 'row': row[0]})

    return render(request, 'parties/parties.html', {'context_data': context_data, 'party': party})
