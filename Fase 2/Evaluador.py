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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#exp.
    def visitExp(self, ctx:proyectoParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#cond.
    def visitCond(self, ctx:proyectoParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#condv.
    def visitCondv(self, ctx:proyectoParser.CondvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#act.
    def visitAct(self, ctx:proyectoParser.ActContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#arith.
    def visitArith(self, ctx:proyectoParser.ArithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#xerneas.
    def visitXerneas(self, ctx:proyectoParser.XerneasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#uxie.
    def visitUxie(self, ctx:proyectoParser.UxieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#func.
    def visitFunc(self, ctx:proyectoParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#extra.
    def visitExtra(self, ctx:proyectoParser.ExtraContext):
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