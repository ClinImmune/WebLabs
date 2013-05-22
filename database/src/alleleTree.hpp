#ifndef ALLELE_TREE_HEADER
#define ALLELE_TREE_HEADER

#include <string>
#include <vector>
#include <boost/smart_ptr.hpp>

using std::string;
using std::vector;
using boost::shared_ptr;

// Defines structure for a generic allele
struct allele {
	string loci;
	vector<int> position;
};

// Defines a structure to hold a matrix interpretation of a matrix which has 22
// rows that represent each amino acid type
// from 0-21
// ACDEFGHIKLMNPQRSTVWYX
struct aminoAcidColumn {
    unsigned short acid[21];
};

// Each column is a boolean representation of a letter, which is memory
// inefficient; but, is much quicker for processing tasks
struct sequenceMatrix {
    int sequenceLength;
    vector<aminoAcidColumn> column;
};

// Defines structure for an allele node in the allele tree which is a generic
// tree where each node points to arbitrary amount of children also there is no
// concern for trees to point at an incorrect node in another branch because of
// how data is structured
struct alleleNode {
	int basePairCount;
	int offset;

    allele alleleName;
	string hla_id;
	string sequence;

	vector<shared_ptr<alleleNode> > children;
};

// Defines a shared pointer to an alleleNode
typedef shared_ptr<alleleNode> alleleNodePtr;

// Defines a struct for all of the loci to be used in the lociParentList
struct locus {
    string loci;
    vector<alleleNodePtr> children;
};

// Defines a shared pointer to a locus
typedef shared_ptr<locus> lociPtr;

// Defines a standard class to handle a tree of loci
class AlleleTree {
private:
    // Holds a vector of loci pointers which point to the lowest resolution
    // children
    vector<lociPtr> alleleParentList;
    // Points to the current node
    alleleNodePtr currentNode;
    // Checks to see if a loci exists in the alleleParentList
    bool isNewLoci(string);
    // returns the name of a loci
    string getLoci(string);
    // returns the matrix form of a sequence
    sequenceMatrix generateMatrix(string);
public:
    // Constructor and destructor
    AlleleTree();
    ~AlleleTree();
    
    // Returns a pointer to an allele to access information from it
    alleleNodePtr getAllele(allele);
    // Inserts a new allele from data in parameters, will be referenced
    void insertAllele(alleleNode&);
    void updateAlleleOffset(allele, string);
    void updateAllele(alleleNode&);
};

///////////////////////////////////////////////////////////////////////////////
// Private methods
///////////////////////////////////////////////////////////////////////////////
bool AlleleTree::isNewLoci(string this_loci) {
    for(int i = 0; i < alleleParentList.size(); i++) {
        if(this_loci.compare(alleleParentList.at(i)->loci) == 0)
            return true;
    }
    return false;
}

///////////////////////////////////////////////////////////////////////////////
// Public methods
///////////////////////////////////////////////////////////////////////////////

AlleleTree::AlleleTree() {/*Creates empty object*/}

AlleleTree::~AlleleTree() {
    alleleParentList.clear();
}

void AlleleTree::insertAllele(alleleNode &this_allele) {
    // Check is the loci is in the parent list
    bool new_loci = true;
    for(int i = 0; i < alleleParentList.size(); i++) {
        if(this_allele
                .alleleName
                .loci
                .compare(alleleParentList
                .at(i)->loci) == 0
        ){
            new_loci = false;
        }
    }
    
    // If the loci is new, create a new allele parent, append the proper number
    // of children, and point currentNode to the last child
    if (new_loci) {
        alleleNodePtr blah(new alleleNode)
    }
    // Iterate through tree until the allele is inserted
}
void AlleleTree::updateAllele(alleleNode &this_allele) {}
#endif
