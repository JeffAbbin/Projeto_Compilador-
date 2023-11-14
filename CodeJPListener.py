# Generated from CodeJP.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CodeJPParser import CodeJPParser
else:
    from CodeJPParser import CodeJPParser

# This class defines a complete listener for a parse tree produced by CodeJPParser.
class CodeJPListener(ParseTreeListener):

    # Enter a parse tree produced by CodeJPParser#program.
    def enterProgram(self, ctx:CodeJPParser.ProgramContext):
        pass

    # Exit a parse tree produced by CodeJPParser#program.
    def exitProgram(self, ctx:CodeJPParser.ProgramContext):
        pass


    # Enter a parse tree produced by CodeJPParser#decls.
    def enterDecls(self, ctx:CodeJPParser.DeclsContext):
        pass

    # Exit a parse tree produced by CodeJPParser#decls.
    def exitDecls(self, ctx:CodeJPParser.DeclsContext):
        pass


    # Enter a parse tree produced by CodeJPParser#decl.
    def enterDecl(self, ctx:CodeJPParser.DeclContext):
        pass

    # Exit a parse tree produced by CodeJPParser#decl.
    def exitDecl(self, ctx:CodeJPParser.DeclContext):
        pass


    # Enter a parse tree produced by CodeJPParser#type.
    def enterType(self, ctx:CodeJPParser.TypeContext):
        pass

    # Exit a parse tree produced by CodeJPParser#type.
    def exitType(self, ctx:CodeJPParser.TypeContext):
        pass


    # Enter a parse tree produced by CodeJPParser#stmts.
    def enterStmts(self, ctx:CodeJPParser.StmtsContext):
        pass

    # Exit a parse tree produced by CodeJPParser#stmts.
    def exitStmts(self, ctx:CodeJPParser.StmtsContext):
        pass


    # Enter a parse tree produced by CodeJPParser#bool.
    def enterBool(self, ctx:CodeJPParser.BoolContext):
        pass

    # Exit a parse tree produced by CodeJPParser#bool.
    def exitBool(self, ctx:CodeJPParser.BoolContext):
        pass


    # Enter a parse tree produced by CodeJPParser#join.
    def enterJoin(self, ctx:CodeJPParser.JoinContext):
        pass

    # Exit a parse tree produced by CodeJPParser#join.
    def exitJoin(self, ctx:CodeJPParser.JoinContext):
        pass


    # Enter a parse tree produced by CodeJPParser#equality.
    def enterEquality(self, ctx:CodeJPParser.EqualityContext):
        pass

    # Exit a parse tree produced by CodeJPParser#equality.
    def exitEquality(self, ctx:CodeJPParser.EqualityContext):
        pass


    # Enter a parse tree produced by CodeJPParser#rel.
    def enterRel(self, ctx:CodeJPParser.RelContext):
        pass

    # Exit a parse tree produced by CodeJPParser#rel.
    def exitRel(self, ctx:CodeJPParser.RelContext):
        pass


    # Enter a parse tree produced by CodeJPParser#expr.
    def enterExpr(self, ctx:CodeJPParser.ExprContext):
        pass

    # Exit a parse tree produced by CodeJPParser#expr.
    def exitExpr(self, ctx:CodeJPParser.ExprContext):
        pass


    # Enter a parse tree produced by CodeJPParser#term.
    def enterTerm(self, ctx:CodeJPParser.TermContext):
        pass

    # Exit a parse tree produced by CodeJPParser#term.
    def exitTerm(self, ctx:CodeJPParser.TermContext):
        pass


    # Enter a parse tree produced by CodeJPParser#unary.
    def enterUnary(self, ctx:CodeJPParser.UnaryContext):
        pass

    # Exit a parse tree produced by CodeJPParser#unary.
    def exitUnary(self, ctx:CodeJPParser.UnaryContext):
        pass


    # Enter a parse tree produced by CodeJPParser#factor.
    def enterFactor(self, ctx:CodeJPParser.FactorContext):
        pass

    # Exit a parse tree produced by CodeJPParser#factor.
    def exitFactor(self, ctx:CodeJPParser.FactorContext):
        pass


    # Enter a parse tree produced by CodeJPParser#stmt.
    def enterStmt(self, ctx:CodeJPParser.StmtContext):
        pass

    # Exit a parse tree produced by CodeJPParser#stmt.
    def exitStmt(self, ctx:CodeJPParser.StmtContext):
        pass


    # Enter a parse tree produced by CodeJPParser#block.
    def enterBlock(self, ctx:CodeJPParser.BlockContext):
        pass

    # Exit a parse tree produced by CodeJPParser#block.
    def exitBlock(self, ctx:CodeJPParser.BlockContext):
        pass



del CodeJPParser