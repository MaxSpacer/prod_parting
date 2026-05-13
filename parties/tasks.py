from django.tasks import task
import logging
from django.conf import settings
# logger = logging.getLogger(__name__)
# import os
from parties.scanner import barcode_reader


@task(takes_context=True, priority=1)
def scan_job(context, file_out):

    # file_out = os.path.join(
    #     settings.MEDIA_ROOT, filebrowser_file_name)

    with open(file_out, mode='w', newline='') as file_out:
        file_out.write('scanned_code' + "\n")
        
        # try:
        #     while True:
        #         # logging.debug("tsevcbcvbcvb----------rt: ",
        #         #                 filebrowser_file_name)
        #         scanned_code = barcode_reader()
        #         if scanned_code:
        #             file_out.write(scanned_code + "\n")
        #             file_out.flush()
        #             print(f"Сохранено: {scanned_code}")
        #             logging.debug(f"Сохранено: {scanned_code}")
        #         break
        # except KeyboardInterrupt:
        #     logging.debug('Keyboard interrupt')
        # except Exception as err:
        #     logging.error(err)

    logging.debug(
        f"Attempt {context.attempt} to send {file_out}. Task result id: {context.task_result.id}."
    )
    return {'report_party_file': str(file_out)}
