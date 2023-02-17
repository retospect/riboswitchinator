import RNA

def test_folding():
    settings = RNA.md()
    fc = RNA.fold_compound("GGGGGGGGGGAAAAACCCCCCCCCC", settings)
    structure, mfe = fc.mfe()
    assert structure ==    "((((((((((.....)))))))))))"
