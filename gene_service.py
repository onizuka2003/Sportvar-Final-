GENES = {
    "ACTN3": {"chrom": "11", "start": 66560624, "end": 66587985},
    "COL1A1": {"chrom": "17", "start": 50184101, "end": 50201631},
    "COL5A1": {"chrom": "9", "start": 134641803, "end": 134844843},
}

def obtener_region_gen(gen: str):
    if not gen:
        return None
    return GENES.get(gen.upper())