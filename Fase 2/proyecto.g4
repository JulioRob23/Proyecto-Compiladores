grammar proyecto;

start: line;

line: var 
	| condi 
	| arith 
	| func 
	| data 
	| CRESSELIA UNOWN 
	| UNOWN?
	| CHARMANDER UNOWN;
	
var: TOTODILE ID '=' INT UNOWN line 
	| TOTODILE ID '=' arith (UNOWN)? line
	| WOOPER ID '=' FLOAT UNOWN line
	| PIKACHU ID '=' BOOL UNOWN line
	| CORVIKNIGHT ID '=' STRING UNOWN line;

condi: RATATA exp act ((elif else)|elif|else) CRESSELIA (UNOWN)? line
	| NECROZMA exp act (UNOWN)? CRESSELIA (UNOWN)? line;


elif: PARAS exp act elif  
	;

else: CLEFABLE act 
	;

exp: ID cond (INT|ID) 
	| ID cond (FLOAT|ID)
	| ID condv (BOOL|ID)
	| ID cond (STRING|ID);

cond: '='
    | '!''='
    | '<'
    | '>'
    | '<''='
    | '>''=';  

condv: '!''='
	| '=';

act: (UNOWN)? line;

arith: (ID '=')? xerneas (('+'|'-') xerneas)*;

xerneas: uxie ((''|'/') uxie);

uxie: '(' arith ')'
	| INT
	| ID
	;

	
func: TENTACOOL ID '(' atr ID (')'|extra) UNOWN line MEWTWO ID UNOWN line
	| (atr)? ID '=' ID '('atrl (')' | extra) (UNOWN)? line ;
extra: ',' atr ID (extra | ')')
	| ',' atrl
	;
atr: TOTODILE 
	| WOOPER 
	| PIKACHU
	| CORVIKNIGHT; 

atrl: STRING
	| INT
	| FLOAT
	;
	
data: atr ID '=' SEEL (UNOWN)? line 
	| DRAGONITE '(' (atrl | ID) ')' (UNOWN |(UNOWN line)) ;

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
BOOL : '0'|'1' ;
WS: [ \t\r\n]+ -> skip;