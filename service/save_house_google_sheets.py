from data.spreadsheets import spreadsheet_id, service

# сохраняет все данные в Google Sheets
def save(data: list) -> None:
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
    print("\n---- Все данные сохранены на Google Sheet ----\n")