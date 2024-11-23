import csv

# Input and output file paths
def toHTML(csv_file_path):
    htmlString = ''

    # Read the CSV file
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        rows = list(csv_reader)

        htmlString += ('<div style="display: flex; justify-content: center; align-items: center;">\n')
        htmlString += ('<table border="1" style="margin: 20px auto;">\n')

        # Write table headers
        htmlString += ('<tr>\n')
        for header in headers:
            htmlString +=(f'<th>{header}</th>\n')
        htmlString +=('</tr>\n')

        # Write table rows
        for row in rows:
            htmlString += ('<tr>\n')
            for cell in row:
                htmlString += (f'<td>{cell}</td>\n')
            htmlString += ('</tr>\n')

        htmlString += ('</table>\n')
        htmlString += ('</div>\n')
        return(htmlString)
