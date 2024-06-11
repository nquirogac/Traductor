# Generated from P:/Universidad/8 Semestre 2024-1/Lenguajes de Programacion/Trabajos en grupo/Traductor/grammar/LatinoGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,415,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,75,8,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,83,8,1,1,2,1,2,5,2,87,8,2,10,2,12,2,90,9,2,1,3,1,3,3,3,94,
        8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,5,6,105,8,6,10,6,12,6,108,
        9,6,1,6,1,6,1,6,1,6,5,6,114,8,6,10,6,12,6,117,9,6,1,7,1,7,5,7,121,
        8,7,10,7,12,7,124,9,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,5,9,139,8,9,10,9,12,9,142,9,9,1,9,5,9,145,8,9,10,9,12,
        9,148,9,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,159,8,9,1,10,1,
        10,1,10,1,10,1,10,1,11,1,11,3,11,168,8,11,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,5,13,179,8,13,10,13,12,13,182,9,13,3,13,184,
        8,13,1,13,1,13,4,13,188,8,13,11,13,12,13,189,1,13,1,13,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,207,
        8,15,10,15,12,15,210,9,15,3,15,212,8,15,1,15,1,15,1,16,1,16,1,16,
        5,16,219,8,16,10,16,12,16,222,9,16,3,16,224,8,16,1,17,1,17,1,17,
        5,17,229,8,17,10,17,12,17,232,9,17,1,17,3,17,235,8,17,3,17,237,8,
        17,1,18,1,18,1,18,1,18,5,18,243,8,18,10,18,12,18,246,9,18,1,19,1,
        19,1,19,5,19,251,8,19,10,19,12,19,254,9,19,1,19,1,19,5,19,258,8,
        19,10,19,12,19,261,9,19,1,19,1,19,1,19,1,19,5,19,267,8,19,10,19,
        12,19,270,9,19,1,19,1,19,1,19,1,19,3,19,276,8,19,1,20,1,20,1,20,
        1,20,1,20,1,20,3,20,284,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,21,5,21,294,8,21,10,21,12,21,297,9,21,3,21,299,8,21,1,21,1,21,
        4,21,303,8,21,11,21,12,21,304,1,22,1,22,1,22,4,22,310,8,22,11,22,
        12,22,311,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        4,23,325,8,23,11,23,12,23,326,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,3,24,337,8,24,1,24,1,24,3,24,341,8,24,1,24,1,24,4,24,345,8,
        24,11,24,12,24,346,1,25,1,25,4,25,351,8,25,11,25,12,25,352,1,25,
        1,25,1,25,1,26,1,26,1,26,4,26,361,8,26,11,26,12,26,362,1,26,5,26,
        366,8,26,10,26,12,26,369,9,26,1,26,3,26,372,8,26,1,27,1,27,1,27,
        4,27,377,8,27,11,27,12,27,378,1,28,1,28,4,28,383,8,28,11,28,12,28,
        384,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,4,30,395,8,30,11,30,
        12,30,396,1,30,4,30,400,8,30,11,30,12,30,401,1,30,1,30,1,30,1,30,
        1,30,4,30,409,8,30,11,30,12,30,410,3,30,413,8,30,1,30,0,0,31,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,0,1,1,0,1,4,450,0,65,1,0,0,0,2,82,1,0,0,0,4,84,
        1,0,0,0,6,93,1,0,0,0,8,95,1,0,0,0,10,99,1,0,0,0,12,106,1,0,0,0,14,
        118,1,0,0,0,16,125,1,0,0,0,18,158,1,0,0,0,20,160,1,0,0,0,22,167,
        1,0,0,0,24,169,1,0,0,0,26,173,1,0,0,0,28,193,1,0,0,0,30,197,1,0,
        0,0,32,223,1,0,0,0,34,236,1,0,0,0,36,238,1,0,0,0,38,275,1,0,0,0,
        40,283,1,0,0,0,42,287,1,0,0,0,44,306,1,0,0,0,46,313,1,0,0,0,48,328,
        1,0,0,0,50,348,1,0,0,0,52,357,1,0,0,0,54,373,1,0,0,0,56,380,1,0,
        0,0,58,386,1,0,0,0,60,412,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,
        67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,
        0,68,69,5,0,0,1,69,1,1,0,0,0,70,74,3,4,2,0,71,75,3,24,12,0,72,75,
        3,12,6,0,73,75,5,10,0,0,74,71,1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,
        0,75,83,1,0,0,0,76,83,3,38,19,0,77,83,3,36,18,0,78,83,3,50,25,0,
        79,83,3,40,20,0,80,83,3,20,10,0,81,83,5,16,0,0,82,70,1,0,0,0,82,
        76,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,0,
        0,82,81,1,0,0,0,83,3,1,0,0,0,84,88,5,41,0,0,85,87,3,6,3,0,86,85,
        1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,5,1,0,0,0,90,
        88,1,0,0,0,91,94,3,8,4,0,92,94,3,10,5,0,93,91,1,0,0,0,93,92,1,0,
        0,0,94,7,1,0,0,0,95,96,5,31,0,0,96,97,3,14,7,0,97,98,5,32,0,0,98,
        9,1,0,0,0,99,100,5,37,0,0,100,101,5,41,0,0,101,11,1,0,0,0,102,103,
        5,38,0,0,103,105,3,4,2,0,104,102,1,0,0,0,105,108,1,0,0,0,106,104,
        1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,106,1,0,0,0,109,110,
        5,5,0,0,110,115,3,22,11,0,111,112,5,38,0,0,112,114,3,22,11,0,113,
        111,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,
        13,1,0,0,0,117,115,1,0,0,0,118,122,3,18,9,0,119,121,3,16,8,0,120,
        119,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,
        15,1,0,0,0,124,122,1,0,0,0,125,126,7,0,0,0,126,127,3,18,9,0,127,
        17,1,0,0,0,128,129,5,33,0,0,129,130,3,14,7,0,130,131,5,34,0,0,131,
        159,1,0,0,0,132,159,5,42,0,0,133,159,5,43,0,0,134,159,5,6,0,0,135,
        159,5,7,0,0,136,140,5,41,0,0,137,139,3,6,3,0,138,137,1,0,0,0,139,
        142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,146,1,0,0,0,142,
        140,1,0,0,0,143,145,3,24,12,0,144,143,1,0,0,0,145,148,1,0,0,0,146,
        144,1,0,0,0,146,147,1,0,0,0,147,159,1,0,0,0,148,146,1,0,0,0,149,
        150,5,1,0,0,150,159,3,14,7,0,151,159,3,20,10,0,152,153,5,9,0,0,153,
        154,5,33,0,0,154,159,5,34,0,0,155,159,3,26,13,0,156,159,3,28,14,
        0,157,159,3,30,15,0,158,128,1,0,0,0,158,132,1,0,0,0,158,133,1,0,
        0,0,158,134,1,0,0,0,158,135,1,0,0,0,158,136,1,0,0,0,158,149,1,0,
        0,0,158,151,1,0,0,0,158,152,1,0,0,0,158,155,1,0,0,0,158,156,1,0,
        0,0,158,157,1,0,0,0,159,19,1,0,0,0,160,161,5,8,0,0,161,162,5,33,
        0,0,162,163,3,22,11,0,163,164,5,34,0,0,164,21,1,0,0,0,165,168,3,
        26,13,0,166,168,3,14,7,0,167,165,1,0,0,0,167,166,1,0,0,0,168,23,
        1,0,0,0,169,170,5,33,0,0,170,171,3,32,16,0,171,172,5,34,0,0,172,
        25,1,0,0,0,173,174,5,11,0,0,174,183,5,33,0,0,175,180,5,41,0,0,176,
        177,5,38,0,0,177,179,5,41,0,0,178,176,1,0,0,0,179,182,1,0,0,0,180,
        178,1,0,0,0,180,181,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,183,
        175,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,187,5,34,0,0,186,
        188,3,2,1,0,187,186,1,0,0,0,188,189,1,0,0,0,189,187,1,0,0,0,189,
        190,1,0,0,0,190,191,1,0,0,0,191,192,5,23,0,0,192,27,1,0,0,0,193,
        194,5,31,0,0,194,195,3,34,17,0,195,196,5,32,0,0,196,29,1,0,0,0,197,
        211,5,35,0,0,198,199,3,14,7,0,199,200,5,39,0,0,200,208,3,22,11,0,
        201,202,5,38,0,0,202,203,3,14,7,0,203,204,5,39,0,0,204,205,3,22,
        11,0,205,207,1,0,0,0,206,201,1,0,0,0,207,210,1,0,0,0,208,206,1,0,
        0,0,208,209,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,211,198,1,0,
        0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,5,36,0,0,214,31,1,0,
        0,0,215,220,3,22,11,0,216,217,5,38,0,0,217,219,3,22,11,0,218,216,
        1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,224,
        1,0,0,0,222,220,1,0,0,0,223,215,1,0,0,0,223,224,1,0,0,0,224,33,1,
        0,0,0,225,230,3,22,11,0,226,227,5,38,0,0,227,229,3,22,11,0,228,226,
        1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,234,
        1,0,0,0,232,230,1,0,0,0,233,235,5,38,0,0,234,233,1,0,0,0,234,235,
        1,0,0,0,235,237,1,0,0,0,236,225,1,0,0,0,236,237,1,0,0,0,237,35,1,
        0,0,0,238,239,5,12,0,0,239,244,3,22,11,0,240,241,5,38,0,0,241,243,
        3,22,11,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,37,1,0,0,0,246,244,1,0,0,0,247,248,5,15,0,0,248,252,
        5,33,0,0,249,251,3,22,11,0,250,249,1,0,0,0,251,254,1,0,0,0,252,250,
        1,0,0,0,252,253,1,0,0,0,253,259,1,0,0,0,254,252,1,0,0,0,255,256,
        5,38,0,0,256,258,3,22,11,0,257,255,1,0,0,0,258,261,1,0,0,0,259,257,
        1,0,0,0,259,260,1,0,0,0,260,262,1,0,0,0,261,259,1,0,0,0,262,276,
        5,34,0,0,263,264,5,14,0,0,264,268,5,33,0,0,265,267,3,22,11,0,266,
        265,1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,
        271,1,0,0,0,270,268,1,0,0,0,271,276,5,34,0,0,272,273,5,13,0,0,273,
        274,5,33,0,0,274,276,5,34,0,0,275,247,1,0,0,0,275,263,1,0,0,0,275,
        272,1,0,0,0,276,39,1,0,0,0,277,284,3,42,21,0,278,284,3,44,22,0,279,
        284,3,46,23,0,280,284,3,48,24,0,281,284,3,52,26,0,282,284,3,58,29,
        0,283,277,1,0,0,0,283,278,1,0,0,0,283,279,1,0,0,0,283,280,1,0,0,
        0,283,281,1,0,0,0,283,282,1,0,0,0,284,285,1,0,0,0,285,286,5,23,0,
        0,286,41,1,0,0,0,287,288,5,11,0,0,288,289,5,41,0,0,289,298,5,33,
        0,0,290,295,5,41,0,0,291,292,5,38,0,0,292,294,5,41,0,0,293,291,1,
        0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,299,1,
        0,0,0,297,295,1,0,0,0,298,290,1,0,0,0,298,299,1,0,0,0,299,300,1,
        0,0,0,300,302,5,34,0,0,301,303,3,2,1,0,302,301,1,0,0,0,303,304,1,
        0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,43,1,0,0,0,306,307,5,24,
        0,0,307,309,3,14,7,0,308,310,3,2,1,0,309,308,1,0,0,0,310,311,1,0,
        0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,45,1,0,0,0,313,314,5,25,
        0,0,314,315,5,33,0,0,315,316,3,4,2,0,316,317,5,5,0,0,317,318,3,14,
        7,0,318,319,5,40,0,0,319,320,3,14,7,0,320,321,5,40,0,0,321,322,3,
        2,1,0,322,324,5,34,0,0,323,325,3,2,1,0,324,323,1,0,0,0,325,326,1,
        0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,47,1,0,0,0,328,329,5,26,
        0,0,329,330,5,41,0,0,330,331,5,27,0,0,331,332,5,28,0,0,332,333,5,
        33,0,0,333,336,3,14,7,0,334,335,5,38,0,0,335,337,3,14,7,0,336,334,
        1,0,0,0,336,337,1,0,0,0,337,340,1,0,0,0,338,339,5,38,0,0,339,341,
        3,14,7,0,340,338,1,0,0,0,340,341,1,0,0,0,341,342,1,0,0,0,342,344,
        5,34,0,0,343,345,3,2,1,0,344,343,1,0,0,0,345,346,1,0,0,0,346,344,
        1,0,0,0,346,347,1,0,0,0,347,49,1,0,0,0,348,350,5,29,0,0,349,351,
        3,2,1,0,350,349,1,0,0,0,351,352,1,0,0,0,352,350,1,0,0,0,352,353,
        1,0,0,0,353,354,1,0,0,0,354,355,5,30,0,0,355,356,3,14,7,0,356,51,
        1,0,0,0,357,358,5,20,0,0,358,360,3,14,7,0,359,361,3,2,1,0,360,359,
        1,0,0,0,361,362,1,0,0,0,362,360,1,0,0,0,362,363,1,0,0,0,363,367,
        1,0,0,0,364,366,3,54,27,0,365,364,1,0,0,0,366,369,1,0,0,0,367,365,
        1,0,0,0,367,368,1,0,0,0,368,371,1,0,0,0,369,367,1,0,0,0,370,372,
        3,56,28,0,371,370,1,0,0,0,371,372,1,0,0,0,372,53,1,0,0,0,373,374,
        5,21,0,0,374,376,3,14,7,0,375,377,3,2,1,0,376,375,1,0,0,0,377,378,
        1,0,0,0,378,376,1,0,0,0,378,379,1,0,0,0,379,55,1,0,0,0,380,382,5,
        22,0,0,381,383,3,2,1,0,382,381,1,0,0,0,383,384,1,0,0,0,384,382,1,
        0,0,0,384,385,1,0,0,0,385,57,1,0,0,0,386,387,5,19,0,0,387,388,3,
        14,7,0,388,389,3,60,30,0,389,59,1,0,0,0,390,391,5,17,0,0,391,392,
        3,14,7,0,392,393,5,39,0,0,393,395,1,0,0,0,394,390,1,0,0,0,395,396,
        1,0,0,0,396,394,1,0,0,0,396,397,1,0,0,0,397,399,1,0,0,0,398,400,
        3,2,1,0,399,398,1,0,0,0,400,401,1,0,0,0,401,399,1,0,0,0,401,402,
        1,0,0,0,402,403,1,0,0,0,403,404,3,60,30,0,404,413,1,0,0,0,405,406,
        5,18,0,0,406,408,5,39,0,0,407,409,3,2,1,0,408,407,1,0,0,0,409,410,
        1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,413,1,0,0,0,412,394,
        1,0,0,0,412,405,1,0,0,0,413,61,1,0,0,0,46,65,74,82,88,93,106,115,
        122,140,146,158,167,180,183,189,208,211,220,223,230,234,236,244,
        252,259,268,275,283,295,298,304,311,326,336,340,346,352,362,367,
        371,378,384,396,401,410,412
    ]

class LatinoGrammarParser ( Parser ):

    grammarFileName = "LatinoGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'nulo'", "<INVALID>", 
                     "'leer'", "<INVALID>", "<INVALID>", "<INVALID>", "'limpiar'", 
                     "<INVALID>", "'imprimirf'", "'romper'", "'caso'", "<INVALID>", 
                     "'elegir'", "'si'", "'osi'", "'sino'", "'fin'", "'mientras'", 
                     "'desde'", "'para'", "'en'", "'rango'", "'repetir'", 
                     "'hasta'", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "L_UNARY_OP", "NUMERIC_OP", "LOGIC_OP", 
                      "STRING_OP", "ASSIGN_OP", "BOOLEAN_VALS", "NULL_VAL", 
                      "OP_BUILTIN_FUNCS_ARG", "OP_BUILTIN_FUNCS_NO_ARG", 
                      "R_UNARY_OP", "FUNC_KEYWORD", "RETURN_KEYWORD", "BUILTIN_FUNC_NO_ARG", 
                      "BUILTIN_FUNC_SINGLE_ARG", "BUILTIN_FUNC_MULTI_ARG", 
                      "BREAK", "CASE", "DEF_CASE", "SWITCH", "IF", "ELSE_IF", 
                      "ELSE", "BLOCK_END", "WHILE", "FOR", "FOR_RANGE", 
                      "IN", "RANGE", "DO_WHILE_START", "DO_WHILE_END", "OPENING_BRA", 
                      "CLOSING_BRA", "OPENING_PAR", "CLOSING_PAR", "OPENING_KEY", 
                      "CLOSING_KEY", "PERIOD", "COMMA", "COLON", "SEMICOLON", 
                      "ID", "REAL", "STRING", "SPACE", "LINE_COMMENT", "MULTILINE_COMMENT" ]

    RULE_source = 0
    RULE_sentence = 1
    RULE_assignableID = 2
    RULE_assignableIDModifiers = 3
    RULE_listAccess = 4
    RULE_propertyAccess = 5
    RULE_assig = 6
    RULE_exp = 7
    RULE_binaryOp = 8
    RULE_terminal = 9
    RULE_opBuiltInTipo = 10
    RULE_assignableExp = 11
    RULE_functionCall = 12
    RULE_anonymousFuncDef = 13
    RULE_listDefinition = 14
    RULE_dictDefinition = 15
    RULE_optionalAssignableExpConcat = 16
    RULE_optAssigExpConcatWithTrail = 17
    RULE_functionReturn = 18
    RULE_builtInFuncSentence = 19
    RULE_codeBlock = 20
    RULE_functionBlock = 21
    RULE_whileBlock = 22
    RULE_forBlock = 23
    RULE_forRangeBlock = 24
    RULE_doWhileBlock = 25
    RULE_conditionalBlock = 26
    RULE_altCondition = 27
    RULE_noCondition = 28
    RULE_switchBlock = 29
    RULE_switchCasesDef = 30

    ruleNames =  [ "source", "sentence", "assignableID", "assignableIDModifiers", 
                   "listAccess", "propertyAccess", "assig", "exp", "binaryOp", 
                   "terminal", "opBuiltInTipo", "assignableExp", "functionCall", 
                   "anonymousFuncDef", "listDefinition", "dictDefinition", 
                   "optionalAssignableExpConcat", "optAssigExpConcatWithTrail", 
                   "functionReturn", "builtInFuncSentence", "codeBlock", 
                   "functionBlock", "whileBlock", "forBlock", "forRangeBlock", 
                   "doWhileBlock", "conditionalBlock", "altCondition", "noCondition", 
                   "switchBlock", "switchCasesDef" ]

    EOF = Token.EOF
    L_UNARY_OP=1
    NUMERIC_OP=2
    LOGIC_OP=3
    STRING_OP=4
    ASSIGN_OP=5
    BOOLEAN_VALS=6
    NULL_VAL=7
    OP_BUILTIN_FUNCS_ARG=8
    OP_BUILTIN_FUNCS_NO_ARG=9
    R_UNARY_OP=10
    FUNC_KEYWORD=11
    RETURN_KEYWORD=12
    BUILTIN_FUNC_NO_ARG=13
    BUILTIN_FUNC_SINGLE_ARG=14
    BUILTIN_FUNC_MULTI_ARG=15
    BREAK=16
    CASE=17
    DEF_CASE=18
    SWITCH=19
    IF=20
    ELSE_IF=21
    ELSE=22
    BLOCK_END=23
    WHILE=24
    FOR=25
    FOR_RANGE=26
    IN=27
    RANGE=28
    DO_WHILE_START=29
    DO_WHILE_END=30
    OPENING_BRA=31
    CLOSING_BRA=32
    OPENING_PAR=33
    CLOSING_PAR=34
    OPENING_KEY=35
    CLOSING_KEY=36
    PERIOD=37
    COMMA=38
    COLON=39
    SEMICOLON=40
    ID=41
    REAL=42
    STRING=43
    SPACE=44
    LINE_COMMENT=45
    MULTILINE_COMMENT=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LatinoGrammarParser.EOF, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource" ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource" ):
                listener.exitSource(self)




    def source(self):

        localctx = LatinoGrammarParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0):
                self.state = 62
                self.sentence()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(LatinoGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignableID(self):
            return self.getTypedRuleContext(LatinoGrammarParser.AssignableIDContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(LatinoGrammarParser.FunctionCallContext,0)


        def assig(self):
            return self.getTypedRuleContext(LatinoGrammarParser.AssigContext,0)


        def R_UNARY_OP(self):
            return self.getToken(LatinoGrammarParser.R_UNARY_OP, 0)

        def builtInFuncSentence(self):
            return self.getTypedRuleContext(LatinoGrammarParser.BuiltInFuncSentenceContext,0)


        def functionReturn(self):
            return self.getTypedRuleContext(LatinoGrammarParser.FunctionReturnContext,0)


        def doWhileBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.DoWhileBlockContext,0)


        def codeBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.CodeBlockContext,0)


        def opBuiltInTipo(self):
            return self.getTypedRuleContext(LatinoGrammarParser.OpBuiltInTipoContext,0)


        def BREAK(self):
            return self.getToken(LatinoGrammarParser.BREAK, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = LatinoGrammarParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.assignableID()
                self.state = 74
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 71
                    self.functionCall()
                    pass
                elif token in [5, 38]:
                    self.state = 72
                    self.assig()
                    pass
                elif token in [10]:
                    self.state = 73
                    self.match(LatinoGrammarParser.R_UNARY_OP)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [13, 14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.builtInFuncSentence()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.functionReturn()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.doWhileBlock()
                pass
            elif token in [11, 19, 20, 24, 25, 26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.codeBlock()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.opBuiltInTipo()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.match(LatinoGrammarParser.BREAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LatinoGrammarParser.ID, 0)

        def assignableIDModifiers(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableIDModifiersContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableIDModifiersContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_assignableID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignableID" ):
                listener.enterAssignableID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignableID" ):
                listener.exitAssignableID(self)




    def assignableID(self):

        localctx = LatinoGrammarParser.AssignableIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignableID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(LatinoGrammarParser.ID)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==37:
                self.state = 85
                self.assignableIDModifiers()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableIDModifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listAccess(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ListAccessContext,0)


        def propertyAccess(self):
            return self.getTypedRuleContext(LatinoGrammarParser.PropertyAccessContext,0)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_assignableIDModifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignableIDModifiers" ):
                listener.enterAssignableIDModifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignableIDModifiers" ):
                listener.exitAssignableIDModifiers(self)




    def assignableIDModifiers(self):

        localctx = LatinoGrammarParser.AssignableIDModifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignableIDModifiers)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.listAccess()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.propertyAccess()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENING_BRA(self):
            return self.getToken(LatinoGrammarParser.OPENING_BRA, 0)

        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def CLOSING_BRA(self):
            return self.getToken(LatinoGrammarParser.CLOSING_BRA, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_listAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListAccess" ):
                listener.enterListAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListAccess" ):
                listener.exitListAccess(self)




    def listAccess(self):

        localctx = LatinoGrammarParser.ListAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LatinoGrammarParser.OPENING_BRA)
            self.state = 96
            self.exp()
            self.state = 97
            self.match(LatinoGrammarParser.CLOSING_BRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERIOD(self):
            return self.getToken(LatinoGrammarParser.PERIOD, 0)

        def ID(self):
            return self.getToken(LatinoGrammarParser.ID, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_propertyAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyAccess" ):
                listener.enterPropertyAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyAccess" ):
                listener.exitPropertyAccess(self)




    def propertyAccess(self):

        localctx = LatinoGrammarParser.PropertyAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_propertyAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(LatinoGrammarParser.PERIOD)
            self.state = 100
            self.match(LatinoGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(LatinoGrammarParser.ASSIGN_OP, 0)

        def assignableExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def assignableID(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableIDContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableIDContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_assig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssig" ):
                listener.enterAssig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssig" ):
                listener.exitAssig(self)




    def assig(self):

        localctx = LatinoGrammarParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assig)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 102
                self.match(LatinoGrammarParser.COMMA)
                self.state = 103
                self.assignableID()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(LatinoGrammarParser.ASSIGN_OP)
            self.state = 110
            self.assignableExp()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 111
                self.match(LatinoGrammarParser.COMMA)
                self.state = 112
                self.assignableExp()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terminal(self):
            return self.getTypedRuleContext(LatinoGrammarParser.TerminalContext,0)


        def binaryOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.BinaryOpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.BinaryOpContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = LatinoGrammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.terminal()
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    self.binaryOp() 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terminal(self):
            return self.getTypedRuleContext(LatinoGrammarParser.TerminalContext,0)


        def L_UNARY_OP(self):
            return self.getToken(LatinoGrammarParser.L_UNARY_OP, 0)

        def NUMERIC_OP(self):
            return self.getToken(LatinoGrammarParser.NUMERIC_OP, 0)

        def LOGIC_OP(self):
            return self.getToken(LatinoGrammarParser.LOGIC_OP, 0)

        def STRING_OP(self):
            return self.getToken(LatinoGrammarParser.STRING_OP, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)




    def binaryOp(self):

        localctx = LatinoGrammarParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 126
            self.terminal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def REAL(self):
            return self.getToken(LatinoGrammarParser.REAL, 0)

        def STRING(self):
            return self.getToken(LatinoGrammarParser.STRING, 0)

        def BOOLEAN_VALS(self):
            return self.getToken(LatinoGrammarParser.BOOLEAN_VALS, 0)

        def NULL_VAL(self):
            return self.getToken(LatinoGrammarParser.NULL_VAL, 0)

        def ID(self):
            return self.getToken(LatinoGrammarParser.ID, 0)

        def assignableIDModifiers(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableIDModifiersContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableIDModifiersContext,i)


        def functionCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.FunctionCallContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.FunctionCallContext,i)


        def L_UNARY_OP(self):
            return self.getToken(LatinoGrammarParser.L_UNARY_OP, 0)

        def opBuiltInTipo(self):
            return self.getTypedRuleContext(LatinoGrammarParser.OpBuiltInTipoContext,0)


        def OP_BUILTIN_FUNCS_NO_ARG(self):
            return self.getToken(LatinoGrammarParser.OP_BUILTIN_FUNCS_NO_ARG, 0)

        def anonymousFuncDef(self):
            return self.getTypedRuleContext(LatinoGrammarParser.AnonymousFuncDefContext,0)


        def listDefinition(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ListDefinitionContext,0)


        def dictDefinition(self):
            return self.getTypedRuleContext(LatinoGrammarParser.DictDefinitionContext,0)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)




    def terminal(self):

        localctx = LatinoGrammarParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_terminal)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(LatinoGrammarParser.OPENING_PAR)
                self.state = 129
                self.exp()
                self.state = 130
                self.match(LatinoGrammarParser.CLOSING_PAR)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(LatinoGrammarParser.REAL)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(LatinoGrammarParser.STRING)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.match(LatinoGrammarParser.BOOLEAN_VALS)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.match(LatinoGrammarParser.NULL_VAL)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.match(LatinoGrammarParser.ID)
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 137
                        self.assignableIDModifiers() 
                    self.state = 142
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 143
                        self.functionCall() 
                    self.state = 148
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 7)
                self.state = 149
                self.match(LatinoGrammarParser.L_UNARY_OP)
                self.state = 150
                self.exp()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 8)
                self.state = 151
                self.opBuiltInTipo()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 9)
                self.state = 152
                self.match(LatinoGrammarParser.OP_BUILTIN_FUNCS_NO_ARG)
                self.state = 153
                self.match(LatinoGrammarParser.OPENING_PAR)
                self.state = 154
                self.match(LatinoGrammarParser.CLOSING_PAR)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 10)
                self.state = 155
                self.anonymousFuncDef()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 11)
                self.state = 156
                self.listDefinition()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 12)
                self.state = 157
                self.dictDefinition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpBuiltInTipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_BUILTIN_FUNCS_ARG(self):
            return self.getToken(LatinoGrammarParser.OP_BUILTIN_FUNCS_ARG, 0)

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def assignableExp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.AssignableExpContext,0)


        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_opBuiltInTipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpBuiltInTipo" ):
                listener.enterOpBuiltInTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpBuiltInTipo" ):
                listener.exitOpBuiltInTipo(self)




    def opBuiltInTipo(self):

        localctx = LatinoGrammarParser.OpBuiltInTipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_opBuiltInTipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(LatinoGrammarParser.OP_BUILTIN_FUNCS_ARG)
            self.state = 161
            self.match(LatinoGrammarParser.OPENING_PAR)
            self.state = 162
            self.assignableExp()
            self.state = 163
            self.match(LatinoGrammarParser.CLOSING_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def anonymousFuncDef(self):
            return self.getTypedRuleContext(LatinoGrammarParser.AnonymousFuncDefContext,0)


        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_assignableExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignableExp" ):
                listener.enterAssignableExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignableExp" ):
                listener.exitAssignableExp(self)




    def assignableExp(self):

        localctx = LatinoGrammarParser.AssignableExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignableExp)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.anonymousFuncDef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def optionalAssignableExpConcat(self):
            return self.getTypedRuleContext(LatinoGrammarParser.OptionalAssignableExpConcatContext,0)


        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = LatinoGrammarParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(LatinoGrammarParser.OPENING_PAR)
            self.state = 170
            self.optionalAssignableExpConcat()
            self.state = 171
            self.match(LatinoGrammarParser.CLOSING_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnonymousFuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_KEYWORD(self):
            return self.getToken(LatinoGrammarParser.FUNC_KEYWORD, 0)

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def BLOCK_END(self):
            return self.getToken(LatinoGrammarParser.BLOCK_END, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.ID)
            else:
                return self.getToken(LatinoGrammarParser.ID, i)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_anonymousFuncDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymousFuncDef" ):
                listener.enterAnonymousFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymousFuncDef" ):
                listener.exitAnonymousFuncDef(self)




    def anonymousFuncDef(self):

        localctx = LatinoGrammarParser.AnonymousFuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_anonymousFuncDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(LatinoGrammarParser.FUNC_KEYWORD)
            self.state = 174
            self.match(LatinoGrammarParser.OPENING_PAR)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 175
                self.match(LatinoGrammarParser.ID)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 176
                    self.match(LatinoGrammarParser.COMMA)
                    self.state = 177
                    self.match(LatinoGrammarParser.ID)
                    self.state = 182
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 185
            self.match(LatinoGrammarParser.CLOSING_PAR)
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 186
                self.sentence()
                self.state = 189 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

            self.state = 191
            self.match(LatinoGrammarParser.BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENING_BRA(self):
            return self.getToken(LatinoGrammarParser.OPENING_BRA, 0)

        def optAssigExpConcatWithTrail(self):
            return self.getTypedRuleContext(LatinoGrammarParser.OptAssigExpConcatWithTrailContext,0)


        def CLOSING_BRA(self):
            return self.getToken(LatinoGrammarParser.CLOSING_BRA, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_listDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListDefinition" ):
                listener.enterListDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListDefinition" ):
                listener.exitListDefinition(self)




    def listDefinition(self):

        localctx = LatinoGrammarParser.ListDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(LatinoGrammarParser.OPENING_BRA)
            self.state = 194
            self.optAssigExpConcatWithTrail()
            self.state = 195
            self.match(LatinoGrammarParser.CLOSING_BRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENING_KEY(self):
            return self.getToken(LatinoGrammarParser.OPENING_KEY, 0)

        def CLOSING_KEY(self):
            return self.getToken(LatinoGrammarParser.CLOSING_KEY, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.ExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COLON)
            else:
                return self.getToken(LatinoGrammarParser.COLON, i)

        def assignableExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_dictDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictDefinition" ):
                listener.enterDictDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictDefinition" ):
                listener.exitDictDefinition(self)




    def dictDefinition(self):

        localctx = LatinoGrammarParser.DictDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dictDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(LatinoGrammarParser.OPENING_KEY)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15438259948482) != 0):
                self.state = 198
                self.exp()
                self.state = 199
                self.match(LatinoGrammarParser.COLON)
                self.state = 200
                self.assignableExp()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 201
                    self.match(LatinoGrammarParser.COMMA)
                    self.state = 202
                    self.exp()
                    self.state = 203
                    self.match(LatinoGrammarParser.COLON)
                    self.state = 204
                    self.assignableExp()
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 213
            self.match(LatinoGrammarParser.CLOSING_KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionalAssignableExpConcatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignableExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_optionalAssignableExpConcat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionalAssignableExpConcat" ):
                listener.enterOptionalAssignableExpConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionalAssignableExpConcat" ):
                listener.exitOptionalAssignableExpConcat(self)




    def optionalAssignableExpConcat(self):

        localctx = LatinoGrammarParser.OptionalAssignableExpConcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_optionalAssignableExpConcat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15438259948482) != 0):
                self.state = 215
                self.assignableExp()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 216
                    self.match(LatinoGrammarParser.COMMA)
                    self.state = 217
                    self.assignableExp()
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptAssigExpConcatWithTrailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignableExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_optAssigExpConcatWithTrail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptAssigExpConcatWithTrail" ):
                listener.enterOptAssigExpConcatWithTrail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptAssigExpConcatWithTrail" ):
                listener.exitOptAssigExpConcatWithTrail(self)




    def optAssigExpConcatWithTrail(self):

        localctx = LatinoGrammarParser.OptAssigExpConcatWithTrailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_optAssigExpConcatWithTrail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15438259948482) != 0):
                self.state = 225
                self.assignableExp()
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 226
                        self.match(LatinoGrammarParser.COMMA)
                        self.state = 227
                        self.assignableExp() 
                    self.state = 232
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 233
                    self.match(LatinoGrammarParser.COMMA)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_KEYWORD(self):
            return self.getToken(LatinoGrammarParser.RETURN_KEYWORD, 0)

        def assignableExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_functionReturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionReturn" ):
                listener.enterFunctionReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionReturn" ):
                listener.exitFunctionReturn(self)




    def functionReturn(self):

        localctx = LatinoGrammarParser.FunctionReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionReturn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(LatinoGrammarParser.RETURN_KEYWORD)
            self.state = 239
            self.assignableExp()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 240
                self.match(LatinoGrammarParser.COMMA)
                self.state = 241
                self.assignableExp()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuiltInFuncSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BUILTIN_FUNC_MULTI_ARG(self):
            return self.getToken(LatinoGrammarParser.BUILTIN_FUNC_MULTI_ARG, 0)

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def assignableExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AssignableExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AssignableExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def BUILTIN_FUNC_SINGLE_ARG(self):
            return self.getToken(LatinoGrammarParser.BUILTIN_FUNC_SINGLE_ARG, 0)

        def BUILTIN_FUNC_NO_ARG(self):
            return self.getToken(LatinoGrammarParser.BUILTIN_FUNC_NO_ARG, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_builtInFuncSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuiltInFuncSentence" ):
                listener.enterBuiltInFuncSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuiltInFuncSentence" ):
                listener.exitBuiltInFuncSentence(self)




    def builtInFuncSentence(self):

        localctx = LatinoGrammarParser.BuiltInFuncSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_builtInFuncSentence)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(LatinoGrammarParser.BUILTIN_FUNC_MULTI_ARG)
                self.state = 248
                self.match(LatinoGrammarParser.OPENING_PAR)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15438259948482) != 0):
                    self.state = 249
                    self.assignableExp()
                    self.state = 254
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 255
                    self.match(LatinoGrammarParser.COMMA)
                    self.state = 256
                    self.assignableExp()
                    self.state = 261
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 262
                self.match(LatinoGrammarParser.CLOSING_PAR)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(LatinoGrammarParser.BUILTIN_FUNC_SINGLE_ARG)
                self.state = 264
                self.match(LatinoGrammarParser.OPENING_PAR)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15438259948482) != 0):
                    self.state = 265
                    self.assignableExp()
                    self.state = 270
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 271
                self.match(LatinoGrammarParser.CLOSING_PAR)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.match(LatinoGrammarParser.BUILTIN_FUNC_NO_ARG)
                self.state = 273
                self.match(LatinoGrammarParser.OPENING_PAR)
                self.state = 274
                self.match(LatinoGrammarParser.CLOSING_PAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_END(self):
            return self.getToken(LatinoGrammarParser.BLOCK_END, 0)

        def functionBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.FunctionBlockContext,0)


        def whileBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.WhileBlockContext,0)


        def forBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ForBlockContext,0)


        def forRangeBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ForRangeBlockContext,0)


        def conditionalBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ConditionalBlockContext,0)


        def switchBlock(self):
            return self.getTypedRuleContext(LatinoGrammarParser.SwitchBlockContext,0)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_codeBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeBlock" ):
                listener.enterCodeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeBlock" ):
                listener.exitCodeBlock(self)




    def codeBlock(self):

        localctx = LatinoGrammarParser.CodeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_codeBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 277
                self.functionBlock()
                pass
            elif token in [24]:
                self.state = 278
                self.whileBlock()
                pass
            elif token in [25]:
                self.state = 279
                self.forBlock()
                pass
            elif token in [26]:
                self.state = 280
                self.forRangeBlock()
                pass
            elif token in [20]:
                self.state = 281
                self.conditionalBlock()
                pass
            elif token in [19]:
                self.state = 282
                self.switchBlock()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 285
            self.match(LatinoGrammarParser.BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_KEYWORD(self):
            return self.getToken(LatinoGrammarParser.FUNC_KEYWORD, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.ID)
            else:
                return self.getToken(LatinoGrammarParser.ID, i)

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_functionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBlock" ):
                listener.enterFunctionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBlock" ):
                listener.exitFunctionBlock(self)




    def functionBlock(self):

        localctx = LatinoGrammarParser.FunctionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(LatinoGrammarParser.FUNC_KEYWORD)
            self.state = 288
            self.match(LatinoGrammarParser.ID)
            self.state = 289
            self.match(LatinoGrammarParser.OPENING_PAR)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 290
                self.match(LatinoGrammarParser.ID)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 291
                    self.match(LatinoGrammarParser.COMMA)
                    self.state = 292
                    self.match(LatinoGrammarParser.ID)
                    self.state = 297
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 300
            self.match(LatinoGrammarParser.CLOSING_PAR)
            self.state = 302 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 301
                self.sentence()
                self.state = 304 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LatinoGrammarParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_whileBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBlock" ):
                listener.enterWhileBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBlock" ):
                listener.exitWhileBlock(self)




    def whileBlock(self):

        localctx = LatinoGrammarParser.WhileBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_whileBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(LatinoGrammarParser.WHILE)
            self.state = 307
            self.exp()
            self.state = 309 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 308
                self.sentence()
                self.state = 311 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LatinoGrammarParser.FOR, 0)

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def assignableID(self):
            return self.getTypedRuleContext(LatinoGrammarParser.AssignableIDContext,0)


        def ASSIGN_OP(self):
            return self.getToken(LatinoGrammarParser.ASSIGN_OP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.ExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.SEMICOLON)
            else:
                return self.getToken(LatinoGrammarParser.SEMICOLON, i)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_forBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForBlock" ):
                listener.enterForBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForBlock" ):
                listener.exitForBlock(self)




    def forBlock(self):

        localctx = LatinoGrammarParser.ForBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(LatinoGrammarParser.FOR)
            self.state = 314
            self.match(LatinoGrammarParser.OPENING_PAR)
            self.state = 315
            self.assignableID()
            self.state = 316
            self.match(LatinoGrammarParser.ASSIGN_OP)
            self.state = 317
            self.exp()
            self.state = 318
            self.match(LatinoGrammarParser.SEMICOLON)
            self.state = 319
            self.exp()
            self.state = 320
            self.match(LatinoGrammarParser.SEMICOLON)
            self.state = 321
            self.sentence()
            self.state = 322
            self.match(LatinoGrammarParser.CLOSING_PAR)
            self.state = 324 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 323
                self.sentence()
                self.state = 326 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_RANGE(self):
            return self.getToken(LatinoGrammarParser.FOR_RANGE, 0)

        def ID(self):
            return self.getToken(LatinoGrammarParser.ID, 0)

        def IN(self):
            return self.getToken(LatinoGrammarParser.IN, 0)

        def RANGE(self):
            return self.getToken(LatinoGrammarParser.RANGE, 0)

        def OPENING_PAR(self):
            return self.getToken(LatinoGrammarParser.OPENING_PAR, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.ExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,i)


        def CLOSING_PAR(self):
            return self.getToken(LatinoGrammarParser.CLOSING_PAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COMMA)
            else:
                return self.getToken(LatinoGrammarParser.COMMA, i)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_forRangeBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForRangeBlock" ):
                listener.enterForRangeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForRangeBlock" ):
                listener.exitForRangeBlock(self)




    def forRangeBlock(self):

        localctx = LatinoGrammarParser.ForRangeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forRangeBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(LatinoGrammarParser.FOR_RANGE)
            self.state = 329
            self.match(LatinoGrammarParser.ID)
            self.state = 330
            self.match(LatinoGrammarParser.IN)
            self.state = 331
            self.match(LatinoGrammarParser.RANGE)
            self.state = 332
            self.match(LatinoGrammarParser.OPENING_PAR)
            self.state = 333
            self.exp()
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 334
                self.match(LatinoGrammarParser.COMMA)
                self.state = 335
                self.exp()


            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 338
                self.match(LatinoGrammarParser.COMMA)
                self.state = 339
                self.exp()


            self.state = 342
            self.match(LatinoGrammarParser.CLOSING_PAR)
            self.state = 344 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 343
                self.sentence()
                self.state = 346 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO_WHILE_START(self):
            return self.getToken(LatinoGrammarParser.DO_WHILE_START, 0)

        def DO_WHILE_END(self):
            return self.getToken(LatinoGrammarParser.DO_WHILE_END, 0)

        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_doWhileBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileBlock" ):
                listener.enterDoWhileBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileBlock" ):
                listener.exitDoWhileBlock(self)




    def doWhileBlock(self):

        localctx = LatinoGrammarParser.DoWhileBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_doWhileBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(LatinoGrammarParser.DO_WHILE_START)
            self.state = 350 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 349
                self.sentence()
                self.state = 352 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

            self.state = 354
            self.match(LatinoGrammarParser.DO_WHILE_END)
            self.state = 355
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LatinoGrammarParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def altCondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.AltConditionContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.AltConditionContext,i)


        def noCondition(self):
            return self.getTypedRuleContext(LatinoGrammarParser.NoConditionContext,0)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_conditionalBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalBlock" ):
                listener.enterConditionalBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalBlock" ):
                listener.exitConditionalBlock(self)




    def conditionalBlock(self):

        localctx = LatinoGrammarParser.ConditionalBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_conditionalBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(LatinoGrammarParser.IF)
            self.state = 358
            self.exp()
            self.state = 360 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 359
                self.sentence()
                self.state = 362 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 364
                self.altCondition()
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 370
                self.noCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AltConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_IF(self):
            return self.getToken(LatinoGrammarParser.ELSE_IF, 0)

        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_altCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAltCondition" ):
                listener.enterAltCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAltCondition" ):
                listener.exitAltCondition(self)




    def altCondition(self):

        localctx = LatinoGrammarParser.AltConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_altCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(LatinoGrammarParser.ELSE_IF)
            self.state = 374
            self.exp()
            self.state = 376 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 375
                self.sentence()
                self.state = 378 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(LatinoGrammarParser.ELSE, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_noCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoCondition" ):
                listener.enterNoCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoCondition" ):
                listener.exitNoCondition(self)




    def noCondition(self):

        localctx = LatinoGrammarParser.NoConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_noCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(LatinoGrammarParser.ELSE)
            self.state = 382 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 381
                self.sentence()
                self.state = 384 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(LatinoGrammarParser.SWITCH, 0)

        def exp(self):
            return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,0)


        def switchCasesDef(self):
            return self.getTypedRuleContext(LatinoGrammarParser.SwitchCasesDefContext,0)


        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_switchBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlock" ):
                listener.enterSwitchBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlock" ):
                listener.exitSwitchBlock(self)




    def switchBlock(self):

        localctx = LatinoGrammarParser.SwitchBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_switchBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(LatinoGrammarParser.SWITCH)
            self.state = 387
            self.exp()
            self.state = 388
            self.switchCasesDef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCasesDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchCasesDef(self):
            return self.getTypedRuleContext(LatinoGrammarParser.SwitchCasesDefContext,0)


        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.CASE)
            else:
                return self.getToken(LatinoGrammarParser.CASE, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.ExpContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.ExpContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.COLON)
            else:
                return self.getToken(LatinoGrammarParser.COLON, i)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatinoGrammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(LatinoGrammarParser.SentenceContext,i)


        def DEF_CASE(self):
            return self.getToken(LatinoGrammarParser.DEF_CASE, 0)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_switchCasesDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchCasesDef" ):
                listener.enterSwitchCasesDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchCasesDef" ):
                listener.exitSwitchCasesDef(self)




    def switchCasesDef(self):

        localctx = LatinoGrammarParser.SwitchCasesDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switchCasesDef)
        self._la = 0 # Token type
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 390
                    self.match(LatinoGrammarParser.CASE)
                    self.state = 391
                    self.exp()
                    self.state = 392
                    self.match(LatinoGrammarParser.COLON)
                    self.state = 396 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==17):
                        break

                self.state = 399 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 398
                    self.sentence()
                    self.state = 401 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                        break

                self.state = 403
                self.switchCasesDef()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(LatinoGrammarParser.DEF_CASE)
                self.state = 406
                self.match(LatinoGrammarParser.COLON)
                self.state = 408 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 407
                    self.sentence()
                    self.state = 410 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199679269120) != 0)):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





