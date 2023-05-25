## alunos: ISA STOHLER BERTOLACCINI e JEFFERSON SOBRINHO ABBIN
# Generated from PythonCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PythonCodeParser import PythonCodeParser
else:
    from PythonCodeParser import PythonCodeParser

# This class defines a complete listener for a parse tree produced by PythonCodeParser.
class PythonCodeListener(ParseTreeListener):

    # Enter a parse tree produced by PythonCodeParser#program.
    def enterProgram(self, ctx:PythonCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#program.
    def exitProgram(self, ctx:PythonCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#statement.
    def enterStatement(self, ctx:PythonCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#statement.
    def exitStatement(self, ctx:PythonCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:PythonCodeParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:PythonCodeParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#ifStatement.
    def enterIfStatement(self, ctx:PythonCodeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#ifStatement.
    def exitIfStatement(self, ctx:PythonCodeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#whileStatement.
    def enterWhileStatement(self, ctx:PythonCodeParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#whileStatement.
    def exitWhileStatement(self, ctx:PythonCodeParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PythonCodeParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PythonCodeParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#expressionStatement.
    def enterExpressionStatement(self, ctx:PythonCodeParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#expressionStatement.
    def exitExpressionStatement(self, ctx:PythonCodeParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#returnStatement.
    def enterReturnStatement(self, ctx:PythonCodeParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#returnStatement.
    def exitReturnStatement(self, ctx:PythonCodeParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#printStatement.
    def enterPrintStatement(self, ctx:PythonCodeParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#printStatement.
    def exitPrintStatement(self, ctx:PythonCodeParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#sleepStatement.
    def enterSleepStatement(self, ctx:PythonCodeParser.SleepStatementContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#sleepStatement.
    def exitSleepStatement(self, ctx:PythonCodeParser.SleepStatementContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#expressionList.
    def enterExpressionList(self, ctx:PythonCodeParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#expressionList.
    def exitExpressionList(self, ctx:PythonCodeParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#parameterList.
    def enterParameterList(self, ctx:PythonCodeParser.ParameterListContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#parameterList.
    def exitParameterList(self, ctx:PythonCodeParser.ParameterListContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#parameter.
    def enterParameter(self, ctx:PythonCodeParser.ParameterContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#parameter.
    def exitParameter(self, ctx:PythonCodeParser.ParameterContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#equality.
    def enterEquality(self, ctx:PythonCodeParser.EqualityContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#equality.
    def exitEquality(self, ctx:PythonCodeParser.EqualityContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#rel.
    def enterRel(self, ctx:PythonCodeParser.RelContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#rel.
    def exitRel(self, ctx:PythonCodeParser.RelContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#expression.
    def enterExpression(self, ctx:PythonCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#expression.
    def exitExpression(self, ctx:PythonCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:PythonCodeParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:PythonCodeParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#functionCall.
    def enterFunctionCall(self, ctx:PythonCodeParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#functionCall.
    def exitFunctionCall(self, ctx:PythonCodeParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#variable.
    def enterVariable(self, ctx:PythonCodeParser.VariableContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#variable.
    def exitVariable(self, ctx:PythonCodeParser.VariableContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#functionName.
    def enterFunctionName(self, ctx:PythonCodeParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#functionName.
    def exitFunctionName(self, ctx:PythonCodeParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by PythonCodeParser#binaryOperator.
    def enterBinaryOperator(self, ctx:PythonCodeParser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by PythonCodeParser#binaryOperator.
    def exitBinaryOperator(self, ctx:PythonCodeParser.BinaryOperatorContext):
        pass



del PythonCodeParser