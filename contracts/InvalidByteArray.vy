# @version 0.3.7

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@external
def variableSlice(_value: uint256) -> Bytes[32]:
	list: bytes32 = empty(bytes32)
	return slice(list, convert(0, uint256), _value) # dev: variableSlice caused an error.
