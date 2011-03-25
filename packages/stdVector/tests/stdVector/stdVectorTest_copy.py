#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

import stdVector

aspects = [
    "simple test"
    ]


def test_0( **kwds):

    vector1 = stdVector.vector( 6, [1.1, 2.2, 3.3])
    vector2 = stdVector.copy( vector1)

    return vector1.compare( vector2)

    
# ------------- do not modify below this line ---------------


def run( **kwds):
    
    allPassed = True
    
    for i, aspect in enumerate( aspects):
        run = eval( 'test_' + str(i))
        utilities.preReport( log, target, aspect)
        passed = run( **kwds)
        utilities.postReport( log, target, aspect, passed)
        allPassed = allPassed and passed

    return allPassed


import  utilities

target = "copy"

log = utilities.picklog()

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id: stdVectorTest_copy.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
