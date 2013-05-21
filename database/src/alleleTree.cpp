#include <vector>
#include <string>
#include <boost/smart_ptr.hpp>

typedef std::string str;

struct alleleVector {
    str loci;
    std::vector<int> pos;
};

struct alleleNode {
    int basePairCount;
    int offset;
    
    alleleVector allele;
    str hla_id;
    str sequence;
    
    std::vector<boost::shared_ptr<alleleNode> > children;
};

typedef boost::shared_ptr<alleleNode> alleleNodePtr;

int main() {
    return 0;
}
