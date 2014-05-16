namespace OtherNamespace
{

}


namespace OtherNamespace {
    class SomeDerivedClass: public SomeTestingNamespace 
    {

    };
}

namespace OtherNamespace {
    class SomeTrashyClassInBetween {

    };

    template <class ParameterClass>
    void someFreeFunction(SomeTestingNamespace::Type aNamespaceType, std::vector<SomeTestingNamespace::OtherType> aNamespaceTypeVector);
}

using namespace SomeTestingNamespace;
