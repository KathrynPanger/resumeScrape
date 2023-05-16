def reset_eof(pdfText):
    for i, x in enumerate(pdfText[::-1]):
        if b'%%EOF' in x:
            actual_line = len(pdfText) - i
            print(f'EOF found at line position {-i} = actual {actual_line}, with value {x}')
            break

            return pdfText[:actual_line]