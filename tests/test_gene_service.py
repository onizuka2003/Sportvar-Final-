from gene_service import obtener_region_gen

def test_gen_existente():
    region = obtener_region_gen("COL5A1")
    assert region is not None
    assert region["chrom"] == "9"

def test_gen_inexistente():
    region = obtener_region_gen("GEN_INVENTADO")
    assert region is None