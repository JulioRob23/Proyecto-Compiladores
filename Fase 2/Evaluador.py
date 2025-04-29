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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#line.
    def visitLine(self, ctx:proyectoParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#var.
    def visitVar(self, ctx:proyectoParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#condi.
    def visitCondi(self, ctx:proyectoParser.CondiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#elif.
    def visitElif(self, ctx:proyectoParser.ElifContext):
        return self.visitChildren(ctx)


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
            print("Visit COND - Value: EXC EQUAL")
        elif ctx.EQUAL() is not None:
            print("Visit COND - Value: EQUAL")
        elif ctx.MINOR() is not None and ctx.EQUAL() is not None:
            print("Visit COND - Value: MINOR EQUAL")
        elif ctx.BIGGER() is not None and ctx.EQUAL() is not None:
            print("Visit COND - Value: BIGGER EQUAL")
        elif ctx.MINOR() is not None:
            print("Visit COND - Value: MINOR")
        elif ctx.BIGGER() is not None:
            print("Visit COND - Value: BIGGER")
        else:
            print("Visit COND - Error: Operador desconocido")
        return


    # Visit a parse tree produced by proyectoParser#condv.
    def visitCondv(self, ctx:proyectoParser.CondvContext):
        if ctx.EXC() is not None and ctx.EQUAL() is not None:
            print("Visit CONDV - Value: EXC EQUAL")
        elif ctx.EQUAL() is not None:
            print("Visit CONDV - Value: EQUAL")
        return


    # Visit a parse tree produced by proyectoParser#act.
    def visitAct(self, ctx:proyectoParser.ActContext):
        if ctx.UNOWN() is not None:
            print("Visit ACT - value: Unown")
        return self.visit(ctx.line())


    # Visit a parse tree produced by proyectoParser#arith.
    def visitArith(self, ctx:proyectoParser.ArithContext):
        if ctx.ID() is not None and ctx.EQUAL() is not None:
            print(f"Visit ARITH - value: {ctx.ID().getText().strip()}")
            self.visit(ctx.xerneas(0))
        for i in range(1, len(ctx.xerneas())):
            if ctx.PLUS() is not None:
                operador = "+"
            elif ctx.MINUS() is not None:
                operador = "-"
            else:
                operador = "ninguno"  
            print(f"Visit ARITH - value: {operador}")
            self.visit(ctx.xerneas(i))     
        return


    # Visit a parse tree produced by proyectoParser#xerneas.
    def visitXerneas(self, ctx:proyectoParser.XerneasContext):
         print("Visit XERNEAS - value: uxie")
         print("Visit XERNEAS - value: uxie")
         self.visit(ctx.uxie(0))
         for i in range(1, len(ctx.uxie())):
            if ctx.MUL() is not None:
                operador = "*"
            elif ctx.DIV() is not None:
                operador = "/"
            else:
                operador = "ninguno" 
            
            if operador:
                print(f"Visit XERNEAS - value: {operador}")
            
            print("Visit XERNEAS - value: uxie")
         return 


    # Visit a parse tree produced by proyectoParser#uxie.
    def visitUxie(self, ctx:proyectoParser.UxieContext):
        if ctx.OPA() is not None:

            print("Visit UXIE - Value: Paréntesis abierto")
            self.visit(ctx.arith())
            print("Visit UXIE - Paréntesis cerrado")
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
            print("Error, invalid value")
        return 

    # Visit a parse tree produced by proyectoParser#atrl.
    def visitAtrl(self, ctx:proyectoParser.AtrlContext):
        if ctx.STRING() is not None: 
            print(f"Visit ANTRL - Value: {ctx.STRING().getText().strip()} ")
        elif ctx.INT() is not None: 
            print(f"Visit ANTRL - Value: {int(ctx.INT().getText().strip())}")
        elif ctx.FLOAT() is not None: 
            print(f"Visit ANTL - Value: {float(ctx.FLOAT().getText().strip())} ")
        else: 
            print("Error, invalid value")
        return
    
    # Visit a parse tree produced by proyectoParser#data.
    def visitData(self, ctx:proyectoParser.DataContext):
        return self.visitChildren(ctx)