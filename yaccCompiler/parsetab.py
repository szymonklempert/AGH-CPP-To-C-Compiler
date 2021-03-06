
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDITION AND ASSIGN AUTO BRACE_LEFT BRACE_RIGHT BRACKET_LEFT BRACKET_RIGHT BREAK CASE CHAR COLON COMMA CONST CONTINUE COUT DECREMENT DECREMENTS_ASSIGN DEFAULT DIVIDES_ASSIGN DIVISION DO DOUBLE ELSE EQUAL FLOAT FLOAT_VAL FOR GOTO GREATER GREATER_OR_EQUAL ID IF INCLUDE INCREMENT INCREMENTS_ASSIGN INT INT_VAL LESS LESS_OR_EQUAL LIBRARY MODULUS MODULUS_ASSIGN MULTIPLICATION MULTIPLIES_ASSIGN NOT NOT_EQUAL NUMBER OR OUTPUT PARENTHESE_LEFT PARENTHESE_RIGHT PREPROCESSOR RETURN SEMICOLON STRING STRUCT SUBSTRACTION SWITCH VOID WHILE\n    start : program\n    \n    program : elements\n    \n    header : PREPROCESSOR INCLUDE LIBRARY\n    \n    elements : element\n             | element elements\n    \n    element : function_definition\n            | void_function_definition\n            | header\n            | empty\n    \n    function_definition : type ID PARENTHESE_LEFT function_parameters PARENTHESE_RIGHT BRACE_LEFT expressions return_statement BRACE_RIGHT\n    \n    void_function_definition : VOID ID PARENTHESE_LEFT function_parameters PARENTHESE_RIGHT BRACE_LEFT expressions BRACE_RIGHT\n    \n    function_parameters : type ID\n                        | type ID COMMA function_parameters\n                        | empty\n    \n    expressions : expression\n        | expression expressions\n        | empty\n    \n    expression : conditional_expression\n            | iteration_expression\n            | print_expression\n            | assignment_expression\n            | empty\n    \n    assignment_expression : ID assignment_operator val SEMICOLON\n                          | ID assignment_operator ID SEMICOLON\n           \n    \n    assignment_operator : ASSIGN\n        | INCREMENTS_ASSIGN\n        | DECREMENTS_ASSIGN\n        | MULTIPLIES_ASSIGN\n        | DIVIDES_ASSIGN\n        | MODULUS_ASSIGN\n    \n    print_expression : COUT OUTPUT val SEMICOLON\n           \n    \n    iteration_expression : while_iteration\n            | do_while_iteration\n           \n    \n    while_iteration : WHILE PARENTHESE_LEFT condition PARENTHESE_RIGHT BRACE_LEFT expressions BRACE_RIGHT\n    \n    do_while_iteration : DO BRACE_LEFT expressions BRACE_RIGHT WHILE PARENTHESE_LEFT condition PARENTHESE_RIGHT SEMICOLON\n    \n    conditional_expression : IF PARENTHESE_LEFT condition PARENTHESE_RIGHT BRACE_LEFT expressions BRACE_RIGHT\n    \n    condition : NOT ID\n        | condition logical_operator condition\n        | val comparison_operator val\n        | val\n    \n    comparison_operator : GREATER\n        | LESS\n        | GREATER_OR_EQUAL\n        | LESS_OR_EQUAL\n        | NOT_EQUAL\n        | EQUAL\n    \n    logical_operator : AND\n        | OR\n    \n    return_statement : RETURN val SEMICOLON\n    \n    val : FLOAT_VAL\n        | INT_VAL\n        | ID\n    \n    type : INT\n            | FLOAT\n            | STRING\n            | CHAR\n            | DOUBLE\n            | VOID\n    \n    empty : \n    '
    
_lr_action_items = {'VOID':([0,4,5,6,7,8,21,22,23,32,65,70,],[10,10,-6,-7,-8,-9,27,27,-3,27,-11,-10,]),'PREPROCESSOR':([0,4,5,6,7,8,23,65,70,],[11,11,-6,-7,-8,-9,-3,-11,-10,]),'INT':([0,4,5,6,7,8,21,22,23,32,65,70,],[12,12,-6,-7,-8,-9,12,12,-3,12,-11,-10,]),'FLOAT':([0,4,5,6,7,8,21,22,23,32,65,70,],[13,13,-6,-7,-8,-9,13,13,-3,13,-11,-10,]),'STRING':([0,4,5,6,7,8,21,22,23,32,65,70,],[14,14,-6,-7,-8,-9,14,14,-3,14,-11,-10,]),'CHAR':([0,4,5,6,7,8,21,22,23,32,65,70,],[15,15,-6,-7,-8,-9,15,15,-3,15,-11,-10,]),'DOUBLE':([0,4,5,6,7,8,21,22,23,32,65,70,],[16,16,-6,-7,-8,-9,16,16,-3,16,-11,-10,]),'$end':([0,1,2,3,4,5,6,7,8,17,23,65,70,],[-59,0,-1,-2,-4,-6,-7,-8,-9,-5,-3,-11,-10,]),'ID':([9,10,12,13,14,15,16,24,27,33,34,38,39,40,41,42,43,45,46,51,52,53,54,55,56,57,59,61,62,63,64,74,79,80,83,84,85,87,88,89,90,91,92,93,94,97,100,104,105,106,109,],[18,19,-53,-54,-55,-56,-57,29,-58,36,36,36,-22,-18,-19,-20,-21,-32,-33,66,-25,-26,-27,-28,-29,-30,72,72,72,72,36,86,-24,-23,72,-47,-48,72,-41,-42,-43,-44,-45,-46,-31,36,36,72,-36,-34,-35,]),'INCLUDE':([11,],[20,]),'PARENTHESE_LEFT':([18,19,44,48,101,],[21,22,61,63,104,]),'LIBRARY':([20,],[23,]),'PARENTHESE_RIGHT':([21,22,25,26,28,29,32,35,68,69,72,73,75,77,86,98,99,107,],[-59,-59,30,-14,31,-12,-59,-13,-50,-51,-52,82,-40,95,-37,-38,-39,108,]),'COMMA':([29,],[32,]),'BRACE_LEFT':([30,31,49,82,95,],[33,34,64,97,100,]),'RETURN':([33,37,38,39,40,41,42,43,45,46,60,79,80,94,105,106,109,],[-59,59,-15,-17,-18,-19,-20,-21,-32,-33,-16,-24,-23,-31,-36,-34,-35,]),'IF':([33,34,38,39,40,41,42,43,45,46,64,79,80,94,97,100,105,106,109,],[44,44,44,-22,-18,-19,-20,-21,-32,-33,44,-24,-23,-31,44,44,-36,-34,-35,]),'COUT':([33,34,38,39,40,41,42,43,45,46,64,79,80,94,97,100,105,106,109,],[47,47,47,-22,-18,-19,-20,-21,-32,-33,47,-24,-23,-31,47,47,-36,-34,-35,]),'WHILE':([33,34,38,39,40,41,42,43,45,46,64,79,80,94,96,97,100,105,106,109,],[48,48,48,-22,-18,-19,-20,-21,-32,-33,48,-24,-23,-31,101,48,48,-36,-34,-35,]),'DO':([33,34,38,39,40,41,42,43,45,46,64,79,80,94,97,100,105,106,109,],[49,49,49,-22,-18,-19,-20,-21,-32,-33,49,-24,-23,-31,49,49,-36,-34,-35,]),'BRACE_RIGHT':([34,38,39,40,41,42,43,45,46,50,58,60,64,78,79,80,81,94,97,100,102,103,105,106,109,],[-59,-15,-17,-18,-19,-20,-21,-32,-33,65,70,-16,-59,96,-24,-23,-49,-31,-59,-59,105,106,-36,-34,-35,]),'ASSIGN':([36,],[52,]),'INCREMENTS_ASSIGN':([36,],[53,]),'DECREMENTS_ASSIGN':([36,],[54,]),'MULTIPLIES_ASSIGN':([36,],[55,]),'DIVIDES_ASSIGN':([36,],[56,]),'MODULUS_ASSIGN':([36,],[57,]),'OUTPUT':([47,],[62,]),'FLOAT_VAL':([51,52,53,54,55,56,57,59,61,62,63,83,84,85,87,88,89,90,91,92,93,104,],[68,-25,-26,-27,-28,-29,-30,68,68,68,68,68,-47,-48,68,-41,-42,-43,-44,-45,-46,68,]),'INT_VAL':([51,52,53,54,55,56,57,59,61,62,63,83,84,85,87,88,89,90,91,92,93,104,],[69,-25,-26,-27,-28,-29,-30,69,69,69,69,69,-47,-48,69,-41,-42,-43,-44,-45,-46,69,]),'NOT':([61,63,83,84,85,104,],[74,74,74,-47,-48,74,]),'SEMICOLON':([66,67,68,69,71,72,76,108,],[79,80,-50,-51,81,-52,94,109,]),'GREATER':([68,69,72,75,],[-50,-51,-52,88,]),'LESS':([68,69,72,75,],[-50,-51,-52,89,]),'GREATER_OR_EQUAL':([68,69,72,75,],[-50,-51,-52,90,]),'LESS_OR_EQUAL':([68,69,72,75,],[-50,-51,-52,91,]),'NOT_EQUAL':([68,69,72,75,],[-50,-51,-52,92,]),'EQUAL':([68,69,72,75,],[-50,-51,-52,93,]),'AND':([68,69,72,73,75,77,86,98,99,107,],[-50,-51,-52,84,-40,84,-37,84,-39,84,]),'OR':([68,69,72,73,75,77,86,98,99,107,],[-50,-51,-52,85,-40,85,-37,85,-39,85,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'program':([0,],[2,]),'elements':([0,4,],[3,17,]),'element':([0,4,],[4,4,]),'function_definition':([0,4,],[5,5,]),'void_function_definition':([0,4,],[6,6,]),'header':([0,4,],[7,7,]),'empty':([0,4,21,22,32,33,34,38,64,97,100,],[8,8,26,26,26,39,39,39,39,39,39,]),'type':([0,4,21,22,32,],[9,9,24,24,24,]),'function_parameters':([21,22,32,],[25,28,35,]),'expressions':([33,34,38,64,97,100,],[37,50,60,78,102,103,]),'expression':([33,34,38,64,97,100,],[38,38,38,38,38,38,]),'conditional_expression':([33,34,38,64,97,100,],[40,40,40,40,40,40,]),'iteration_expression':([33,34,38,64,97,100,],[41,41,41,41,41,41,]),'print_expression':([33,34,38,64,97,100,],[42,42,42,42,42,42,]),'assignment_expression':([33,34,38,64,97,100,],[43,43,43,43,43,43,]),'while_iteration':([33,34,38,64,97,100,],[45,45,45,45,45,45,]),'do_while_iteration':([33,34,38,64,97,100,],[46,46,46,46,46,46,]),'assignment_operator':([36,],[51,]),'return_statement':([37,],[58,]),'val':([51,59,61,62,63,83,87,104,],[67,71,75,76,75,75,99,75,]),'condition':([61,63,83,104,],[73,77,98,107,]),'logical_operator':([73,77,98,107,],[83,83,83,83,]),'comparison_operator':([75,],[87,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> program','start',1,'p_start','parser.py',163),
  ('program -> elements','program',1,'p_program','parser.py',171),
  ('header -> PREPROCESSOR INCLUDE LIBRARY','header',3,'p_header','parser.py',179),
  ('elements -> element','elements',1,'p_elements','parser.py',185),
  ('elements -> element elements','elements',2,'p_elements','parser.py',186),
  ('element -> function_definition','element',1,'p_element','parser.py',196),
  ('element -> void_function_definition','element',1,'p_element','parser.py',197),
  ('element -> header','element',1,'p_element','parser.py',198),
  ('element -> empty','element',1,'p_element','parser.py',199),
  ('function_definition -> type ID PARENTHESE_LEFT function_parameters PARENTHESE_RIGHT BRACE_LEFT expressions return_statement BRACE_RIGHT','function_definition',9,'p_function_definition','parser.py',206),
  ('void_function_definition -> VOID ID PARENTHESE_LEFT function_parameters PARENTHESE_RIGHT BRACE_LEFT expressions BRACE_RIGHT','void_function_definition',8,'p_void_function_definition','parser.py',212),
  ('function_parameters -> type ID','function_parameters',2,'p_function_parameters','parser.py',218),
  ('function_parameters -> type ID COMMA function_parameters','function_parameters',4,'p_function_parameters','parser.py',219),
  ('function_parameters -> empty','function_parameters',1,'p_function_parameters','parser.py',220),
  ('expressions -> expression','expressions',1,'p_expressions','parser.py',230),
  ('expressions -> expression expressions','expressions',2,'p_expressions','parser.py',231),
  ('expressions -> empty','expressions',1,'p_expressions','parser.py',232),
  ('expression -> conditional_expression','expression',1,'p_expression','parser.py',243),
  ('expression -> iteration_expression','expression',1,'p_expression','parser.py',244),
  ('expression -> print_expression','expression',1,'p_expression','parser.py',245),
  ('expression -> assignment_expression','expression',1,'p_expression','parser.py',246),
  ('expression -> empty','expression',1,'p_expression','parser.py',247),
  ('assignment_expression -> ID assignment_operator val SEMICOLON','assignment_expression',4,'p_assignment_expression','parser.py',253),
  ('assignment_expression -> ID assignment_operator ID SEMICOLON','assignment_expression',4,'p_assignment_expression','parser.py',254),
  ('assignment_operator -> ASSIGN','assignment_operator',1,'p_assignment_operator','parser.py',261),
  ('assignment_operator -> INCREMENTS_ASSIGN','assignment_operator',1,'p_assignment_operator','parser.py',262),
  ('assignment_operator -> DECREMENTS_ASSIGN','assignment_operator',1,'p_assignment_operator','parser.py',263),
  ('assignment_operator -> MULTIPLIES_ASSIGN','assignment_operator',1,'p_assignment_operator','parser.py',264),
  ('assignment_operator -> DIVIDES_ASSIGN','assignment_operator',1,'p_assignment_operator','parser.py',265),
  ('assignment_operator -> MODULUS_ASSIGN','assignment_operator',1,'p_assignment_operator','parser.py',266),
  ('print_expression -> COUT OUTPUT val SEMICOLON','print_expression',4,'p_print_expression','parser.py',273),
  ('iteration_expression -> while_iteration','iteration_expression',1,'p_iteration_expression','parser.py',281),
  ('iteration_expression -> do_while_iteration','iteration_expression',1,'p_iteration_expression','parser.py',282),
  ('while_iteration -> WHILE PARENTHESE_LEFT condition PARENTHESE_RIGHT BRACE_LEFT expressions BRACE_RIGHT','while_iteration',7,'p_while_iteration','parser.py',289),
  ('do_while_iteration -> DO BRACE_LEFT expressions BRACE_RIGHT WHILE PARENTHESE_LEFT condition PARENTHESE_RIGHT SEMICOLON','do_while_iteration',9,'p_do_while_iteration','parser.py',295),
  ('conditional_expression -> IF PARENTHESE_LEFT condition PARENTHESE_RIGHT BRACE_LEFT expressions BRACE_RIGHT','conditional_expression',7,'p_conditional_expression','parser.py',303),
  ('condition -> NOT ID','condition',2,'p_condition','parser.py',309),
  ('condition -> condition logical_operator condition','condition',3,'p_condition','parser.py',310),
  ('condition -> val comparison_operator val','condition',3,'p_condition','parser.py',311),
  ('condition -> val','condition',1,'p_condition','parser.py',312),
  ('comparison_operator -> GREATER','comparison_operator',1,'p_comparison_operator','parser.py',323),
  ('comparison_operator -> LESS','comparison_operator',1,'p_comparison_operator','parser.py',324),
  ('comparison_operator -> GREATER_OR_EQUAL','comparison_operator',1,'p_comparison_operator','parser.py',325),
  ('comparison_operator -> LESS_OR_EQUAL','comparison_operator',1,'p_comparison_operator','parser.py',326),
  ('comparison_operator -> NOT_EQUAL','comparison_operator',1,'p_comparison_operator','parser.py',327),
  ('comparison_operator -> EQUAL','comparison_operator',1,'p_comparison_operator','parser.py',328),
  ('logical_operator -> AND','logical_operator',1,'p_logical_operator','parser.py',334),
  ('logical_operator -> OR','logical_operator',1,'p_logical_operator','parser.py',335),
  ('return_statement -> RETURN val SEMICOLON','return_statement',3,'p_return_statement','parser.py',342),
  ('val -> FLOAT_VAL','val',1,'p_val','parser.py',349),
  ('val -> INT_VAL','val',1,'p_val','parser.py',350),
  ('val -> ID','val',1,'p_val','parser.py',351),
  ('type -> INT','type',1,'p_type','parser.py',358),
  ('type -> FLOAT','type',1,'p_type','parser.py',359),
  ('type -> STRING','type',1,'p_type','parser.py',360),
  ('type -> CHAR','type',1,'p_type','parser.py',361),
  ('type -> DOUBLE','type',1,'p_type','parser.py',362),
  ('type -> VOID','type',1,'p_type','parser.py',363),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',373),
]
