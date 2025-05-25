from Evaluador import *
from proyectoLexer import *
from proyectoParser import *
from proyectoVisitor import *

input_stream1 = FileStream(r"Fase 1\prueba1.txt", encoding='utf-8')
input_stream2 = FileStream(r"Fase 1\prueba2.txt", encoding='utf-8')

#input_stream3 = FileStream(r"C:\Users\jujar\OneDrive\Escritorio\BackUp\U Landivar\Primer semestre 2025\Compiladores\Proyecto Compiladores\Fase 1\prueba3.txt", encoding='utf-8')
#input_stream4 = FileStream(r"C:\Users\jujar\OneDrive\Escritorio\BackUp\U Landivar\Primer semestre 2025\Compiladores\Proyecto Compiladores\Fase 1\prueba4.txt", encoding='utf-8')
#input_stream5 = FileStream(r"C:\Users\jujar\OneDrive\Escritorio\BackUp\U Landivar\Primer semestre 2025\Compiladores\Proyecto Compiladores\Fase 1\prueba5.txt", encoding='utf-8')
#input_stream6 = FileStream(r"C:\Users\jujar\OneDrive\Escritorio\BackUp\U Landivar\Primer semestre 2025\Compiladores\Proyecto Compiladores\Fase 1\prueba6.txt", encoding='utf-8')
#input_stream7 = FileStream(r"C:\Users\jujar\OneDrive\Escritorio\BackUp\U Landivar\Primer semestre 2025\Compiladores\Proyecto Compiladores\Fase 1\prueba7.txt", encoding='utf-8')
#input_stream8 = FileStream(r"C:\Users\jujar\OneDrive\Escritorio\BackUp\U Landivar\Primer semestre 2025\Compiladores\Proyecto Compiladores\Fase 1\prueba8.txt", encoding='utf-8')

try: 
    lexer = proyectoLexer(input_stream2)
    token_stream = CommonTokenStream(lexer)
    parser = proyectoParser(token_stream)

    tree = parser.start()

    visito = Evaluador()
    visito.visit(tree)
    visito.cerrar_archivo()
except Exception as e:
    print(e)
