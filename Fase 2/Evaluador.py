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
        else:
            print("Visit START - Error: no se encontró línea")
        return


    # Visit a parse tree produced by proyectoParser#line.
    def visitLine(self, ctx:proyectoParser.LineContext):
        if ctx.var() is not None:
            print("Visit LINE - Variable")
            return self.visit(ctx.var())
        elif ctx.condi() is not None:
            print("Visit LINE - Condición")
            return self.visit(ctx.condi())
        elif ctx.arith() is not None:
            print("Visit LINE - Expresión aritmética")
            return self.visit(ctx.arith())
        elif ctx.func() is not None:
            print("Visit LINE - Función")
            return self.visit(ctx.func())
        elif ctx.data() is not None:
            print("Visit LINE - Datos")
            return self.visit(ctx.data())
        elif ctx.UNOWN() is not None:
            print("Visit LINE - UNOWN")
        elif ctx.UNOWN() is not None and ctx.CHARMANDER() is not None:
            print("Visit LINE - CHARMANDER UNOWN")
        else:
            print("Visit LINE - Línea vacía o no reconocida")
        return


    # Visit a parse tree produced by proyectoParser#var.
    def visitVar(self, ctx:proyectoParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#condi.
    def visitCondi(self, ctx:proyectoParser.CondiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#elif.
    def visitElif(self, ctx:proyectoParser.ElifContext):
        if ctx.PARAS() is not None and ctx.exp() is not None and ctx.act() is not None and ctx.elif_() is not None:
            print("Visit ELIF - Value: PARAS")
            self.visit(ctx.exp())
            self.visit(ctx.act())
            self.visit(ctx.elif_())
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
        return self.visitChildren(ctx)
    

      # Visit a parse tree produced by proyectoParser#extrac.
    def visitExtrac(self, ctx:proyectoParser.ExtracContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)