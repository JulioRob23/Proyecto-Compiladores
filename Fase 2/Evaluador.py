from proyectoVisitor import *
from proyectoParser import *
from proyectoListener import *

class Evaluador(proyectoVisitor):
    
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
        print("Visit: ATR")

        if ctx.TOTODILE() is not None: 
            return ctx.TOTODILE.getText()
        elif ctx.WOOPER() is not None: 
            return ctx.WOOPER.getText()
        elif ctx.PIKACHU() is not None: 
            return ctx.PIKACHU.getText()
        else: 
            return ctx.CORVIKNIGHT.getText()
    # Visit a parse tree produced by proyectoParser#atrl.
    def visitAtrl(self, ctx:proyectoParser.AtrlContext):
        print("Visit: ATRL")
        
        if ctx.INT() is not None:
            value = int(ctx.INT().getText())
            print(f"INT: {value}")
            return value
        elif ctx.FLOAT() is not None:
            value = float(ctx.FLOAT().getText())
            print(f"FLOAT: {value}")
            return value
        else : #ctx.INT() is not None :
            value = ctx.STRING().getText()
            print(f"STRING: {value}")
            return value


    # Visit a parse tree produced by proyectoParser#data.
    def visitData(self, ctx:proyectoParser.DataContext):
        return self.visitChildren(ctx)  