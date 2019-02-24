class ErrorLexico(Exception):
    def __init__(self, caracter):
        self.caracterMalo = caracter


class C1:
    def __init__(self, lexema):
        self.lexema = lexema
        self.categoria = "C1"
    def __str__(self):
        return self.categoria + '(' + self.lexema + ')'

class C2:
    def __init__(self, lexema):
        self.lexema = lexema
        self.categoria = "C2"
    def __str__(self):
        return self.categoria + '(' + self.lexema + ')'

class Eof:
    def __init__(self):
        self.categoria = "Eof"
    def __str__(self):
        return self.categoria


class AnalizadorLexico:

    def __init__(self, entrada):
        self.entrada = entrada
        self.posicion = 0

        # self.sucesor[q][c] indica a que estado se llega desde el estado q con el caracter c
        self.sucesor = [{'a':1,'b':3,'c':5}, # desde el estado 0
                        {'b':2},             # desde el estado 1
                        {'b':1},             # desde el estado 2
                        {'c':4},             # desde el estado 3
                        {},                  # desde el estado 4
                        {}]                  # desde el estado 5

        # self.esFinal[q] indica si q es final
        self.esFinal = [False,True,False,False,True,True]

        # self.emitir[q] indica la categoria que se emite en q si es final y su accion es emitir,
        # y vale None si q no es final o si su accion es omitir
        self.emitir  = [None, C1, None, None, C2, None]

    def siguiente(self):

        estado = 0
        lexema = ""
        ultimoFinalVisitado = None

        while True:
            print ("Objeto : ", self)
            if self.posicion >= len(self.entrada):
                if estado == 0:
                    return Eof()
                caracter = '' # Representamos asi que no hay mas caracteres en la entrada
            else:
                caracter = self.entrada[self.posicion]

            if self.sucesor[estado].has_key(caracter): # Podemos avanzar

                if self.esFinal[estado]:
                    ultimoFinalVisitado = estado
                    lexemaAlPasarPorEstadoFinal = lexema
                    posicionAlPasarPorEstadoFinal = self.posicion
                self.posicion += 1
                lexema += caracter
                estado = self.sucesor[estado][caracter]

            else: # No podemos avanzar (incluye el caso en que no hay mas caracteres en la entrada)

                if self.esFinal[estado]:

                    if self.emitir[estado] != None:
                        return self.emitir[estado](lexema)
                    else: # Omitir
                        estado = 0
                        lexema = ""
                        ultimoFinalVisitado = None

                else: # No es final

                    if ultimoFinalVisitado != None:

                        if self.emitir[ultimoFinalVisitado] != None:
                            self.posicion = posicionAlPasarPorEstadoFinal
                            return self.emitir[ultimoFinalVisitado](lexemaAlPasarPorEstadoFinal)
                        else: # Omitir
                            estado = 0
                            lexema = ""
                            ultimoFinalVisitado = None
                    else:   
                        if lexema:
                            raise ErrorLexico(lexema[0])
                        else:
                            raise ErrorLexico(caracter)


pruebas = []
for pr in ["", "a", "b", "c", "ab", "abb", "abbb", "abbbb", "abbbbb", "bc", "abbbc", "abbbbbcccaba"]:
    pruebas.append(pr)
    pruebas.append(pr+'c')
    pruebas.append(pr+'d')

print ("(Datos de entrada) : ", pruebas)

for entrada in pruebas:

    print ("Analizando : ", entrada )
    
    anaLex = AnalizadorLexico(entrada)
    while True:
        try:
            token = anaLex.siguiente()
            if token.categoria == "Eof":
                break
        except excepcion:
            print ("Error lexico(" + excepcion.caracterMalo + ")")
            break
