from proyectoVisitor import *
from proyectoParser import *
from proyectoListener import *

class Evaluador(proyectoVisitor):
    
    def __init__(self):
        self.varTOTODILE = {}
        self.varWOOPER = {}
        self.varPIKACHU = {}
        self.varCORVIKNIGHT = {}
        self.varGeneral = {}
        
    # Visit a parse tree produced by proyectoParser#start.
    def visitStart(self, ctx:proyectoParser.StartContext):
        if ctx.line() is not None:
            print("Visit START - value: line")
            self.visit(ctx.line())
        return


    # Visit a parse tree produced by proyectoParser#line.
    def visitLine(self, ctx:proyectoParser.LineContext):
        if ctx.var() is not None:
            print(f"Visit LINE - Declaracion de variable")
            self.visit(ctx.var())
        elif ctx.condi() is not None:
            print(f"Visit LINE - Ciclo con condicion")
            self.visit(ctx.condi())
        elif ctx.arith() is not None:
            print(f"Visit LINE - operacion aritmetica")
            self.visit(ctx.arith())
        elif ctx.func() is not None:
            print(f"Visit LINE - Funcion ")
            self.visit(ctx.func())
        elif ctx.data() is not None:
            print(f"Visit LINE - Manejo de datos")
            self.visit(ctx.data())
        elif ctx.UNOWN() is not None and ctx.CHARMANDER() is not None:
            print("Visit LINE - Final programa")
        elif ctx.UNOWN() is not None:
            print("Visit LINE - UNOWN")
        else:
            print("Visit LINE - Linea no reconocida")
        return


    # Visit a parse tree produced by proyectoParser#var.
    def visitVar(self, ctx:proyectoParser.VarContext):
        if ctx.TOTODILE() is not None and ctx.ID() is not None and ctx.EQUAL() is not None:
            var_name = ctx.ID().getText().strip()
            if ctx.INT() is not None:
                if var_name not in self.varGeneral:
                    value = int(ctx.INT().getText().strip())
                    print(f"Visit VAR - Declaracion entero para {var_name}")
                    self.varTOTODILE[var_name] = value
                    self.varGeneral[var_name] = value
                else: 
                    print("Error, ya existe la varible que intentas definir")
                    return
            elif ctx.arith() is not None:
                if var_name not in self.varGeneral:
                    print(f"Visit VAR - Declaracion entero con operacion aritmetica para {var_name} ")
                    self.visit(ctx.arith())
                    self.varTOTODILE[var_name] = -1
                else: 
                    print("Error, ya existe la varible que intentas definir")
                    return
            else:
                print("Visit VAR - TOTODILE: Error - Valor no especificado")
                return
            if ctx.UNOWN() is not None:
                print("Visit VAR entero- UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
            else:
                print("Error, falta fin de programa")
        elif ctx.WOOPER() is not None and ctx.ID() is not None and ctx.EQUAL() is not None and ctx.FLOAT() is not None:
            var_name = ctx.ID().getText().strip()
            if var_name not in self.varGeneral:
                value = float(ctx.FLOAT().getText().strip())
                print(f"Visit VAR - Declaracion flotante")
                self.varWOOPER[var_name] = value
            else: 
                    print("Error, ya existe la varible que intentas definir")
                    return
            if ctx.UNOWN() is not None:
                print("Visit VAR - UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
            else:
                print("Error, falta fin de programa")
        elif ctx.PIKACHU() is not None and ctx.ID() is not None and ctx.EQUAL() is not None and ctx.BOOL() is not None:
            var_name = ctx.ID().getText().strip()
            if var_name not in self.varGeneral:
                value = ctx.BOOL().getText().strip()
                print(f"Visit VAR - Declaracion booleano")
                self.varPIKACHU[var_name] = value
            else: 
                    print("Error, ya existe la varible que intentas definir")
                    return
            if ctx.UNOWN() is not None:
                print("Visit VAR - UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
            else:
                print("Error, falta fin de programa")
        elif ctx.CORVIKNIGHT() is not None and ctx.ID() is not None and ctx.EQUAL() is not None and ctx.STRING() is not None:
            var_name = ctx.ID().getText().strip()
            if var_name not in self.varGeneral:
                value = ctx.STRING().getText().strip()
                print(f"Visit VAR - Declaracion de string")
                self.varCORVIKNIGHT[var_name] = value
            else: 
                print("Error, ya existe la varible que intentas definir")
                return
            if ctx.UNOWN() is not None:
                print("Visit VAR - UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
            else:
                print("Error, falta fin de programa")
        else:
            print("Visit VAR - Error: Estructura de variable no reconocida o incompleta")
        return

    # Visit a parse tree produced by proyectoParser#condi.
    def visitCondi(self, ctx:proyectoParser.CondiContext):
        if ctx.RATATA() is not None:
            if ctx.exp() is not None and ctx.act() is not None and ctx.CRESSELIA()  is not None and ctx.line() is not None:
                print("Visit: CONDI - ciclo If")
                self.visit(ctx.exp())
                self.visit(ctx.act())

                if ctx.elif_() is not None and ctx.else_() is not None:
                    print(f"Visit CONDI - Extension: ELIF")
                    self.visit(ctx.elif_())
                    print(f"Visit CONDI - Extension: ELSE")
                    self.visit(ctx.else_())
                elif ctx.elif_():
                    print(f"Visit CONDI - Extension: ELIF")
                    self.visit(ctx.elif_())     
                elif ctx.else_():
                    print(f"Visit CONDI - Extension: ELSE")
                    self.visit(ctx.else_())
                    
                print("Visit CONDI - Fin de ciclo: CRESSELIA")
                if ctx.UNOWN():
                    print("Visit CONDI - value: UNOWN")
                if ctx.line() is not None:
                    self.visit(ctx.line())
                else:
                    print("Error, falta fin de programa")
            else:
                print("Visit CONDI - Error en bloque RATATA: faltan componentes")

        elif ctx.NECROZMA() is not None:
            if ctx.exp() is not None and ctx.act() is not None and ctx.CRESSELIA() is not None and ctx.line() is not None:
                print("Visit: CONDI - ciclo While")
                self.visit(ctx.exp())
                self.visit(ctx.act())
                                
                if ctx.UNOWN():
                    print("Visit CONDI - value: UNOWN")
                
                print("Visit CONDI - value: CRESSELIA")
                if ctx.line() is not None:
                    self.visit(ctx.line())
                else:
                    print("Error, falta fin de programa")
            else:
                print("Visit CONDI - Error en bloque NECROZMA: faltan componentes")

        else:
            print("Visit CONDI - Error: ni RATATA ni NECROZMA presente")


    # Visit a parse tree produced by proyectoParser#elif.
    def visitElif(self, ctx:proyectoParser.ElifContext):
        if ctx.PARAS() is not None and ctx.exp() is not None and ctx.act() is not None:
            self.visit(ctx.exp())
            self.visit(ctx.act())
            if ctx.elif_() is not None: 
                self.visit(ctx.elif_())
            return
        else:
            print("Error: ELIF incompleto")
        return


    # Visit a parse tree produced by proyectoParser#else.
    def visitElse(self, ctx:proyectoParser.ElseContext):
        if ctx.CLEFABLE() is not None:
            self.visit(ctx.else_())
        else: 
            print("Error: ELSE incompleto")
        return 


    # Visit a parse tree produced by proyectoParser#exp.
    def visitExp(self, ctx:proyectoParser.ExpContext):
        ids = ctx.ID()
        operador = ctx.cond().getText() if ctx.cond() else ctx.condv().getText()

        if len(ids) > 1:
            id1 = ids[0].getText()
            id2 = ids[1].getText()

            if id2 in self.varTOTODILE:
                valor = self.varTOTODILE[id2]
            elif id2 in self.varWOOPER:
                valor = self.varWOOPER[id2]
            elif id2 in self.varCORVIKNIGHT:
                valor = f"\"{self.varCORVIKNIGHT[id2]}\""
            elif id2 in self.varPIKACHU:
                valor = self.varPIKACHU[id2]
            elif id2 in self.varGeneral:
                valor = self.varGeneral[id2]
            else:
                valor = "<valor no encontrado>"
            
            print(f"VISIT EXP - {id1} {operador} {valor}")
            return f"{id1} {operador} {valor}"

        elif len(ids) == 1:
            id1 = ids[0].getText()

            if id1 not in self.varTOTODILE and id1 not in self.varWOOPER and \
            id1 not in self.varCORVIKNIGHT and id1 not in self.varPIKACHU and \
            id1 not in self.varGeneral:
                raise Exception(f"ERROR: variable '{id1}' no ha sido declarada")

            if ctx.INT():
                valor = ctx.INT().getText()
            elif ctx.FLOAT():
                valor = ctx.FLOAT().getText()
            elif ctx.STRING():
                valor = ctx.STRING().getText()
                valor = f"\"{valor}\""
            elif ctx.BOOL():
                valor = ctx.BOOL().getText()
            else:
                valor = "<valor desconocido>"

            print(f"VISIT EXP - {id1} {operador} {valor}")
            return f"{id1} {operador} {valor}"

        else:
            print("VISIT EXP - expresión no válida")


    # Visit a parse tree produced by proyectoParser#cond.
    def visitCond(self, ctx:proyectoParser.CondContext):
        if ctx.EXC() is not None and ctx.EQUAL() is not None:
            print("Visit COND - Value: !=")
        elif ctx.MINOR() is not None and ctx.EQUAL() is not None:
            print("Visit COND - Value: <=")
        elif ctx.BIGGER() is not None and ctx.EQUAL() is not None:
            print("Visit COND - Value: >=")
        elif ctx.MINOR() is not None:
            print("Visit COND - Value: <")
        elif ctx.BIGGER() is not None:
            print("Visit COND - Value: >")
        elif ctx.EQUAL() is not None:
            print("Visit COND - Value: =")
        else:
            print("Visit COND - Error: Operador desconocido")
        return


    # Visit a parse tree produced by proyectoParser#condv.
    def visitCondv(self, ctx:proyectoParser.CondvContext):
        if ctx.EXC() is not None and ctx.EQUAL() is not None:
            print("Visit CONDV - Value: !=")
        elif ctx.EQUAL() is not None:
            print("Visit CONDV - Value: =")
        else:
            print("Visit CONDV - Error: Operador desconocido")
        return


    # Visit a parse tree produced by proyectoParser#act.
    def visitAct(self, ctx:proyectoParser.ActContext):
        if ctx.UNOWN() is not None:
            print("Visit ACT - value: Unown")
        self.visit(ctx.line())
        return 


    # Visit a parse tree produced by proyectoParser#arith.
    def visitArith(self, ctx:proyectoParser.ArithContext):
        print("Visit ARITH ")
        if ctx.ID() is not None and ctx.EQUAL() is not None:
            print(f"Asignacion a : {ctx.ID().getText().strip()}")
        if ctx.xerneas() is not None: 
            self.visit(ctx.xerneas(0))
            if len(ctx.xerneas()) > 1: 
                idxxerneas = 1
                for child in ctx.children: 
                    if child.getText().strip() == "+": 
                        print("Operador - + ")
                        self.visit(ctx.xerneas(idxxerneas))
                        idxxerneas += 1
                    elif child.getText().strip() == "-":
                        print("Operador - - ")
                        self.visit(ctx.xerneas(idxxerneas))
                        idxxerneas += 1
                
            else: 
                return 
        else: 
            print("Error falta de operador")
            return


    # Visit a parse tree produced by proyectoParser#xerneas.
    def visitXerneas(self, ctx:proyectoParser.XerneasContext):
        print("Visit XERNEAS")
        if ctx.uxie(0) is not None:    
            self.visit(ctx.uxie(0))
            if len(ctx.uxie()) > 1: 
                idxuxie = 1
                for child in ctx.children: 
                    if child.getText().strip() == "*": 
                        print("Operador - * ")
                        self.visit(ctx.uxie(idxuxie))
                        idxuxie += 1
                    elif child.getText().strip() == "/":
                        print("Operador - / ")
                        self.visit(ctx.uxie(idxuxie))
                        idxuxie += 1
                    else: 
                        return
            else: 
                return
        else: 
            print("Error, falta de operador")
            return


    # Visit a parse tree produced by proyectoParser#uxie.
    def visitUxie(self, ctx:proyectoParser.UxieContext):
        if ctx.OPA() is not None:
            if ctx.CLPA() is not None: 
                print("Visit UXIE - Value: (")
                self.visit(ctx.arith())
                print("Visit UXIE - )")
            else: 
                print("Error, numero impar de parentesis")
        elif ctx.INT() is not None:
            print(f"Visit UXIE - Value: {int(ctx.INT().getText().strip())}")
        elif ctx.ID() is not None:
            print(f"Visit UXIE - Value: {ctx.ID().getText().strip()}")
        else: 
            print("Error, invalid value")
        return 

    # Visit a parse tree produced by proyectoParser#func.
    def visitFunc(self, ctx:proyectoParser.FuncContext):
        if ctx.TENTACOOL():

            if len(ctx.ID()) >= 2 and ctx.OPA() and ctx.atr():
                id1 = ctx.ID(0).getText()
                argumento = self.visit(ctx.atr())
                id2 = ctx.ID(1).getText()
                cierre = ctx.CLPA().getText() if ctx.CLPA() else self.visit(ctx.extraf)
                print(f"VISIT FUNC - {id1} ( {argumento} {id2} {cierre}")

            elif ctx.OPA() and ctx.CLPA():
                print("VISIT FUNC  - ()")

            if ctx.UNOWN():
                print("Visit ACT - value: Unown")

            self.visit(ctx.line(0))

            if ctx.MEWTWO():
                print("VISIT FUNC - MEWTWO")
                if ctx.ID(2):
                    print(f"VISIT FUNC -> ID2: {ctx.ID(2).getText()}")

            if ctx.UNOWN(1):
                print("Visit ACT - value: Unown")
            self.visit(ctx.line(1))

        else:
            if ctx.atr():
                atr_val = self.visit(ctx.atr())
                print(f"VISIT FUNC - {atr_val}")

            id_izq = ctx.ID(0).getText()
            if ctx.EQUAL():
                print(f"FUNC -> {ctx.EQUAL().getText()}")
            id_der = ctx.ID(1).getText()

            if ctx.OPA():
                op = ctx.OPA().getText()
                if ctx.atrl():
                    arg = self.visit(ctx.atrl())
                    cierre = ctx.CLPA().getText() if ctx.CLPA() else self.visit(ctx.extrac)
                    print(f"VISIT FUNC - {id_izq} = {id_der} {op}{arg}{cierre}")
                else:
                    print(f"VISIT FUNC -> {id_izq} = {id_der} ()")

            if ctx.UNOWN():
                print("Visit ACT - value: Unown")

            self.visit(ctx.line(0))

        return


    # Visit a parse tree produced by proyectoParser#extraf.
    def visitExtraf(self, ctx:proyectoParser.ExtrafContext):
        if ctx.COMA() is not None:
            if ctx.atr() is not None and ctx.ID() is not None:
                print("Visit EXTRAF - parametro extra")
                self.visit(ctx.atr())
                print(f"Nombre variable: {ctx.ID().getText().strip()}")

                if ctx.extraf() is not None:
                    self.visit(ctx.extraf())
                elif ctx.CLPA() is not None:
                    print("Visit EXTRAF - )")
                    self.visit(ctx.CLPA())
                else:
                    print("Visit EXTRAF - Error: falta extra funcion o )")
            else:
                print("Visit EXTRAF - Error en bloque: extra funcion incompleto")
        else:
            print("Formato incorrecto")
        return

    

      # Visit a parse tree produced by proyectoParser#extrac.
    def visitExtrac(self, ctx:proyectoParser.ExtracContext):
        if ctx.COMA() is not None:
            print("Visit EXTRAC - atributo extra")
            if ctx.atrl() is not None:
                print("Enviar atributo extra: ")
                self.visit(ctx.atrl())  
            elif ctx.ID() is not None:            
                if ctx.ID() in self.varGeneral:
                    print(f"Enviar atributo extra - variable: {ctx.ID().getText().strip()}")
            else:
                print("Visit EXTRAC - Error: falta atrl o ID")
                return 

            if ctx.extrac() is not None:
                self.visit(ctx.extrac())
            elif ctx.CLPA() is not None:
                print("Visit EXTRAC - )")
            else:
                print("Visit EXTRAC - Error: falta extrac o )")
        else:
                print("Visit EXTRAC - Error en bloque: extra condicion incompleto")
        return


    # Visit a parse tree produced by proyectoParser#atr.
    def visitAtr(self, ctx:proyectoParser.AtrContext):
        if ctx.TOTODILE() is not None: 
            print(f"Visit ATR - Value: Totodile")
        elif ctx.WOOPER() is not None: 
            print(f"Visit ATR - Value: Wooper")
        elif ctx.PIKACHU() is not None: 
            print(f"Visit ATR - Value: Pickachu")
        elif ctx.CORVIKNIGHT() is not None: 
            print(f"Visit ATR - Value: Corviknight")
        else: 
            print("Error, ATR -  invalid value")
        return 

    # Visit a parse tree produced by proyectoParser#atrl.
    def visitAtrl(self, ctx:proyectoParser.AtrlContext):
        if ctx.STRING() is not None: 
            print(f"Visit ATRL - Value: {ctx.STRING().getText().strip()} ")
        elif ctx.INT() is not None: 
            print(f"Visit ATRL - Value: {int(ctx.INT().getText().strip())}")
        elif ctx.FLOAT() is not None: 
            print(f"Visit ATRL - Value: {float(ctx.FLOAT().getText().strip())} ")
        else: 
            print("Error, ATRL - invalid value")
        return
    
    # Visit a parse tree produced by proyectoParser#data.
    def visitData(self, ctx:proyectoParser.DataContext):
        if ctx.atr() is not None and ctx.ID() is not None and ctx.EQUAL() is not None and ctx.SEEL() is not None:
            print("Visit DATA - Leer datos")

            self.visit(ctx.atr())
            
            if ctx.ID().getText.strip() in self.varGeneral:
                print(f"Variable a asignar: {ctx.ID().getText.strip()}")
                print("=")
            else: 
                print("Error, no existe la variable ")
                return

            if ctx.UNOWN() is not None:
                print("Visit DATA - value: UNOWN")

            if ctx.line() is not None:
                self.visit(ctx.line())
            else: 
                print("Error, falta fin de programa")
                return

        elif ctx.DRAGONITE() is not None and ctx.OPA() is not None and ctx.CLPA() is not None:
            print("Visit DATA - Mostrar datos")

            if ctx.atrl() is not None:
                self.visit(ctx.atrl())
            elif ctx.ID() is not None:
                if ctx.ID().getText().strip() in self.varGeneral:
                    print(f"Variable a mostrar {ctx.ID().getText().strip()}")
                else: 
                    print("Error, no existe la variable")
            else:
                print("Visit DATA - Error: falta atrl o ID")
                return

            if ctx.UNOWN() is not None:
                print("Visit DATA - Value: UNOWN")
                if ctx.line() is not None:
                    self.visit(ctx.line())
                return

        else:
            print("Visit DATA - Error: no coincide con ninguna opcion")