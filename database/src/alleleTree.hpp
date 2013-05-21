// W00t! I win!!!

#ifndef ALLELE_TREE_HEADER
#define ALLELE_TREE_HEADER

#include <string>
#include <vector>
#include <boost/smart_ptr.hpp>
#include <boost/multi_array.hpp>

typedef std::string str;

// Defines structure for a generic allele
struct allele {
	str loci;
	std::vector<int> position;
};

// Defines a structure to hold a matrix interpretation of a matrix which has 22
// rows that represent each amino acid type
// from 0-21
// ACDEFGHIKLMNPQRSTVWYX
struct aminoAcidRow {
    unsigned short acid[21];
};

// Each column is a boolean representation of a letter, which is memory
// inefficient; but, is much quicker for processing tasks
struct sequenceMatrix {
    int sequenceLength;
    std::vector<aminoAcidColumn> column;
};

// Defines structure for an allele node in the allele tree which is a generic
// tree where each node points to arbitrary amount of children also there is no
// concern for trees to point at an incorrect node in another branch because of
// how data is structured
struct alleleNode {
	int basePairCount;
	int offset;

    allele alleleName;
	str hla_id;
	str sequence;

	std::vector<boost::shared_ptr<alleleNode> > children;
};

// Defines a shared pointer to an alleleNode
typedef boost::shared_ptr<alleleNode> alleleNodePtr;

// Defines a struct for all of the loci to be used in the lociParentList
struct locus {
    str loci;
    std::vector<alleleNodePtr> children;
};

// Defines a shared pointer to a locus
typedef boost::shared_ptr<locus> lociPtr;

// Defines a standard class to handle a tree of loci
class AlleleTree {
private:
    // Holds a vector of loci pointers which point to the lowest resolution
    // children
    std::vector<lociPrt> alleleParentList;
    // Points to the current node
    alleleNodePtr currentNode;
    // Checks to see if a loci exists in the alleleParentList
    bool isNewLoci(str);
    // returns the name of a loci
    str getLoci(str);
    // returns the matrix form of a sequence
    sequenceMatrix generateMatrix(str);
public:
    // Constructor and destructor
    AlleleTree();
    ~AlleleTree();
    
    // Returns a pointer to an allele to access information from it
    alleleNodePtr getAllele(allele);
    // Inserts a new allele from data in parameters, will be referenced
    void insertAllele(str this_sequence, allele this_allele)
};

#endif
