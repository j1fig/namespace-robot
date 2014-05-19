namespace ANamespace
{

}


namespace ANamespace {
    class SomeDerivedClass: public SomeTestingNamespace 
    {

    };
}

namespace ANamespace {
    class SomeTrashyClassInBetween {

    };

    template <class ParameterClass>
    void someFreeFunction(ANamespace::Type aNamespaceType, std::vector<ANamespace::OtherType> aNamespaceTypeVector);
}

using namespace ANamespace;
