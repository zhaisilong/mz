def parse_ions_block(block):
    ions_data = {}
    masses = []

    lines = block.strip().split("\n")
    for line in lines:
        if "BEGIN IONS" in line:
            continue
        if "=" in line:
            key, value = line.split("=")
            ions_data[key] = value
        else:
            mz, intensity = map(float, line.split())
            masses.append((mz, intensity))

    ions_data["masses"] = masses
    return ions_data

def parse_mgf(data):
    blocks = data.strip().split("END IONS")
    parsed_data = [parse_ions_block(block) for block in blocks if block.strip()]

    return parsed_data

def pick_mgf(mgf_list, target_mass, tense_threshold=100, digits=3):
    selected_mgf = []
    for peak in mgf_list:
        for _mass, tense in peak["masses"]:
            # 保证小数点后三位一致
            if round(target_mass, digits) == round(_mass, digits) and tense > tense_threshold:
                selected_mgf.append(peak)
                break  # 一旦找到了匹配的mass，就跳出内部循环
    return selected_mgf