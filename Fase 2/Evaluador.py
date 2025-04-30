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
            return self.visit(ctx.line())
        return


    # Visit a parse tree produced by proyectoParser#line.
    def visitLine(self, ctx:proyectoParser.LineContext):
        if ctx.var() is not None:
            print(f"Visit LINE - {self.visit(ctx.var())}")
        elif ctx.condi() is not None:
            print(f"Visit LINE - {self.visit(ctx.condi())}")
        elif ctx.arith() is not None:
            print(f"Visit LINE - {self.visit(ctx.arith())}")
        elif ctx.func() is not None:
            print(f"Visit LINE - {self.visit(ctx.func())}")
        elif ctx.data() is not None:
            print(f"Visit LINE - {self.visit(ctx.data())}")
        elif ctx.UNOWN() is not None:
            print("Visit LINE - value: UNOWN")
        elif ctx.UNOWN() is not None and ctx.CHARMANDER() is not None:
            print("Visit LINE - vlaue: CHARMANDER UNOWN")
        else:
            print("Visit LINE - Línea vacía o no reconocida")
        return


    # Visit a parse tree produced by proyectoParser#var.
    def visitVar(self, ctx:proyectoParser.VarContext):
        if ctx.TOTODILE() is not None and ctx.ID() is not None and ctx.EQUAL() is not None:
            var_name = ctx.ID().getText().strip()
            if ctx.INT() is not None:
                value = int(ctx.INT().getText().strip())
                print(f"Visit VAR - TOTODILE {var_name} = {value}")
                self.varTOTODILE[var_name] = value
            elif ctx.arith() is not None:
                print(f"Visit VAR - TOTODILE {var_name} = Expresión aritmética")
                result = self.visit(ctx.arith())
                self.varTOTODILE[var_name] = result
            else:
                print("Visit VAR - TOTODILE: Error - Valor no especificado")
            if ctx.UNOWN() is not None:
                print("Visit VAR - UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
        elif ctx.WOOPER() is not None and ctx.ID() is not None and ctx.EQUAL() is not None and ctx.FLOAT() is not None:
            var_name = ctx.ID().getText().strip()
            value = float(ctx.FLOAT().getText().strip())
            print(f"Visit VAR - WOOPER {var_name} = {value}")
            self.varWOOPER[var_name] = value
            if ctx.UNOWN() is not None:
                print("Visit VAR - UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
        elif ctx.PIKACHU() is not None and ctx.ID() is not None and ctx.EQUAL() is not None and ctx.BOOL() is not None:
            var_name = ctx.ID().getText().strip()
            value = ctx.BOOL().getText().strip()
            print(f"Visit VAR - PIKACHU {var_name} = {value}")
            self.varPIKACHU[var_name] = value
            if ctx.UNOWN() is not None:
                print("Visit VAR - UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
        elif ctx.CORVIKNIGHT() is not None and ctx.ID() is not None and ctx.EQUAL() is not None and ctx.STRING() is not None:
            var_name = ctx.ID().getText().strip()
            value = ctx.STRING().getText().strip()
            print(f"Visit VAR - CORVIKNIGHT {var_name} = {value}")
            self.varCORVIKNIGHT[var_name] = value
            if ctx.UNOWN() is not None:
                print("Visit VAR - UNOWN")
            if ctx.line() is not None:
                self.visit(ctx.line())
        else:
            print("Visit VAR - Error: Estructura de variable no reconocida o incompleta")
        return

    # Visit a parse tree produced by proyectoParser#condi.
    def visitCondi(self, ctx:proyectoParser.CondiContext):
        if ctx.RATATA() is not None:
            if ctx.exp() and ctx.act() and ctx.CRESSELIA() and ctx.line():
                exp_val = self.visit(ctx.exp())
                act_val = self.visit(ctx.act())

                print(f"Visit CONDI - value: RATATA EXP: {exp_val} ACT: {act_val}")

                elif_else = ctx.elif_() is not None and ctx.else_() is not None
                if elif_else:
                    elif_val = self.visit(ctx.elif_())
                    else_val = self.visit(ctx.else_())

                    print(f"Visit CONDI - value: ELIF: {elif_val}  ELSE: {else_val}")

                elif ctx.elif_():
                    print(f"Visit CONDI - value: {self.visit(ctx.elif_())}")
                elif ctx.else_():
                    print(f"Visit CONDI - value: {self.visit(ctx.else_())}")
                print("Visit CONDI - value: CRESSELIA")
                if ctx.UNOWN():
                    print("Visit CONDI - value: UNOWN")
                self.visit(ctx.line())
            else:
                print("Visit CONDI - Error en bloque RATATA: faltan componentes")

        elif ctx.NECROZMA() is not None:
            if ctx.exp() and ctx.act() and ctx.CRESSELIA() and ctx.line():
                exp_val = self.visit(ctx.exp())
                act_val = self.visit(ctx.act())
                print(f"Visit CONDI - value: NECROZMA EXP: {exp_val} ACT: {act_val}")
                
                if ctx.UNOWN():
                    print("Visit CONDI - value: UNOWN")
                
                print("Visit CONDI - value: CRESSELIA")
                self.visit(ctx.line())
            else:
                print("Visit CONDI - Error en bloque NECROZMA: faltan componentes")

        else:
            print("Visit CONDI - Error: ni RATATA ni NECROZMA presente")


    # Visit a parse tree produced by proyectoParser#elif.
    def visitElif(self, ctx:proyectoParser.ElifContext):
        if ctx.PARAS() is not None and ctx.exp() is not None and ctx.act() is not None and ctx.elif_() is not None:
            exp_val = self.visit(ctx.exp())
            act_val = self.visit(ctx.act())
            elif_val = self.visit(ctx.elif_())

            print(f"Visit ELIF - Value: PARAS EXP: {exp_val}  ACT: {act_val} ELIF: {elif_val}")
        else:
            print("Error: ELIF incompleto")
        return


    # Visit a parse tree produced by proyectoParser#else.
    def visitElse(self, ctx:proyectoParser.ElseContext):
        if ctx.CLEFABLE() is not None:
            print("Visit ELSE - Value: CLEFABLE")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#exp.
    def visitExp(self, ctx:proyectoParser.ExpContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#extraf.
    def visitExtraf(self, ctx:proyectoParser.ExtrafContext):
        if ctx.COMA() is not None:
            if ctx.atr() is not None and ctx.ID() is not None:
                print("Visit EXTRAF - value: extra funcion")
                self.visit(ctx.atr())
                self.visit(ctx.ID())

                if ctx.extraf() is not None:
                    print(f"Visit EXTRAF - value: {self.visit(ctx.extraf())}")
                elif ctx.CLPA() is not None:
                    print("Visit EXTRAF - value: )")
                    self.visit(ctx.CLPA())
                else:
                    print("Visit EXTRAF - Error: falta extra funcion o )")
            else:
                print("Visit EXTRAF - Error en bloque: extra funcion incompleto")

    

      # Visit a parse tree produced by proyectoParser#extrac.
    def visitExtrac(self, ctx:proyectoParser.ExtracContext):
        if ctx.COMA() is not None:
            if ctx.atrl() is not None:
                print(f"Visit EXTRAC - value: {self.visit(ctx.atrl())}")  
            elif ctx.ID() is not None:
                print(f"Visit EXTRAC - value: {self.visit(ctx.ID())}")
            else:
                print("Visit EXTRAC - Error: falta atrl o ID")
                return 

            if ctx.extrac() is not None:
                print(f"Visit EXTRAC - value: {self.visit(ctx.extrac())}")
            elif ctx.CLPA() is not None:
                print("Visit EXTRAC - value: )")
                self.visit(ctx.CLPA())
            else:
                print("Visit EXTRAC - Error: falta extrac o )")
        else:
                print("Visit EXTRAC - Error en bloque: extra condicion incompleto")


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
            print("Visit DATA - value: DATA1")

            self.visit(ctx.atr())
            self.visit(ctx.ID())
            print("Visit DATA - value: = SEEL")

            if ctx.UNOWN() is not None:
                print("Visit DATA - value: UNOWN")

            if ctx.line() is not None:
                self.visit(ctx.line())

        elif ctx.DRAGONITE() is not None and ctx.OPA() is not None and ctx.CLPA() is not None:
            print("Visit DATA - value: DRAGONITE ( )")

            if ctx.atrl() is not None:
                print(f"Visit DATA - value: {self.visit(ctx.atrl())}")
            elif ctx.ID() is not None:
                print(f"Visit DATA - Value: {ctx.ID().getText().strip()}")
                self.visit(ctx.ID())
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