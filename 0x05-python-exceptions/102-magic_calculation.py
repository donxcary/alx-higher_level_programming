#!/usr/bin/python3

def magic_calculation(a, b):
	result = 0 # LOAD_CONST 1 (0) and STORE_FAST 2 (result)
		for i in range(1, 3):  # SETUP_LOOP 94 (to 103), LOAD_GLOBAL 0 (range), LOAD_CONST 2 (1), LOAD_CONST 3 (3), CALL_FUNCTION 2, GET_ITER, and FOR_ITER 77 (to 102)
			try: # SETUP_EXCEPT 49 (to 80)
				if i > a: # LOAD_FAST 3 (i), LOAD_FAST 0 (a), COMPARE_OP 4 (>), and POP_JUMP_IF_FALSE 58
					raise Exception("Too Far") # LOAD_GLOBAL 1 (Exception), LOAD_CONST 4 ('Too far'), CALL_FUNCTION 1, and RAISE_VARARGS 1

			else: # JUMP_FORWARD 18 (to 76)
				result += a ** b / i # LOAD_FAST 2 (result), LOAD_FAST 0 (a), LOAD_FAST 1 (b), BINARY_POWER, LOAD_FAST 3 (i), BINARY_TRUE_DIVIDE, INPLACE_ADD, and STORE_FAST 2 (result)
			except: # POP_BLOCK, POP_TOP, POP_TOP, POP_TOP, and POP_EXCEPT
				result = b + a # LOAD_FAST 1 (b), LOAD_FAST 0 (a), BINARY_ADD, and STORE_FAST 2 (result)
			break # BREAK_LOOP
	return result # LOAD_FAST 2 (result) and RETURN_VALUE
