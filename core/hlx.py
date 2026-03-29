from core.multiscale import multiscale_rese
from core.color import restore_color
from core.frequency import frequency_match_local

def hlx_reconstruct(original, corrupted, region, config):

    structure = multiscale_rese(original, corrupted, region)

    colored = restore_color(original, structure)

    final = frequency_match_local(
        original,
        colored,
        region,
        strength=config["freq_strength"]
    )

    return final