from decimal import Decimal

import ape


def test_AssertRaise(AssertRaise, owner):
    with ape.reverts(dev_message="dev: assert caused an error."):
        AssertRaise._assert(False, sender=owner)

    with ape.reverts(dev_message="dev: raise caused an error."):
        AssertRaise._raise(sender=owner)


def test_BadConversion(BadConversion, owner):
    with ape.reverts(dev_message="dev: convertNegativeWei caused an error."):
        BadConversion.convertNegativeWei(-1, sender=owner)


def test_IntegerOverflow(Overflow, owner):
    with ape.reverts(dev_message="dev: signedIntegerMaxAdd caused an error."):
        Overflow.signedIntegerMaxAdd(1, sender=owner)

    with ape.reverts(dev_message="dev: unsignedIntegerMaxAdd caused an error."):
        Overflow.unsignedIntegerMaxAdd(1, sender=owner)

    with ape.reverts(dev_message="dev: signedIntegerMinSub caused an error."):
        Overflow.signedIntegerMinSub(1, sender=owner)

    with ape.reverts(dev_message="dev: unsignedIntegerMinSub caused an error."):
        Overflow.unsignedIntegerMinSub(1, sender=owner)

    with ape.reverts(dev_message="dev: signedIntegerMaxMult caused an error."):
        Overflow.signedIntegerMaxMult(2, sender=owner)

    with ape.reverts(dev_message="dev: unsignedIntegerMaxMult caused an error."):
        Overflow.unsignedIntegerMaxMult(2, sender=owner)

    with ape.reverts(dev_message="dev: signedIntegerMinMult caused an error."):
        Overflow.signedIntegerMinMult(2, sender=owner)

    with ape.reverts(dev_message="dev: decimalMaxAdd caused an error."):
        Overflow.decimalMaxAdd(Decimal(1.0), sender=owner)

    with ape.reverts(dev_message="dev: decimalMinSub caused an error."):
        Overflow.decimalMinSub(Decimal(1.0), sender=owner)

    with ape.reverts(dev_message="dev: decimalMaxMult caused an error."):
        Overflow.decimalMaxMult(Decimal(2.0), sender=owner)

    with ape.reverts(dev_message="dev: decimalMinMult caused an error."):
        Overflow.decimalMinMult(Decimal(2.0), sender=owner)


def test_InvalidByteArray(InvalidByteArray, owner):
    with ape.reverts(dev_message="dev: variableSlice caused an error."):
        InvalidByteArray.variableSlice(33, sender=owner)


def test_OutOfBounds(OutOfBounds, owner):
    with ape.reverts(dev_message="dev: outOfStaticBounds caused an error."):
        OutOfBounds.outOfStaticBounds(10, sender=owner)

    with ape.reverts(dev_message="dev: outOfDynamicBounds caused an error."):
        OutOfBounds.outOfDynamicBounds(10, sender=owner)

    with ape.reverts(dev_message="dev: popEmptyDynArray caused an error."):
        OutOfBounds.popEmptyDynArray(sender=owner)


def test_ReentryError(ReentryError, owner):
    with ape.reverts(dev_message="dev: nonreentrantFunction caused an error."):
        ReentryError.nonreentrantFunction(sender=owner)

    with ape.reverts(dev_message="dev: nestedNonreentrantFunction caused an error."):
        ReentryError.nestedNonreentrantFunction(sender=owner)


def test_ZeroDivision(ZeroDivision, owner):
    with ape.reverts(dev_message="dev: divideByIntegerZero caused an error."):
        ZeroDivision.divideByIntegerZero(0, sender=owner)

    with ape.reverts(dev_message="dev: divideByDecimalZero caused an error."):
        ZeroDivision.divideByDecimalZero(Decimal(0.0), sender=owner)

    with ape.reverts(dev_message="dev: sqrtByNegativeDecimal caused an error."):
        ZeroDivision.sqrtByNegativeDecimal(Decimal(-1.0), sender=owner)
