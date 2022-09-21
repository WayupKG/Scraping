from data.spreadsheets import spreadsheet_id, service


def save(data: list):
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "A1:D1",
                "majorDimension": "ROWS",
                "values": [["Название", "Цена", "Дата", "Ссылка на изображение"]]},
                {"range": "A:D",
                "majorDimension": "ROWS",
                "values": data}
            ]
        }
    ).execute()