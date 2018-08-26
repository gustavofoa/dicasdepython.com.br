import base64

texto = "um texto qualquer"
texto_em_bytearray = texto.encode('utf-8')

texto_em_base64 = base64.b64encode(texto_em_bytearray)

print(texto_em_base64)

texto_decriptado_em_byte_array = base64.b64decode(texto_em_base64)

texto_decriptado = texto_decriptado_em_byte_array.decode('utf-8')

print(texto_decriptado)