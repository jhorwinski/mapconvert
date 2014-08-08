Public Sub ExportSheets(wbk As Workbook, sPath As String)
   Dim sht As Worksheet
   For Each sht In wbk.Worksheets
      sht.Select
      sht.SaveAs sPath & sht.Name & ".txt", XlFileFormat.xlTextMac
   Next sht
   wbk.Close
   MsgBox "Done exporting."
End Sub