#coding:utf-8
__author__ = 'johhny'
import xlwt
import StringIO
import mimetypes
from flask import Response
from werkzeug.datastructures import Headers

class export_excel():
    def export_download(self,file_name, sheet_name, headings, data, heading_xf, data_xfs):
        response = Response()
        response.status_code = 200


        ##################################
        # 新建excel并加入response对象
        ##################################
        book = xlwt.Workbook(encoding='UTF-8')
        sheet = book.add_sheet(sheet_name)
        rowx = 0
        for colx, value in enumerate(headings):
            sheet.write(rowx, colx, value, heading_xf)
        sheet.set_panes_frozen(True)
        sheet.set_horz_split_pos(rowx+1)
        sheet.set_remove_splits(True)
        for row in data:
            rowx += 1
            for colx, value in enumerate(row):
                sheet.write(rowx, colx, value, data_xfs[colx])

        output = StringIO.StringIO()
        book.save(output)
        response.data = output.getvalue()

        ################################
        # 提供jquery下载的报文头
        #################################
        filename = file_name
        mimetype_tuple = mimetypes.guess_type(filename)

        #HTTP下载报文头
        response_headers = Headers({
                'Pragma': "public",  # required,
                'Expires': '0',
                'Cache-Control': 'must-revalidate, post-check=0, pre-check=0',
                'Cache-Control': 'private',  # required for certain browsers,
                'Content-Type': mimetype_tuple[0],
                'Content-Disposition': 'attachment; filename=\"%s\";' % filename,
                'Content-Transfer-Encoding': 'binary',
                'Content-Length': len(response.data)
            })

        if not mimetype_tuple[1] is None:
            response.update({
                    'Content-Encoding': mimetype_tuple[1]
                })

        response.headers = response_headers

        #jquery.fileDownload.js
        response.set_cookie('fileDownload', 'true', path='/')

        return response