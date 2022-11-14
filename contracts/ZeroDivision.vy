# @version 0.3.7

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@external
def divideByIntegerZero(_value: int128) -> int128:
	return 1 / _value # dev: divideByIntegerZero caused an error.

@external
def divideByDecimalZero(_value: decimal) -> decimal:
	return 1.0 / _value # dev: divideByDecimalZero caused an error.

@external
def sqrtByNegativeDecimal(_value: decimal) -> decimal: # dev: sqrtByNegativeDecimal caused an error.
	return sqrt(_value)
