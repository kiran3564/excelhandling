*** Settings ***

Library  ExcelLibrary
Library    QWeb

 

*** Test Cases ***

Write Data to Excel

    Open Excel  my_data.xls

    Put String To Cell  Sheet1  1  1  Hello, Copado!

    Save Excel

    Close All Excel Documents

I