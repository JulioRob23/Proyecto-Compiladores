grammar proyecto;

start: line;

line: var 
	| condi 
	| arith 
	| func 
	| data 
	| UNOWN?
	| CHARMANDER UNOWN;
	
var: TOTODILE ID EQUAL INT (UNOWN)? line 
	| TOTODILE ID EQUAL arith (UNOWN)? line
	| WOOPER ID EQUAL FLOAT UNOWN line
	| PIKACHU ID EQUAL BOOL UNOWN line
	| CORVIKNIGHT ID EQUAL STRING UNOWN line;

condi: RATATA exp act (UNOWN)? (elif)? else? CRESSELIA (UNOWN)? line
	| NECROZMA exp act (UNOWN)? CRESSELIA (UNOWN)? line;


elif: (PARAS exp act (UNOWN)?)+
	;

else: CLEFABLE act 
	;

exp: ID cond (INT|ID) 
	| ID cond (FLOAT|ID)
	| ID condv (BOOL|ID)
	| ID cond (STRING|ID);

cond: EQUAL
    | EXC EQUAL
    | MINOR
    | BIGGER
    | MINOR EQUAL
    | BIGGER EQUAL;  

condv: EXC EQUAL
	| EQUAL;

act: (UNOWN)? line;

arith: (ID EQUAL)? xerneas ((PLUS|MINUS) xerneas)* (UNOWN)? line;

xerneas: uxie ((MUL|DIV) uxie)*;

uxie: OPA arith CLPA
	| INT
	| ID
	;

	
func: TENTACOOL atr ((ID OPA atr ID (CLPA|extraf)) | (ID OPA CLPA)) UNOWN line MEWTWO ID? UNOWN line
	| (atr)? ID EQUAL ID ((OPA atrl (CLPA | extrac)) | (OPA CLPA)) (UNOWN)? line ;

extraf: COMA atr ID (extraf | CLPA);

extrac: COMA (atrl | ID ) (extrac | CLPA);

atr: TOTODILE 
	| WOOPER 
	| PIKACHU
	| CORVIKNIGHT; 

atrl: STRING
	| INT
	| FLOAT
	;
	
data: atr ID EQUAL SEEL (UNOWN)? line 
	| DRAGONITE OPA (atrl | ID) CLPA (UNOWN)? line ;


CHARMANDER : 'Charmander';
TOTODILE : 'Totodile';
WOOPER : 'Wooper';
PIKACHU : 'Pikachu';
CORVIKNIGHT : 'Corviknight';
RATATA : 'Ratata';
PARAS : 'Paras';
CLEFABLE : 'Clefable';
TENTACOOL : 'Tentacool';
SEEL : 'Seel';
DRAGONITE : 'Dragonite';
NECROZMA : 'Necrozma';
CRESSELIA : 'Cresselia';
MEWTWO : 'Mewtwo';
UNOWN : [\r\n]+ ;
INT : [0-9]+ ;
ID : [a-zA-Z][A-Za-z0-9]*; 
FLOAT : [0-9]+'.'[0-9]*; 
STRING : '"'(~["\r\n])+'"'; 
BOOL : '0F'|'1V' ;
WS: [ \t\r\n]+ -> skip;
EQUAL : '=';
EXC : '!';
MINOR : '<';
BIGGER :'>';
PLUS : '+';
MINUS : '-';
DIV : '/';
MUL : '*';
OPA : '(';
CLPA : ')';
COMA : ',';