# @version 0.3.7

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@external
def _assert(_value: bool):
	assert _value # dev: assert caused an error.

@external
def _raise():
	raise # dev: raise caused an error.
