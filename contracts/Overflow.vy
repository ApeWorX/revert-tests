# @version 0.3.7

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@external
def signedIntegerMaxAdd(_value: int256) -> int256:
	return max_value(int256) + _value   # dev: signedIntegerMaxAdd caused an error.

@external
def unsignedIntegerMaxAdd(_value: uint256) -> uint256:
	return max_value(uint256) + _value   # dev: unsignedIntegerMaxAdd caused an error.

@external
def signedIntegerMinSub(_value: int256) -> int256:
	return min_value(int256) - _value   # dev: signedIntegerMinSub caused an error.

@external
def unsignedIntegerMinSub(_value: uint256) -> uint256:
	return min_value(uint256) - _value   # dev: unsignedIntegerMinSub caused an error.

@external
def signedIntegerMaxMult(_value: int256) -> int256:
	return max_value(int256) * _value   # dev: signedIntegerMaxMult caused an error.

@external
def unsignedIntegerMaxMult(_value: uint256) -> uint256:
	return max_value(uint256) * _value   # dev: unsignedIntegerMaxMult caused an error.

@external
def signedIntegerMinMult(_value: int256) -> int256:
	return min_value(int256) * _value   # dev: signedIntegerMinMult caused an error.

@external
def decimalMaxAdd(_value: decimal) -> decimal:
	return max_value(decimal) + _value # dev: decimalMaxAdd caused an error.

@external
def decimalMinSub(_value: decimal) -> decimal:
	return min_value(decimal) - _value # dev: decimalMinSub caused an error.

@external
def decimalMaxMult(_value: decimal) -> decimal:
	return max_value(decimal) * _value # dev: decimalMaxMult caused an error.

@external
def decimalMinMult(_value: decimal) -> decimal:
	return max_value(decimal) * _value # dev: decimalMinMult caused an error.
