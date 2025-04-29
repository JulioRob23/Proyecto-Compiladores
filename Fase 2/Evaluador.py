from proyectoVisitor import *
from proyectoParser import *
from proyectoListener import *

class Evaluador(proyectoVisitor):
    
    def __init__(self):
        self.varTOTODILE = {}
        self.varWOOPER = {}
        self.varPIKACHU = {}
        self.varCORVIKNIGHT = {}
        
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
        print("visit: EXP")
        mybool = True
        if ctx.BOOL() is not None or ctx.ID(1).getText().strip() in self.varPIKACHU: 
            if ctx.BOOL() is not None and ctx.BOOL().getText() == "0F" : 
                mybool = False
            elif ctx.BOOL() is not None and ctx.BOOL().getText() == "1V" : 
                mybool = True
            else: 
                mybool = self.varPIKACHU[ctx.ID(1).getText().strip()]
            condv = self.visit(ctx.condv())
            if ctx.ID(0).getText().strip() in self.varPIKACHU:
                if condv == "!=":
                    value = self.varPIKACHU[ctx.ID(0).getText().strip()]
                    if value != mybool: 
                        return True
                    else: 
                        return False
                elif condv == "=": 
                    value = self.varPIKACHU[ctx.ID(0).getText().strip()]
                    if value == mybool: 
                        return True
                    else: 
                        return False
                else: 
                    print("Error, operador invalido")
            else: 
                print("Error, variable no definida")
        else: 
            cond = self.visit(ctx.cond())
            if ctx.INT() is not None or ctx.ID(1).getText() in self.varTOTODILE :
                if ctx.INT() is not None: 
                    value2 = int(ctx.INT().getText())
                else: 
                    value2 = self.varTOTODILE[ctx.ID(1).getText()]
                value1 = self.varTOTODILE[ctx.ID(0).getText()]
                if cond == "<": 
                    if value1 < value2: 
                        return True
                    else: 
                        return False
                elif cond == "<=": 
                    if value1 <= value2: 
                        return True
                    else: 
                        return False
                elif cond == ">": 
                    if value1 > value2: 
                        return True
                    else: 
                        return False
                elif cond == ">=": 
                    if value1 >= value2: 
                        return True
                    else: 
                        return False
                elif cond == "!=": 
                    if value1 != value2: 
                        return True
                    else: 
                        return False
                else: 
                    if value1 == value2: 
                        return True
                    else: 
                        return False
            elif ctx.FLOAT() is not None or ctx.ID(1).getText() in self.varWOOPER :
                if ctx.FLOAT() is not None: 
                    value2 = float(ctx.INT().getText())
                else: 
                    value2 = self.varWOOPER[ctx.ID(1).getText()]
                value1 = self.varWOOPER[ctx.ID(0).getText]()
                if cond == "<": 
                    if value1 < value2: 
                        return True
                    else: 
                        return False
                elif cond == "<=": 
                    if value1 <= value2: 
                        return True
                    else: 
                        return False
                elif cond == ">": 
                    if value1 > value2: 
                        return True
                    else: 
                        return False
                elif cond == ">=": 
                    if value1 >= value2: 
                        return True
                    else: 
                        return False
                elif cond == "!=": 
                    if value1 != value2: 
                        return True
                    else: 
                        return False
                else: 
                    if value1 == value2: 
                        return True
                    else: 
                        return False
            elif ctx.STRING() is not None or ctx.ID(1).getText() in self.varCORVIKNIGHT :
                if ctx.STRING() is not None: 
                    value2 = ctx.INT().getText()
                else: 
                    value2 = self.varWOOPER[ctx.ID(1).getText()]
                value1 = self.varWOOPER[ctx.ID(0).getText()]
                if cond == "<": 
                    if value1 < value2: 
                        return True
                    else: 
                        return False
                elif cond == "<=": 
                    if value1 <= value2: 
                        return True
                    else: 
                        return False
                elif cond == ">": 
                    if value1 > value2: 
                        return True
                    else: 
                        return False
                elif cond == ">=": 
                    if value1 >= value2: 
                        return True
                    else: 
                        return False
                elif cond == "!=": 
                    if value1 != value2: 
                        return True
                    else: 
                        return False
                else: 
                    if value1 == value2: 
                        return True
                    else: 
                        return False
                
                
    # Visit a parse tree produced by proyectoParser#cond.
    def visitCond(self, ctx:proyectoParser.CondContext):
        if ctx.EXC() is not None: 
            exc = ctx.EXC().getText.strip()
            if ctx.EQUAL() is not None:
                equal = ctx.EQUAL().getText.strip()
                return  "" + exc + equal
            else: 
                return
        elif ctx.MINOR() is not None: 
            minor = ctx.MINOR().getText.strip()
            if ctx.EQUAL() is not None:
                equal = ctx.EQUAL().getText.strip()
                return  "" + minor + equal
            else: 
                return "" + minor
        elif ctx.BIGGER() is not None: 
            bigger = ctx.BIGGER().getText.strip()
            if ctx.EQUAL() is not None:
                equal = ctx.EQUAL().getText.strip()
                return  "" + bigger + equal
            else: 
                return "" + bigger
        elif ctx.EQUAL() is not None: 
            equal = ctx.EQUAL().getText.strip()
            return "" + equal
        else: 
            return

    # Visit a parse tree produced by proyectoParser#condv.
    def visitCondv(self, ctx:proyectoParser.CondvContext):
        print("Visit: CONDV")
        
        if ctx.EXC() is not None: 
            exc = ctx.EXC().getText.strip()
            if ctx.EQUAL() is not None:
                equal = ctx.EQUAL().getText.strip()
                return  "" + exc + equal
            else: 
                return
        elif ctx.EQUAL() is not None: 
            equal = ctx.EQUAL().getText.strip()
            return "" + equal
        else: 
            return

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
        print("Visit: UXIE")
        
        if ctx.ID() is not None: 
            value = int(ctx.ID.getText())
            print(f"ID: {value}")
            return value
        elif ctx.INT() is not None: 
            value = int(ctx.INT().getText())
            print(f"INT: {value}")
            return value
        else: 
            return self.visit(ctx.arith())
            

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