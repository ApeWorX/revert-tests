from decimal import Decimal

import ape


def test_AssertRaise(AssertRaise, owner):
    with ape.reverts(dev_message="assert caused an error."):
        AssertRaise._assert(False, sender=owner)

    with ape.reverts(dev_message="raise caused an error."):
        AssertRaise._raise(sender=owner)


def test_BadConversion(BadConversion, owner):
    with ape.reverts(dev_message="convertNegativeWei caused an error."):
        BadConversion.convertNegativeWei(-1, sender=owner)


def test_IntegerOverflow(Overflow, owner):
    with ape.reverts(dev_message="signedIntegerMaxAdd caused an error."):
        Overflow.signedIntegerMaxAdd(1, sender=owner)

    with ape.reverts(dev_message="unsignedIntegerMaxAdd caused an error."):
        Overflow.unsignedIntegerMaxAdd(1, sender=owner)

    with ape.reverts(dev_message="signedIntegerMinSub caused an error."):
        Overflow.signedIntegerMinSub(1, sender=owner)

    with ape.reverts(dev_message="unsignedIntegerMinSub caused an error."):
        Overflow.unsignedIntegerMinSub(1, sender=owner)

    with ape.reverts(dev_message="signedIntegerMaxMult caused an error."):
        Overflow.signedIntegerMaxMult(2, sender=owner)

    with ape.reverts(dev_message="unsignedIntegerMaxMult caused an error."):
        Overflow.unsignedIntegerMaxMult(2, sender=owner)

    with ape.reverts(dev_message="signedIntegerMinMult caused an error."):
        Overflow.signedIntegerMinMult(2, sender=owner)

    with ape.reverts(dev_message="decimalMaxAdd caused an error."):
        Overflow.decimalMaxAdd(Decimal(1.0), sender=owner)

    with ape.reverts(dev_message="decimalMinSub caused an error."):
        Overflow.decimalMinSub(Decimal(1.0), sender=owner)

    with ape.reverts(dev_message="decimalMaxMult caused an error."):
        Overflow.decimalMaxMult(Decimal(2.0), sender=owner)

    with ape.reverts(dev_message="decimalMinMult caused an error."):
        Overflow.decimalMinMult(Decimal(2.0), sender=owner)


def test_InvalidByteArray(InvalidByteArray, owner):
    with ape.reverts(dev_message="variableSlice caused an error."):
        InvalidByteArray.variableSlice(33, sender=owner)


def test_OutOfBounds(OutOfBounds, owner):
    with ape.reverts(dev_message="outOfStaticBounds caused an error."):
        OutOfBounds.outOfStaticBounds(10, sender=owner)

    with ape.reverts(dev_message="outOfDynamicBounds caused an error."):
        OutOfBounds.outOfDynamicBounds(10, sender=owner)

    with ape.reverts(dev_message="popEmptyDynArray caused an error."):
        OutOfBounds.popEmptyDynArray(sender=owner)


def test_ReentryError(ReentryError, owner):
    with ape.reverts(dev_message="nonreentrantFunction caused an error."):
        ReentryError.nonreentrantFunction(sender=owner)

    with ape.reverts(dev_message="nestedNonreentrantFunction caused an error."):
        ReentryError.nestedNonreentrantFunction(sender=owner)


def test_ZeroDivision(ZeroDivision, owner):
    with ape.reverts(dev_message="divideByIntegerZero caused an error."):
        ZeroDivision.divideByIntegerZero(0, sender=owner)

    with ape.reverts(dev_message="divideByDecimalZero caused an error."):
        ZeroDivision.divideByDecimalZero(Decimal(0.0), sender=owner)

    with ape.reverts(dev_message="sqrtByNegativeDecimal caused an error."):
        ZeroDivision.sqrtByNegativeDecimal(Decimal(-1.0), sender=owner)
