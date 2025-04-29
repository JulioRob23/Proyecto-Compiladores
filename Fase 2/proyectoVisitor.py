# Generated from proyecto.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .proyectoParser import proyectoParser
else:
    from proyectoParser import proyectoParser

# This class defines a complete generic visitor for a parse tree produced by proyectoParser.

class proyectoVisitor(ParseTreeVisitor):

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


    # Visit a parse tree produced by proyectoParser#extraf.
    def visitExtraf(self, ctx:proyectoParser.ExtrafContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#extrac.
    def visitExtrac(self, ctx:proyectoParser.ExtracContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#atr.
    def visitAtr(self, ctx:proyectoParser.AtrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#atrl.
    def visitAtrl(self, ctx:proyectoParser.AtrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoParser#data.
    def visitData(self, ctx:proyectoParser.DataContext):
        return self.visitChildren(ctx)



del proyectoParser