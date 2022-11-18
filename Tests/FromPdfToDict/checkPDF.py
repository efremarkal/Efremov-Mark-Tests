import fitz  # pip install PyMuPDF

class CheckPDF:

    def __init__(self, path):
        self.path = path

    def checking(self):

        result = {}
        text = ''
        errors = 'ERRORS: \n'

        with fitz.Document(self.path) as doc:
            for page in doc:
                if 'page 1' in str(page):
                    errors = f'{errors} too many pages - should be 1 \n'
                    break
                text = f'COMPANY: {page.get_text()}'.replace(' : ', ':').replace(': ', ':').replace(' :', ':')

        textList = text.split('\n')

        while 'NOTES:' not in textList[-1]:  # concatenates 'NOTES' and 'inspection notes'
            textList[-2] = textList[-2] + textList[-1]
            textList.pop(-1)

        for line in textList:  # adds to dictionary
            try:
                result[line.split(":")[0]] = line.split(":")[1]
            except:
                continue

        for value in result.items():  # collect errors is some value or key is empty
            if value[1] == '':
                errors = f'{errors}{value[0]} has no value \n'
            if value[0] == '':
                errors = f'{errors}{value[1]} has no key \n'

        print(errors)
        return result


'''pdfFile = CheckPDF('test_task.pdf')
print(pdfFile.checking())'''