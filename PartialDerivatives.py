from __future__ import division

def PartialDerivatives(func, dpar, prettyprint=None, *params):
	'''
	PartialDerivatives(func, dpar, *params) # or **params for dictionary notation.
	
	func:   str, the function equation.  Not name, but the math of the function.  
			Make sure the parameters within the function match all of those parameters 
			within the parameter list.
			
			*** WARNING ***: sympy requires input of
			ln for natural log and 
			log for log base 10
			However, it outputs log and log10.
	
	dpar:	str, parameter you want to take the derivative with respect to. 'alpha'
	
	params:	list of str, pass a list of strings containing the parameter names.  
			Make sure they match all of those included in the function.
	
	
	
	EXAMPLE:  
	
	lower = 'energy * norm_band *((energy/enorm)**alpha)*(exp(-((energy*(2.+alpha))/epeak)))'
	
	pars = 'alpha beta epeak norm_band enorm energy'.split(' ')

	PartialDerivatives(func=lower, dpar='epeak', *pars)
	
	'''
	import sympy
	from sympy import mpmath, integrate, diff, exp, log, ln, sqrt, lambdify
	from sympy import Function, Symbol
	# in this program, sympy uses log for log10 and ln for natural log.
	from sympy.parsing.sympy_parser import parse_expr
	from sympy.mpmath import atanh
	#enorm		= Symbol('enorm', real=True)
	#energy		= Symbol('energy', real=True)
	
	
	for par in params:
		locals()[par] = Symbol('%s'%par, real=True)
		
	answer	= diff(eval(func), eval(dpar), method='quad')
	return answer

