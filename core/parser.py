from typing import List, Dict

BEGIN_IONS = "BEGIN IONS"
END_IONS = "END IONS"

def parse_ions_block(block: Dict) -> Dict:
    """
    Parses a single ion block and returns a dictionary containing the metadata and masses.
    """
    ions_data = {}
    masses = []

    lines = block.strip().split("\n")
    for line in lines:
        if BEGIN_IONS in line:
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            ions_data[key.strip()] = value.strip()  # Ensuring no unwanted spaces
        else:
            mz, intensity = map(float, line.split())
            masses.append((mz, intensity))

    ions_data["masses"] = masses
    return ions_data

def parse_mgf(data: str) -> List[Dict]:
    """
    Parses the entire mgf data and returns a list of dictionaries, each representing an ion block.
    """
    blocks = data.strip().split(END_IONS)
    return [parse_ions_block(block) for block in blocks if block.strip()]

def pick_mgf(
    mgf_list: List[Dict], target_mass: float, tense_threshold: float = 100, digits: int = 3
) -> List[Dict]:
    """
    Selects ion blocks that have a mass matching the target_mass within the specified number of decimal places 
    and with an intensity greater than the tense_threshold.
    """
    return [
        peak for peak in mgf_list 
        if any(
            round(target_mass, digits) == round(_mass, digits) and tense > tense_threshold
            for _mass, tense in peak["masses"]
        )
    ]
