// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef H_DANSE_AXISMAPPER
#define H_DANSE_AXISMAPPER


#include "Exception.h"

namespace DANSE {

  struct OutOfBound : public Exception
  {
    OutOfBound() : Exception( "out of bound" ) 
    {}
  };
  
  // map data value to index
  template <typename DataType, typename IndexType>
  class AxisMapper {

  public:
    
    typedef DataType datatype;
    typedef IndexType indextype;
  
    virtual IndexType operator() ( const DataType & data ) const = 0;
    virtual ~AxisMapper() {};
  };

}

#endif


// version
// $Id$

// End of file 